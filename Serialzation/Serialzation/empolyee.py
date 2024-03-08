import json
employee ='''{
    "name":"abhishek",
    "age":20,
    "salary":120000,
    "ismarried" : true,
    "girlfriend":null
}'''

    
    

# for deserilazation of json_ string into the pythob dict
#emp = json.loads(employe)
#print(emp)
#print("empolyee name",emp['name'])
#print("empolyee age",emp['age'])
#print("empolyee salary",emp['salary'])
#print("empolyee ismarried",emp['ismaarried'])
#print("empolyee girlfriend",emp['girlfriend'])

with open("ansh.text","r") as f:
 emp_dict  = json.load(f)
print(emp_dict) 

# dumps() = convert the python dict to json string
# dump() = convert the python dict to json  and save to a file
# loads() = convert the json string  to python dict
# load() = convert the json  to python dict and save to a file

# for serilazation of python dict to json string:
#json_string = json.dumps(employee)
#print(json_string)
#with open("ansh.text","w") as f:
#    json.dump(employee,f)
    

















































    
    
        
       
        


  
        