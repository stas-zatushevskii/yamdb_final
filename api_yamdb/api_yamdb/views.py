from django.http import HttpResponse


def index(request):
    return HttpResponse('Всё работает, поверь мне на слово')
