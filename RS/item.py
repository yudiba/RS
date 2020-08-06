from django.http import JsonResponse


def get(request):

    dic = {"itemid": 20, "title": 'Toy Story (2003)'}

    return JsonResponse(dic)
