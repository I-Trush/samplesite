# from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

from .models import Bb


def index(request):
    # return HttpResponse("здесь будет выведен список объявлений")
    s = 'Список объявлений\r\n\r\n\r\n'
    for bb in Bb.objects.order_by('-published'):  # '-' означает в обратном порядке
        s += str(bb.pk) + '\r\n' + bb.title + '\r\n' + bb.content + '\r\n\r\n'
    return HttpResponse(s, content_type='text/plain; charset=utf-8')  # content_type без этого параметра веб-обозреватель посчитает текст HTML кодом
