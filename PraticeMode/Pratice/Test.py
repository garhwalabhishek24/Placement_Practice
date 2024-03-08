import pymysql
con = pymysql.connect(host="localhost",port=3306,database="sqldatabase",user="root",password="root")
crsr=con.cursor()
crsr.execute("create table ansh(name varchar(55),lname varchar(55)),adress varchar(55),email varchar(55)")

print("success")