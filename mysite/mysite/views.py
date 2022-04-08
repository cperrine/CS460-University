from django.http import HttpResponse
import mysql.connector
from django.shortcuts import render
#from django.views.decorators import csrf exempt



def index(request):
    form='<!DOCTYPE html>' +\
    '<html>' +\
    '<body>' +\
    '<h1>Display the name of instructors who earn more than:</h1>'+\
    '<form action="instructor/" method="post">' +\
        '<label for="amount">$</label>' +\
        '<input type="text" id="amount" name="amount"><br><br>' +\
        '<input type="submit" value="Submit">' +\
    '</form>' +\
    '</body>/' +\
    '</html>'
    return HttpResponse('Hello, this is the index page')
    
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
    
#@csrf_exempt
def instructor(request):
    mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="Snaildog13!",
    auth_plugin='mysql_native_password',
    database="university",
    )
    
    mycursor = mydb.cursor()
    
    sal= 80000
    query=f'SELECT * FROM instructor WHERE salary > {sal};'
    mycursor.execute(query)
    
    data = '<table style="width:400px">'
    for (id,name,dept,salary) in mycursor:
        r= ('<tr>'+ \
            '<th>' + str(id) +'</th>'+\
            '<th>' + name + '</th>'+\
            '<th>' + dept + '</th>'+\
            '<th>' + str(salary) + '</th>'+\
            '</tr>')
        data += r
    data += '</table>'
    mycursor.close()
    mydb.close()
    return HttpResponse(data)
def administrator_f2(request):
    mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="Snaildog13!",  #USE YOUR PASSWORD
    auth_plugin='mysql_native_password',
    database="university",
    )
    
    mycursor = mydb.cursor()
    
    query1 = 'select min(salary), avg(salary) , max(salary), dept from instructor group by dept;'
    mycursor.execute(query1)
    
    data = '<table style="width:400px">'
    for (min,avg, max, dept) in mycursor:
        r = ('<tr>'+\
            '<th>' + str(min) + '</th>'+\
            '<th>' + str(avg) + '</th>'+\
            '<th>' + str(max) + '</th>'+\
            '<th>' + dept + '</th>'+\
            '</tr>')
        data += r
    data += '</table>'
    mycursor.close()
    mydb.close()
    return HttpResponse(data)