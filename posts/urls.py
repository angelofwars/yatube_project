# posts/urls.py
from django.urls import path
from . import views

app_name = 'posts'

urlpatterns = [
    path('', views.index, name='post_detail'),
    path('posts', views.posts_list,
         name='posts_list'),
    path(
        'group/<slug:slug>/',
        views.group_posts_detail,
        name='group_list'
    ),
]
