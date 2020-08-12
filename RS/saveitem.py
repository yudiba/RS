from django.http import JsonResponse, HttpResponse
import pymysql
import pymysql.cursors
import json
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def save(request):

    postBody = request.body
    json_result = json.loads(postBody)

    username = json_result['itemid']

    host = "localhost"
    port = 3306
    user = 'root'
    password = 'root'
    db = 'data'
    charset = 'utf8'
    table = 'item_new1'

    dbconn = pymysql.connect(host=host, port=port, user=user, password=password, db=db, charset=charset)
    cursor = pymysql.cursors.SSCursor(dbconn)

    if request.method == 'POST':
        title = json_result['title']
        dic = {'itemid': username, 'title': title}
        sql_find = "select * from item_new1 where itemid=%s"
        args = {username}
        cursor.execute(sql_find, args)
        results = cursor.fetchall()
        s = len(results)
        if s == 0:
            keys = ','.join(dic.keys())
            values = ','.join(['%s'] * len(dic))
            sql_insert = 'INSERT INTO {table}({keys}) VALUES ({values})'.format(table=table, keys=keys, values=values)
            cursor.execute(sql_insert, tuple(dic.values()))
            dbconn.commit()
            dbconn.close()
            print("插入数据")
            return JsonResponse(dic)
        else:
            dbconn.close()
            return HttpResponse("已存在")

    elif request.method == 'DELETE':
        sql_delete = "delete from item_new1 where itemid=%s"
        args = {username}
        cursor.execute(sql_delete, args)
        dbconn.commit()
        dbconn.close()
        print("删除数据")
        return JsonResponse(json_result)

    elif request.method == 'GET':
        sql_find1 = "select * from item_new1 where itemid=%s"
        args = {username}
        cursor.execute(sql_find1, args)
        result = cursor.fetchall()
        for row in result:
            (a, b) = [str(row[0]), str(row[1])]
            json_result = {'itemid': a, 'title': b}
        dbconn.close()
        print("查询数据")
        return JsonResponse(json_result)

    else:
        pass

