from django.urls import path

from . import views

urlpatterns = [
    path('createModel', views.createModel, name='createModel'),
]