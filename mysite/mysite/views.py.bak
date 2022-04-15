from django.http import HttpResponse, HttpResponseRedirect
import mysql.connector
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

my_passward = "" #put your passward here

def index(request):
    data='<!DOCTYPE html>' +\
    '<html>' +\
    '<body>' +\
    '<h1>Main Page:</h1>'+\
    '<form action="student/" method="post">' +\
        '<input type="submit" value="Student">' +\
    '</form>' +\
    '<form action="instructor/" method="post">' +\
        '<input type="submit" value="Instructor">' +\
    '</form>' +\
    '<form action="administrator_view/" method="post">' +\
        '<input type="submit" value="Admin">' +\
    '</form>' +\
    '</body>/' +\
    '</html>'
    return HttpResponse(data)

@csrf_exempt
def administrator_view(request):
    data='<!DOCTYPE html>' +\
    '<html>' +\
    '<body>' +\
    '<h1>Administrator View:</h1>'+\
    '<form action="administrator_f1/" method="post">' +\
        '<input type="submit" value="List of Professors">' +\
    '</form>' +\
    '<form action="administrator_f2/" method="post">' +\
        '<input type="submit" value="Average Salaries">' +\
    '</form>' +\
    '<form action="administrator_f3/" method="post">' +\
        '<input type="submit" value="Number of Students Taught">' +\
    '</form>' +\
    '</body>/' +\
    '</html>'
    return HttpResponse(data)

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
        
        mycursor.execute(f'select section.course_id, section.sec_id, course.title, course.credits, section.building, section.room, section.capacity  from course inner join section on course.course_id = section.course_id where dept_name = "{department}" and semester = {semester} and year = {year};')
        
        data = '<table style="width:400px">'
        for (course_id, section_id, title,credits,building,room,capacity) in mycursor:
            r= ('<tr>'+ \
                '<th>Course: ' + course_id+'</th>'+\
                '<th>Section: ' + section_id+'</th>'+\
                '<th>Title: ' + title + '</th>'+\
                '<th>Credits: ' + str(credits) + '</th>'+\
                '<th>Building: ' + building + '</th>'+\
                '<th>Room: ' + str(room) + '</th>'+\
                '<th>Capacity: ' + str(capacity) + '</th>'+\
                '</tr>')
            data += r
        data += '</table>'
        mycursor.close()
        mydb.close()
    return HttpResponse(data)
    
