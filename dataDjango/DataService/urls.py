from django.urls import path

from . import views

urlpatterns = [
    path('createModel', views.createModel, name='createModel'),
    path('deleteModel/<int:tid>/', views.deleteModel, name='deleteModel'),
]