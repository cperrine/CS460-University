from django.http import HttpResponse
import mysql.connector

def index(request):
    return HttpResponse("Hello, world. \nAgain")
def student(request):
    mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="Snaildog13!",    #USE YOUR PASSWORD
    auth_plugin='mysql_native_password',
    database="university",
    )
    
    mycursor = mydb.cursor()
    
    mycursor.execute('select * from section;')
    
    data = '<table style="width:400px">'
    for (course_id,sec_id,semester,year,building,room,capacity) in mycursor:
        r= ('<tr>'+ \
            '<th>' + course_id+'</th>'+\
            '<th>' + str(sec_id) + '</th>'+\
            '<th>' + str(semester) + '</th>'+\
            '<th>' + str(year) + '</th>'+\
            '<th>' + building + '</th>'+\
            '<th>' + str(room) + '</th>'+\
            '<th>' + str(capacity) + '</th>'+\
            '</tr>')
        data += r
    data += '</table>'
    mycursor.close()
    mydb.close()
    return HttpResponse(data)
def instructor(request):
    mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="Snaildog13!",
    auth_plugin='mysql_native_password',
    database="university",
    )
    
    mycursor = mydb.cursor()
    
    mycursor.execute('select * from instructor;')
    
    data = '<table style="width:400px">'
    for (id,name,dept,salary) in mycursor:
        r= ('<tr>'+ \
            '<th>' + str(id)+'</th>'+\
            '<th>' + name + '</th>'+\
            '<th>' + dept + '</th>'+\
            '<th>' + str(salary) + '</th>'+\
            '</tr>')
        data += r
    data += '</table>'
    mycursor.close()
    mydb.close()
    return HttpResponse(data)
def administrator(request):
    mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="Snaildog13!",  #USE YOUR PASSWORD
    auth_plugin='mysql_native_password',
    database="university",
    )
    
    mycursor = mydb.cursor()
    
    mycursor.execute('select * from department;')
    
    data = '<table style="width:400px">'
    for (dept_name,building, budget) in mycursor:
        r= ('<tr>'+ \
            '<th>' + dept_name + '</th>'+\
            '<th>' + building + '</th>'+\
            '<th>' + str(budget) + '</th>'+\
            '</tr>')
        data += r
    data += '</table>'
    mycursor.close()
    mydb.close()
    return HttpResponse(data)