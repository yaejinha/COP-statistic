from django.urls import path

from . import views

urlpatterns = [
    path('createModel', views.createModel, name='createModel'),
    path('updateModel', views.updateModel, name='updateModel'),
    path('deleteModel/<int:tid>/', views.deleteModel, name='deleteModel'),
]