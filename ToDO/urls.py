from django.urls import path
from . import views

urlpatterns = [
    path('app/', views.app, name="app"),
    path('delete_Task/<int:id>/', views.delete_Task, name="delete_Task",),
    path('update_Task/<int:id>/', views.update_Task, name="update_Task",),
    path('register/', views.register, name="register",),
    path('', views.login, name="login"),


]
