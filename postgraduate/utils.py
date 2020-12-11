import time,jieba,pymysql
import pandas as pd
from threading import Timer # 定时函数
from sklearn.feature_extraction.text import CountVectorizer # 词频计算

# 百度文本检测API连接
from aip import AipContentCensor
APP_ID = "22982291"
API_KEY = "mnnvDxGFRVENkCdANdqYLqVl"
SECRET_KEY = "k2GUNHGt8GnbTxemGrtb3RsucBY6wgNs"
client = AipContentCensor(APP_ID, API_KEY, SECRET_KEY)

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

def get_time():
    time_str = time.strftime("%Y{}%m{}%d{} %X")
    return time_str.format("年","月","日")

'''
# 数据库通用查询
def get_conn():
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

def close_conn(conn,cursor):
    cursor.close()
    conn.close()

def qurey(sql,*args):
    conn,cursor = get_conn()
    cursor.execute(sql,args)
    res = cursor.fetchall()
    close_conn(conn,cursor)
    return res

'''
# 没有在数据库调用数据，所以自己构造数据
def get_c1_data():
    res = ("39所","112所","329万","311万")
    return res

# 创建词云表，数据插入数据库
def WordCloud(value):
    # 连接数据库
    conn,cursor = con_sql()
    #创建词云表
    sql_creat = '''CREATE TABLE IF NOT EXISTS wordcloud(
        `ID` INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
        `name` CHAR(30),
        `value` CHAR(30)
        )'''
    
    cursor.execute(sql_creat)
    # 数据库支持中文
    cursor.execute("alter table wordcloud convert to character set utf8mb4;")
    # 插入数据命令
    sql_insert = "INSERT INTO wordcloud(name,value) VALUES (%s,%s)"
    try:
        cursor.execute(sql_insert, value)
        conn.commit()
        print('词云信息插入数据成功')
    except:
        conn.rollback()
        print("词云信息插入数据失败")
    conn.close()

# 收集所有评价，文本检测，返回词频
def search_questions():
    # 连接数据库
    conn,cursor = con_sql()

#查询question数据的 sql语句
    sql='select * from question'
    
    try:
        #执行sql语句
        cursor.execute(sql)
        results=cursor.fetchall()
        # print(results)
    except:
        print('问卷信息查询失败')
    standard_text = []
    # 文本检测
    """ 调用文本审核接口 """
    for m in results:
        for n in range(4,7):
            check_text = client.textCensorUserDefined(m[n])
            if check_text.get("conclusion") != "合规":
                continue
            else:
                standard_text.append(m[n])
    # 文本分词处理
    jieba_text = []         # 文本分词结果
    for each in standard_text:
        jieba_text.append(" ".join(jieba.cut(each)))

    # 建立CountVectorizer模型
    stop_words_list = ["就是","就"]
    count_vec = CountVectorizer(min_df=2,max_df=50,max_features=50,stop_words=stop_words_list)
    # 训练模型，计算词频矩阵
    sparse_result_count = count_vec.fit_transform(jieba_text)
    # 输出关键词
    text_key = count_vec.get_feature_names()        # 关键词
    text_value = sparse_result_count.toarray().sum(axis=0)  # 对应关键字词频

    # 若表存在则删除
    cursor.execute("drop table if exists wordcloud;")
    # 插入数据库
    for i in range(len(text_key)):
        WordCloud([text_key[i],str(text_value[i])])

# 词云数据读取
def get_word():
    # 连接数据库
    conn,cursor = con_sql()

    #查询wordcloud数据的 sql语句
    sql='select * from wordcloud'
    
    try:
        #执行sql语句
        cursor.execute(sql)
        word_results=cursor.fetchall()
        # print(word_results)
    except:
        print('问卷信息查询失败')
    data_text = []
    for i in word_results:
        data_text.append({"name":i[1],"value":i[2]})
    return data_text

# 获取表单考研男女比例
def sex_rate():
    # 连接数据库
    conn,cursor = con_sql()

    #查询wordcloud数据的 sql语句
    sql='select * from question'
    
    try:
        #执行sql语句
        cursor.execute(sql)
        sex_results=cursor.fetchall()
        # print(sex_results)
    except:
        print('问卷性别信息查询失败')
    
    # 数据处理
    sex_data = []
    grat_data = []
    for i in sex_results:
        sex_data.append(i[2])
        grat_data.append(i[3])
    data_sex={'sex':sex_data,'yes_no':grat_data}
    df_sex=pd.DataFrame(data_sex)
    data_result = df_sex.groupby(["yes_no",'sex']).size()
    yes_female = data_result['graduate_yes', 'female']
    yes_male = data_result['graduate_yes', 'male']
    # print(yes_female/(yes_male+yes_female))
    return yes_female/(yes_male+yes_female)

if __name__ == '__main__':
    sex_rate()