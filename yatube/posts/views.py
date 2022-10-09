from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    template = 'posts/index.html'
    return render(request, template)


def posts_list(request):
    return HttpResponse('Список постов')


def group_posts_list(request):
    return HttpResponse('Список групп')


# В урл мы ждем парметр, и нужно его прередать в функцию для использования
def group_posts_detail(request, slug):
    return HttpResponse(f'Группа постов {slug}')
