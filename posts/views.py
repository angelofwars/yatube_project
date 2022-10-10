from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, 'posts/index.html')


def posts_list(request):
    template = 'posts/group_list.html'
    return render(request, template)


def group_posts_list(request, slug) :
    return render(request, 'posts/group_list.html')


# В урл мы ждем парметр, и нужно его прередать в функцию для использования
def group_posts_detail(request, slug):
    return HttpResponse(f'Группа постов {slug}')


