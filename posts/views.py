from django.http import HttpResponse


def index(request):
    return HttpResponse('Главная страница')


def posts_list(request):
    return HttpResponse('Список постов')


def group_posts_list(request) :
    return HttpResponse('Список групп')


# В урл мы ждем парметр, и нужно его прередать в функцию для использования
def group_posts_detail(request, slug):
    return HttpResponse(f'Группа постов {slug}')


