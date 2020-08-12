from django.http import JsonResponse, HttpResponse
import pymysql
import pymysql.cursors
import json
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def save(request):

    postBody = request.body
    json_result = json.loads(postBody)

    username = json_result['user']
    movieid = json_result['movieid']

    host = "localhost"
    port = 3306
    user = 'root'
    password = 'root'
    db = 'data'
    charset = 'utf8'
    table = 'data_new'

    dbconn = pymysql.connect(host=host, port=port, user=user, password=password, db=db, charset=charset)
    cursor = pymysql.cursors.SSCursor(dbconn)

    if request.method == 'POST':

        rating = json_result['rating']
        dic = {'user': username, 'movieid': movieid, 'rating': rating}
        sql_find = "select * from data_new where user=%s and movieid=%s" % (username, movieid)
        cursor.execute(sql_find)
        results = cursor.fetchall()
        s = len(results)

        if s == 0:
            print("插入数据")
            keys = ','.join(dic.keys())
            values = ','.join(['%s'] * len(dic))
            sql_insert = 'INSERT INTO {table}({keys}) VALUES ({values})'.format(table=table, keys=keys, values=values)
            cursor.execute(sql_insert, tuple(dic.values()))
            dbconn.commit()
            dbconn.close()
            return JsonResponse(dic)
        else:
            sql_update = "update data_new set rating=%s where user=%s and movieid=%s" % (rating, username, movieid)
            cursor.execute(sql_update)
            dbconn.commit()
            dbconn.close()
            print("已修改")
            return JsonResponse(dic)

    elif request.method == 'DELETE':
        sql_delete = "delete from data_new where user=%s and movieid=%s" % (username, movieid)
        cursor.execute(sql_delete)
        dbconn.commit()
        dbconn.close()
        print("删除数据")
        return JsonResponse(json_result)

    elif request.method == 'GET':
        sql_find1 = "select * from data_new where user=%s and movieid=%s" % (username, movieid)
        cursor.execute(sql_find1)
        result = cursor.fetchall()
        if len(result) > 0:
            for row in result:
                (a, b, c) = [str(row[0]), str(row[1]), str(row[2])]
                json_result1 = {'user': a, 'movieid': b, 'rating': c}
            dbconn.close()
            print("查询数据")
            return JsonResponse(json_result1)
        else:
            return HttpResponse("不存在")

    else:
        pass
