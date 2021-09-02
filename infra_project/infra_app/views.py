from django.http import HttpResponse


def index(request):
    return HttpResponse(content='У меня получилось!', status=200)


def second_page(request):
    return HttpResponse(content='А это вторая страница!', status=200)
