import pymysql
con=pymysql.connect(host="localhost",port=3306,database="sqldatabase",user="root",password="root")
crsr=con.cursor()
crsr.execute("create table studentdata(name varchar(55),lastname varchar (55),fathername varchar (55),adress varchar (100))")
query="insert into studentdata(name,lastname,fathername,adress) values('ansh','gadhwal','sanjay','lalbagh')"
crsr.execute(query)

con.commit()
con.close()
crsr.close()    
print("success")
    