from django.apps import AppConfig


class IceCreamConfig(AppConfig):
    name = 'ice_cream'
    verbose_name: str = 'Управеление сортами мороженого'


class PostIceCream():
    name = 'post'
    
