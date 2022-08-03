# from django.shortcuts import render

# Create your views here.

# #from django.http import HttpResponse
# #from django.template import loader

from django.shortcuts import render

from .models import Bb
from .models import Rubric


def index(request):
    # return HttpResponse("здесь будет выведен список объявлений")

    # #s = 'Список объявлений\r\n\r\n\r\n'
    # #for bb in Bb.objects.order_by('-published'):  # '-' означает в обратном порядке
    # #   s += str(bb.pk) + '\r\n' + bb.title + '\r\n' + bb.content + '\r\n\r\n'
    # #return HttpResponse(s, content_type='text/plain; charset=utf-8')  # content_type без этого параметра веб-обозреватель посчитает текст HTML кодом

    # ##template = loader.get_template('bboard/index.html')     #get_template загружает шаблон; параметр = путь
    # ##bbs = Bb.objects.order_by('-published')
    # ##context = {'bbs':bbs}
    # ##return  HttpResponse(template.render(context, request))

    bbs = Bb.objects.all()
    rubrics = Rubric.objects.all()
    context = {'bbs':bbs, 'rubrics':rubrics}                # набор параметров для вывода в шаблон index.html
    return render(request, 'bboard/index.html', context)


def by_rubric(request, rubric_id):
    bbs = Bb.objects.filter(rubric=rubric_id)
    rubrics = Rubric.objects.all()
    current_rubric = Rubric.objects.get(pk=rubric_id)
    context = {'bbs':bbs, 'rubrics':rubrics, 'current_rubric':current_rubric}
    return render(request, 'bboard/by_rubric.html', context)

