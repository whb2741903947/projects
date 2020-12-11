# 爬取考研学校及其地域

# 导入库
import requests
from bs4 import BeautifulSoup
import re
import pymysql

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

def drop_tables():
    # 连接数据库
    conn,cursor = con_sql()

    cursor.execute("drop table if exists school_area;")
    cursor.execute("drop table if exists new_school_area;")
    conn.close()

# 数据库连接及插入数据
def insert_info(value):
    # 连接数据库
    conn,cursor = con_sql()

    #添加数据库表头
    sql_creat = '''CREATE TABLE IF NOT EXISTS school_area(
        `ID` INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
        `name` CHAR(30),
        `area` CHAR(16)    
        )'''
    
    cursor.execute(sql_creat)
    # 数据库支持中文
    cursor.execute("alter table school_area convert to character set utf8mb4;")

    # 插入数据命令
    sql_insert = "INSERT INTO school_area(name,area) VALUES (%s,%s)"
    try:
        cursor.execute(sql_insert, value)
        conn.commit()
        print('插入数据成功')
    except:
        conn.rollback()
        print("插入数据失败")
    conn.close()

# 添加请求头
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.183 Safari/537.36"
}

#从首页拿到各地研究网的url
def geturl():
    url='http://www.chinakaoyan.com/'
    res=requests.get(url,headers=headers)
    soup=BeautifulSoup(res.text,'html.parser')
    data=soup.find_all('div',attrs={'class':'soso_area_box'})
    data=str(data)
    data=str(data)
    pattern=re.compile(r'<a href="(.*?)".*?>(.*?)</a>',re.S)
    item=pattern.findall(data)
    # print(item)
    return  item
 
#拿到一个地区每个学校的学校名称
def getcityhtml(a_list):
    url='http://www.chinakaoyan.com/'+a_list[0]
    res=requests.get(url,headers=headers)
    soup=BeautifulSoup(res.text,'html.parser')
    data=soup.find_all('div',attrs={'class':'colu-info-body'})
    data = str(data)
    pattern = re.compile(r'<div class="item">.*?<h3><a .*?>(.*?)</a></h3>',re.S)
    item = pattern.findall(data)
    for i in item:
        b_list=[]
        b_list.append(i)
        b_list.append(a_list[1])
        insert_info(b_list)
        print(b_list)
 
 
#从geturl返回的url拿到各地信息
def everycity_gethtml():
    a_list=geturl()
    for i in a_list:
        getcityhtml(i)

if __name__ == '__main__':
    drop_tables()
    everycity_gethtml()


# 数据清洗
# 导入库
import pymysql
import pandas as pd
 
# 从数据库中查询数据
def all_info():
    # 连接数据库
    conn,cursor = con_sql()

    # 创建新表储存数据
    sql_creat = '''CREATE TABLE IF NOT EXISTS new_school_area(
        `ID` INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
        `name` CHAR(30),
        `area` CHAR(16)    
        )'''
    cursor.execute(sql_creat)
    # 数据库支持中文
    cursor.execute("alter table new_school_area convert to character set utf8mb4;")

    #sql语句
    sql='select * from school_area'
    
    try:
        #执行sql语句
        cursor.execute(sql)
        results=cursor.fetchall()
        # print(results)
        return results
    except:
        print('error')

def insert(value):
    # 连接数据库
    conn,cursor = con_sql()

    sql = "INSERT INTO new_school_area(name,area) VALUES (%s,%s)"
    try:
        cursor.execute(sql, value)
        conn.commit()
        print('插入数据成功')
    except:
        conn.rollback()
        print("插入数据失败")
    conn.close()

# 构造DataFrame
def school():
    results=all_info()
    name=[]
    locate=[]
    for i in results:
        name.append(i[1])
        locate.append(i[2])
    data={'name':name,'locate':locate}
    df=pd.DataFrame(data)
    # print(df)
    df1=df.drop_duplicates('name',keep='first',inplace=False)  #按照name去除重复行
    
    # 重新存入数据库
    for i in range(len(df1)):
        print(df1.iloc[i])
        insert(list(df1.iloc[i]))
 
 
if __name__ == '__main__':
    school()
