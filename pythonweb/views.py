from django.http import HttpResponse
from django.shortcuts import render
from django.db import connection

def dictfetchall(cursor):
    "Return all rows from a cursor as a dict"
    columns = [col[0] for col in cursor.description]
    return [
        dict(zip(columns, row))
        for row in cursor.fetchall()
    ]

def dictfetchone(cur):
    seq = cur.fetchone()
    if seq == None:
        return seq
    result = {}
    colnum = 0
    for column in cur.description:
        result[column[0]] = seq[colnum]
        colnum += 1
    return result
    #response.write(result['username'])

def query(query):
    cursor = connection.cursor()
    cursor.execute(query)
    ret = dictfetchall(cursor)
    cursor.close()
    return ret

def about(request):
    "Return all rows from a cursor as a dict"
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM users")
    # row = cursor.fetchone()
    result = dictfetchall(cursor)
    response = HttpResponse()
    for item in result:
        response.write(item.get('username')+'<br/>')
        # for k, v in item.items():
        #     if(k=='username'):
        #         response.writelines (str(v)+'<br/>')
    #response.write(result['username'])
    return response
    
    # return HttpResponse(result[0].email)
    #return render(request,'about.html')
    # return render(request, 'tracdb/bouncing_tickets.html', {
    #     'tickets': tickets,
    # })

def home(request):
    #return HttpResponse('home')
    return render(request,'home.html')