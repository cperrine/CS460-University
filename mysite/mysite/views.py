from django.http import HttpResponse, HttpResponseRedirect
import mysql.connector
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

my_passward = "" #put your passward here

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
    return HttpResponse(form)

@csrf_exempt
def student(request):
    try:
        department = request.POST['department']
        year = request.POST['year']
        semester = request.POST['semester']
    except:
        data='<!DOCTYPE html>' +\
            '<html>' +\
            '<body>' +\
            '<h1>Student Form:</h1>'+\
            '<form action="" method="post">' +\
                '<label for="department">department: </label>' +\
                '<input type="text" id="department" name="department"><br><br>' +\
                '<label for="year">year: </label>' +\
                '<input type="text" id="year" name="year"><br><br>' +\
                '<label for="semester">semester: </label>' +\
                '<input type="text" id="semester" name="semester"><br><br>' +\
                '<input type="submit" value="Submit">' +\
            '</form>' +\
            '</body>/' +\
            '</html>'
    else:
        mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd=my_passward,
        auth_plugin='mysql_native_password',
        database="university",
        )
        mycursor = mydb.cursor()
        
        mycursor.execute(f'select section.course_id, course.title, course.credits, section.building, section.room, section.capacity  from course inner join section on course.course_id = section.course_id where dept_name = "{department}" and semester = {semester} and year = {year} group by section.course_id;')
        
        data = '<p>courseID, Title, Credits, Building, Room, Capacity' +\
                '<table style="width:400px">'
        for (course_id,title,credits,building,room,capacity) in mycursor:
            r= ('<tr>'+ \
                '<th>' + course_id+'</th>'+\
                '<th>' + title + '</th>'+\
                '<th>' + str(credits) + '</th>'+\
                '<th>' + building + '</th>'+\
                '<th>' + str(room) + '</th>'+\
                '<th>' + str(capacity) + '</th>'+\
                '</tr>')
            data += r
        data += '</table>'
        mycursor.close()
        mydb.close()
    return HttpResponse(data)
    
@csrf_exempt
def instructor(request):
    mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd=my_passward,
    auth_plugin='mysql_native_password',
    database="university",
    )
    
    mycursor = mydb.cursor()
    
    try:
        sal= request.POST['amount']
    except:
        sal=0

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
    passwd=my_passward,
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
