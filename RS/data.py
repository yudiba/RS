from django.http import JsonResponse


def get(request):

    dic = {"user": 19, "movieid": 45, "rating": 4}

    return JsonResponse(dic)
