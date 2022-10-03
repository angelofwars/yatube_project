from django.urls import path

from . import views

urlpatterns = [
    # Главная страница
    path('', views.index),
    path('posts', views.posts_list()),
    path(
        'group_posts/<slug:any slug>/',
        views.group_posts_detail()
    ),
    path('group_posts/', views.group_posts_list(),
    ]