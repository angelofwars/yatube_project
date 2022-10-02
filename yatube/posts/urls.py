from django.urls import path

from . import views


urlpatterns = [
    # Главная страница
    path('', views.index),
    path(
        'group_posts/<slug:slug>/',
        views.ice_cream_detail
    ),
]