@csrf_exempt
def instructor(request):
    try:
        #instructor_name = request.POST['instructor_name']
        instructor_id = request.POST['instructor_id']
        semester = request.POST['semester']
        year = request.POST['year']
    except:
        data='<!DOCTYPE html>' +\
            '<html>' +\
            '<body>' +\
            '<h1>Instructor Form:</h1>'+\
            '<form action="" method="post">' +\
                '<label for="instructor_name">Instructor Name: </label>' +\
                '<input type="text" id="instructor_name" name="instructor_name"><br><br>' +\
                '<label for="instructor_id">Instructor ID: </label>' +\
                '<input type="text" id="instructor_id" name="instructor_id"><br><br>' +\
                '<label for="semester">Semester: </label>' +\
                '<input type="text" id="semester" name="semester"><br><br>' +\
                '<label for="year">Year: </label>' +\
                '<input type="text" id="year" name="year"><br><br>' +\
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

        query=f'select t1.course_id, t1.sec_id, t1.building, t1.room, t1.capacity, count(grade) as students from (select s.course_id, s.sec_id, s.semester, s.year, s.building, s.room, s.capacity from section s inner join teaches t on s.course_id = t.course_id and s.sec_id = t.sec_id and s.semester = t.semester and s.year = t.year where t.id = {instructor_id} and t.semester = {semester} and t.year = {year}) as t1 left join takes t2 on t1.course_id = t2.course_id and t1.sec_id = t2.sec_id and t1.semester = t2.semester and t1.year = t2.year group by t1.course_id, t1.sec_id, t1.semester, t1.year;'
        mycursor.execute(query)
        
        data = '<table style="width:400px">'
        for (course_id,sec_id,building,room,capacity,students) in mycursor:
            r= ('<tr>'+ \
                '<th>Course:  ' + str(course_id) +'</th>'+\
                '<th>Section: ' + str(sec_id) + '</th>'+\
                '<th>Building: ' + building + '</th>'+\
                '<th>Room: ' + str(room) + '</th>'+\
                '<th>Capacity: ' + str(capacity) + '</th>'+\
                '<th>Students: ' + str(students) + '</th>'+\
                '</tr>')
            data += r
        data += '</table>'
        mycursor.close()
        mydb.close()

        data += f'<h1>Section Form:</h1>'+\
            '<form action="section" method="post">' +\
                '<label for="instructor_id">Instructor ID: </label>' +\
                '<input type="text" id="instructor_id" name="instructor_id" value="' + instructor_id + '"><br><br>' +\
                '<label for="semester">Semester: </label>' +\
                '<input type="text" id="semester" name="semester" value="' + semester + '"><br><br>' +\
                '<label for="year">Year: </label>' +\
                '<input type="text" id="year" name="year" value="' + year + '"><br><br>' +\
                '<label for="course_id">Course: </label>' +\
                '<input type="text" id="course_id" name="course_id"><br><br>' +\
                '<label for="sec_id">section: </label>' +\
                '<input type="text" id="sec_id" name="sec_id"><br><br>' +\
                '<input type="submit" value="Submit">' +\
            '</form>' +\
            '</body>/' +\
            '</html>'
    return HttpResponse(data)

@csrf_exempt
def section(request):
    try:
        instructor_id = request.POST['instructor_id']
        semester = request.POST['semester']
        year = request.POST['year']
        course_id = request.POST['course_id']
        sec_id = request.POST['sec_id']
    except:
        data = f'<h1>Section Form:</h1>'+\
            '<form action="section" method="post">' +\
                '<label for="instructor_id">Instructor ID: </label>' +\
                '<input type="text" id="instructor_id" name="instructor_id"><br><br>' +\
                '<label for="semester">Semester: </label>' +\
                '<input type="text" id="semester" name="semester"><br><br>' +\
                '<label for="year">Year: </label>' +\
                '<input type="text" id="year" name="year"><br><br>' +\
                '<label for="course_id">Course: </label>' +\
                '<input type="text" id="course_id" name="course_id"><br><br>' +\
                '<label for="sec_id">section: </label>' +\
                '<input type="text" id="sec_id" name="sec_id"><br><br>' +\
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

        query=f'select s.ID, s.name, s.dept_name, s.tot_cred from (select t1.course_id, t1.sec_id, t1.building, t1.room, t1.capacity, t2.ID from (select s.course_id, s.sec_id, s.semester, s.year, s.building, s.room, s.capacity from section s inner join teaches t on s.course_id = t.course_id and s.sec_id = t.sec_id and s.semester = t.semester and s.year = t.year where t.id = {instructor_id} and t.semester = {semester} and t.year = {year} and t.course_id = "{course_id}" and t.sec_id = {sec_id}) as t1 left join takes t2 on t1.course_id = t2.course_id and t1.sec_id = t2.sec_id and t1.semester = t2.semester and t1.year = t2.year) as t3 join student s on t3.ID = s.ID;'
        mycursor.execute(query)
        
        data = '<table style="width:400px">'
        for (id,name,dept_name,tot_cred) in mycursor:
            r= ('<tr>'+ \
                '<th>ID: ' + str(id) +'</th>'+\
                '<th>Name: ' + name + '</th>'+\
                '<th>Department: ' + dept_name + '</th>'+\
                '<th>Total Credits: ' + str(tot_cred) + '</th>'+\
                '</tr>')
            data += r
        data += '</table>'
        mycursor.close()
        mydb.close()
    return HttpResponse(data)
    
