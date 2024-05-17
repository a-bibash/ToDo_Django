from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('delete_Task/<int:id>/', views.delete_Task, name="delete_Task",),


]
