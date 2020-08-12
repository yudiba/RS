from django.http import JsonResponse
from . import rs
import json
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def get(request):

    postBody = request.body
    json_result = json.loads(postBody)

    username = json_result['username']

    host = "localhost"
    port = 3306
    user = 'root'
    password = 'root'
    db = 'data'
    charset = 'utf8'
    table_data = 'data'
    table_item = 'item'
    num = 10
    table = 'rs'

    if request.method == 'POST':

        result_rs = rs.rs(host, port, user, password, db, charset, table_data, table_item, username, num, table)

        dic = {}
        dic['userid'] = username
        dic['result'] = result_rs
        print(dic)
        return JsonResponse(dic)