@csrf_exempt
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
            '<th>Min:' + str(min) + '</th>'+\
            '<th>Avg:' + str(avg) + '</th>'+\
            '<th>Max:' + str(max) + '</th>'+\
            '<th>Dept:' + dept + '</th>'+\
            '</tr>')
        data += r
    data += '</table>'
    mycursor.close()
    mydb.close()
    return HttpResponse(data)
    
@csrf_exempt    
def administrator_f1(request):
    try:
        ID = request.POST['ID']
        name = request.POST['name']
        dept = request.POST['dept']
        salary = request.POST['salary']
    except:
        data = f'<h1>Sort By:</h1>'+\
        '<form action="name/" method="post">' +\
        '<input type="submit" value="Name">' +\
        '</form>' +\
        '<form action="department/" method="post">' +\
        '<input type="submit" value="Department">' +\
        '</form>' +\
        '<form action="salary/" method="post">' +\
        '<input type="submit" value="Salary">' +\
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
        
        query = f'select ID, name, dept, salary from instructor order by name;'
        mycursor.execute(query)
        
        data += '<table style="width:400px">'
        for (ID, name, dept, salary) in mycursor:
            r = ( '<tr>'+\
                '<th>' + str(ID) + '</th>'+\
                '<th>' + name + '</th>'+\
                '<th>' + dept + '</th>'+\
                '<th>' + str(salary) + '</th>'+\
                '</tr>' )
            data += r
        data += '</table>'
        mycursor.close()
        mydb.close()
    return HttpResponse(data)
    
@csrf_exempt    
def f1name (request):

    mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd=my_passward,
    auth_plugin='mysql_native_password',
    database="university",
    )
    
    mycursor = mydb.cursor()
    
    query = 'select ID, name, dept, salary from instructor order by name;'
    mycursor.execute(query)
    data = ''    
    data += '<table style="width:400px">'
    for (ID, name, dept, salary) in mycursor:
            r = ( '<tr>'+\
                '<th>' + str(ID) + '</th>'+\
                '<th>' + name + '</th>'+\
                '<th>' + dept + '</th>'+\
                '<th>' + str(salary) + '</th>'+\
                '</tr>' )
            data += r
    data += '</table>'
    mycursor.close()
    mydb.close()
    return HttpResponse(data)
@csrf_exempt        
def f1department (request):

    mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd=my_passward,
    auth_plugin='mysql_native_password',
    database="university",
    )
    
    mycursor = mydb.cursor()
    
    query = 'select ID, name, dept, salary from instructor order by dept;'
    mycursor.execute(query)
    data = ''    
    data += '<table style="width:400px">'
    for (ID, name, dept, salary) in mycursor:
            r = ( '<tr>'+\
                '<th>' + str(ID) + '</th>'+\
                '<th>' + name + '</th>'+\
                '<th>' + dept + '</th>'+\
                '<th>' + str(salary) + '</th>'+\
                '</tr>' )
            data += r
    data += '</table>'
    mycursor.close()
    mydb.close()
    return HttpResponse(data)
@csrf_exempt        
def f1salary (request):

    mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd=my_passward,
    auth_plugin='mysql_native_password',
    database="university",
    )
    
    mycursor = mydb.cursor()
    
    query = 'select ID, name, dept, salary from instructor order by salary;'
    mycursor.execute(query)
    data = ''    
    data += '<table style="width:400px">'
    for (ID, name, dept, salary) in mycursor:
            r = ( '<tr>'+\
                '<th>' + str(ID) + '</th>'+\
                '<th>' + name + '</th>'+\
                '<th>' + dept + '</th>'+\
                '<th>' + str(salary) + '</th>'+\
                '</tr>' )
            data += r
    data += '</table>'
    mycursor.close()
    mydb.close()
    return HttpResponse(data)