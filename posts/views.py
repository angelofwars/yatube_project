from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    template = "posts/index.html"
    title = "Это главная страница проекта Yatube"
    context = {
        "title": title
    }
    return render(request, template, context)


def posts_list(request, slug):
    template = 'posts/group_list.html'
    return render(request, template)



# В урл мы ждем парметр, и нужно его прередать в функцию для использования
def group_posts_detail(request, slug):
    template = 'posts/group_list.html'
    posts = "Здесь будет информация о группах проекта Yatube"
    context = {
        "posts": posts
    }
    return render(request, template, context)


