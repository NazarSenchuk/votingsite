from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('change_username', views.change_username , name = 'change_username')
]
