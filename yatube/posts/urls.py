from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='post_detail'),
    path(
        'group/<slug:slug>/',
        views.group_posts_detail,
        name='group_list'
    ),
]