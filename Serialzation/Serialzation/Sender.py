import json
import pymysql
from flask import Flask, jsonify, request
from Serialzation.ansh import empolyee
import requests
from django.http.response import HttpResponse



from django.http import JsonResponse
from flask.wrappers import Response


def connect(self):
    con=pymysql.connect(host = "localhost",port=3306,database ="abhi1",user = "root",password="root")
    crsr = con.cursor()
    crsr.execute("CREATE Table ansh(stuid int(5),stuname varchar(55),slastname varchar(55),stusub varchar(55))")   
    query="insert into ansh(stuid,stuname,slastname,stusub) values(%s,%s,%s,%s)"
    record=[
        (1,"abhishek","gadhwal","maths"),
        (2,"mayur","gorakhpuriya","science"),
        (3,"abhay","gadhwal","biology"),
        (4,"rahul","gorakhpuriya","arts"),
        (5,"ajay","yadav","science"),
        (6,"vinayak","agrawal","maths"),
        (7,"ansh","thakur","agriculture"),
        (8,"rohit","mahajan","science"),
        (9,"shivam","dube","hindi"),
        (10,"virat","kohli","english"),
        (11,"shivam","pawar","sankrit")
        ]
    crsr.executemany(query,record)

    con.commit()
    con.close()
    crsr.close()    
    
def fetch():
    l=[]
    con=pymysql.connect(host = "localhost",port=3306,database ="abhi1",user = "root",password="root")
    crsr = con.cursor()
    query ="select * from ansh"
    crsr.execute(query)
    data=crsr.fetchall()
    for i in data:
        e1=empolyee()
        e1.set_stuid(i[0])
        e1.set_stuname(i[1])
        e1.set_slastname(i[2])
        e1.set_stusub(i[3])
        l.append(e1)
    
    
    con.close()
    crsr.close()
    
    return Response([e1.__dict__ for e1 in l])


print(fetch())
        