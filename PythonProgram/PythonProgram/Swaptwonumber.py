import pymysql
con=pymysql.connect(host="localhost",port=3306,database="new_schema",user="root",password="root")
ansh=con.cursor()
#ansh.execute("create table abhishek(id int (10),name varchar(55),lastname varchar(55),salary varchar (10))")
query="INSERT INTO abhishek (id,name,lastname,salary)VALUES (1,'sanjay','gadhwal',1000)"  
#query="insert into abhishek(id,name,lastname,salary) values(2,'ansh','gadhwal',1000)"
#query="insert into abhishek(id,name,lastname,salary) values(3,'abhishek','gadhwal',200233)"
#query="DELETE FROM abhishek WHERE name='sanjay'"
#query="SELECT * FROM abhishek WHERE id= 2"
ansh.execute(query) 
con.commit()
con.close()
ansh.close()