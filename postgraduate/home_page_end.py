# 导入库
import pymysql,config,time,os
import matplotlib.pyplot as plt
import numpy as np
from flask import Flask, render_template, request,redirect,send_from_directory

root = os.path.join(os.path.dirname(os.path.abspath(__file__)), "templates")

#准备
time_start = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) # 记录当前时间
print('>> 当前时间：',time_start)
print('>> 开始处理……')

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

# 从数据库中查询用户信息
def search_mysql():
    # 连接数据库
    conn,cursor = con_sql()

#查询new_school_area数据的 sql语句
    sql='select * from register'
    
    try:
        #执行sql语句
        cursor.execute(sql)
        results=cursor.fetchall()
        # print(results)
        return results
    except:
        print('用户信息查询失败')

# 创建注册账户密码表，并存到数据库
def insert_register(value):
    # 连接数据库
    conn,cursor = con_sql()

    #创建注册用户密码表
    sql_creat = '''CREATE TABLE IF NOT EXISTS register(
        `ID` INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
        `Username` CHAR(30),
        `Password` CHAR(30),
        `Secretguard` CHAR(30)
        )'''
    
    cursor.execute(sql_creat)

    # 数据库支持中文
    cursor.execute("alter table register convert to character set utf8mb4;")
    # 插入数据命令
    sql_insert = "INSERT INTO register(Username,Password,Secretguard) VALUES (%s,%s,%s)"
    try:
        cursor.execute(sql_insert, value)
        conn.commit()
        print('注册信息插入数据成功')
    except:
        conn.rollback()
        print("注册信息插入数据失败")
    conn.close()

# 创建调查问卷表，并存到数据库
def insert_question(value):
    # 连接数据库
    conn,cursor = con_sql()

    #创建调查问卷表
    sql_creat = '''CREATE TABLE IF NOT EXISTS question(
        `ID` INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
        `Nickname` CHAR(30),
        `sex` CHAR(30),
        `grad` CHAR(30),
        `content_one` CHAR(100),
        `content_two` CHAR(100),
        `content_three` CHAR(100)
        )'''
    
    cursor.execute(sql_creat)

    # 数据库支持中文
    cursor.execute("alter table question convert to character set utf8mb4;")
    # 插入数据命令
    sql_insert = "INSERT INTO question(Nickname,sex,grad,content_one,content_two,content_three) VALUES (%s,%s,%s,%s,%s,%s)"
    try:
        cursor.execute(sql_insert, value)
        conn.commit()
        print('问卷信息插入数据成功')
    except:
        conn.rollback()
        print("问卷信息插入数据失败")
    conn.close()

# 找回密码
@app.route('/find', methods=("GET", "POST"))
def findback():
    if request.method == "GET":
        return render_template("findback.html")
    if request.method == "POST":

        # 获取所有输入信息
        user_info = request.form.to_dict()

        # 密保查找信息
        for secret in search_mysql():
            if user_info.get("findback") == secret[3]:
                error_six = "用户名:" + secret[1]
                error_seven = "密码:" + secret[2]
                return render_template("findback.html",error_name = error_six,error_pass = error_seven)
        return render_template("findback.html")

@app.route("/")
def index():
    return "<h1>请转移 /login</h1>"

# 表单网页
@app.route("/question",methods=("GET", "POST"))
def question():
    if request.method == "GET":
        return render_template("questionnaire_try.html")
    if request.method == "POST":
        # 获取所有输入信息
        user_info = request.form.to_dict()

        Nickname = request.values.get('Nickname')
        sex = request.values.get('sex')
        grad = request.values.get('grad')
        content_one = request.values.get('content_one')
        content_two = request.values.get('content_two')
        content_three = request.values.get('content_three')

        # 插入调查问卷信息
        insert_question([Nickname,sex,grad,content_one,content_two,content_three])

        return render_template("success.html")


@app.route("/login", methods=("GET", "POST"))
def login():
    if request.method == "GET":
        return render_template("home_page_end.html")
    
    if request.method == "POST":

        # 获取所有输入信息
        user_info = request.form.to_dict()

        # 用户登录
        if user_info.get("username") != None and user_info.get("password") != None:
            length = len(search_mysql())
            which = 0
            while(which<=length):
                for mess in search_mysql():
                    if user_info.get("username") == mess[1] and user_info.get("password") == mess[2]:
                        # 获取所有输入信息
                        return redirect("/question")
                        which += 1
                error_five = "!!! 用户名密码错误。"
                return render_template("home_page_end.html",error = error_five)

        # 无用户名，注册信息存储
        if user_info.get("Username") != None and user_info.get("Password") != None:
            Username = request.values.get('Username')
            Password = request.values.get('Password')
            Passwordrepeat = request.values.get('Passwordrepeat')
            Secretguard = request.values.get("Secretguard")

            # 输入格式判断
            if len(Password)>8 or len(Password)<3 or (Password.isdigit() == False and Password.isalpha() == False and Password.isalnum() == False):
                error_three = "!!! 密码输入格式有误。"
                return render_template("home_page_end.html",error = error_three)
            if Passwordrepeat != Password:
                error_one = "!!! 两次输入密码不同，请重新注册。"
                return render_template("home_page_end.html",error = error_one)
            if len(Username) >8 or len(Username)<1 or (Username.isdigit() == False and Username.isalpha() == False and Username.isalnum() == False):
                error_two = "!!! 用户名输入格式有误。"
                return render_template("home_page_end.html",error = error_two)
            if len(Secretguard)>8 or len(Secretguard)<3 or (Secretguard.isdigit() == False and Secretguard.isalpha() == False and Secretguard.isalnum() == False):
                error_four = "!!! 密保输入格式有误。"
                return render_template("home_page_end.html",error = error_four)

            # 注册信息存储
            else:
                insert_register([Username,Password,Secretguard])
                error_eight = "^O^ 恭喜注册成功!"
                return render_template("home_page_end.html",error = error_eight)

    return render_template("404.html")


@app.route("/code")
def code():
    return send_from_directory(root, "all_code.html")

if __name__ == '__main__':
    app.run(debug=True)