from django.http import JsonResponse


def get(request):

    dic = {"username": '22'}

    return JsonResponse(dic)
