# -*- coding: utf-8 -*-
import pymysql,time,os,glob
import pandas as pd
from flask import Flask,render_template,jsonify
import utils

app = Flask(__name__)

# 连接数据库统一接口
def con_sql():
    # 连接数据库
    config = {
    "host":"127.0.0.1",
    "port":3306,
    "user":"root",
    "password":'mysqlksh',
    "charset":'utf8mb4',
    "database":"hao1"
}
    conn = pymysql.connect(**config)
    cursor = conn.cursor()  # 执行完毕返回的结果默认以元组显示
    return conn,cursor

#准备
time_start = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) # 记录当前时间
print('>> 当前时间：',time_start)
print('>> 开始处理……')

# 从数据库中查询数据
def data_mysql():
    # 连接数据库
    conn,cursor = con_sql()

#查询new_school_area数据的 sql语句
    sql='select * from new_school_area'
    
    try:
        #执行sql语句
        cursor.execute(sql)
        results=cursor.fetchall()
        # print(results)
        return results
    except:
        print('error')

# 构建DataFrame,并按照地区分组计数,转换为字典
def creat_DF():
    data_pd = pd.DataFrame(data_mysql(),columns=['id','name','area'])
    # print(data_pd.head(3))

    name = list(data_pd['area'].value_counts().index[:])
    area = list(data_pd['area'].value_counts())
    data_dict = dict(zip(name,area))
    return data_dict

@app.route("/c1")
def get_c1_data():
    data = utils.get_c1_data()
    return jsonify({"confirm":data[0],"suspect":data[1],"heal":data[2],"dead":data[3]})

@app.route("/time")
def get_time():
    return utils.get_time()

@app.route('/school')
def get_data():
    return render_template('postgraduate.html')

@app.route("/center2")
def get_center_data():
    res = []
    for i in creat_DF():
        res.append({"name":i,"value":int(creat_DF().get(i))})
    return jsonify({"data":res})

@app.route("/right2")
def get_right2_data():
    data_text = utils.get_word()
    # print(data_text)
    return jsonify({"data":data_text})

@app.route("/left2")
def get_left2_data():
    data_rate = utils.sex_rate()
    # print(data_rate)
    return jsonify({"data":round(data_rate*100,2)})

# 实时将文本信息存到数据库
@app.route("/ques")
def question():
    unmeaning = utils.search_questions()
    return "unmeaning"


if __name__ == '__main__':
    app.run(debug=True)