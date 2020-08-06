from django.http import JsonResponse
from . import rs
import requests
import ast


def get(request):

    url = 'http://127.0.0.1:8000/username/'
    res = requests.get(url)
    res = res.text
    res = ast.literal_eval(res)

    host = "localhost"
    port = 3306
    user = 'root'
    password = 'root'
    db = 'data'
    charset = 'utf8'
    table_data = 'data'
    table_item = 'item'
    username = res['username']
    num = 10
    table = 'rs'

    result_rs = rs.rs(host, port, user, password, db, charset, table_data, table_item, username, num, table)

    dic = {}
    dic['userid'] = username
    dic['result'] = result_rs

    return JsonResponse(dic)
