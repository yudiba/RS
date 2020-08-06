from django.http import JsonResponse, HttpResponse
import requests
import ast
import pymysql
import pymysql.cursors


def save(request):

    url = 'http://127.0.0.1:8000/data/'
    res = requests.get(url)
    res = res.text
    res = ast.literal_eval(res)

    host = "localhost"
    port = 3306
    user = 'root'
    password = 'root'
    db = 'data'
    charset = 'utf8'
    username = res['user']
    movieid = res['movieid']
    rating = res['rating']
    table = 'data_new'

    dic = {'user': username, 'movieid': movieid, 'rating': rating}

    dbconn = pymysql.connect(host=host, port=port, user=user, password=password, db=db, charset=charset)
    cursor = pymysql.cursors.SSCursor(dbconn)
    sql = "select * from data_new where user=%s and movieid=%s" % (username, movieid)
    cursor.execute(sql)
    results = cursor.fetchall()
    s = len(results)

    if s == 0:
        print("插入数据")
        keys = ','.join(dic.keys())
        values = ','.join(['%s'] * len(dic))
        sql1 = 'INSERT INTO {table}({keys}) VALUES ({values})'.format(table=table, keys=keys, values=values)
        cursor.execute(sql1, tuple(dic.values()))
        dbconn.commit()
        dbconn.close()
        return JsonResponse(dic)
    else:
        sql2 = "update data_new set rating=%s where user=%s and movieid=%s" % (rating, username, movieid)
        cursor.execute(sql2)
        dbconn.commit()
        dbconn.close()
        print("已修改")
        return JsonResponse(dic)
