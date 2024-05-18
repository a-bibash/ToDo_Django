from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('delete_Task/<int:id>/', views.delete_Task, name="delete_Task",),
    path('update_Task/<int:id>/', views.update_Task, name="update_Task",),


]
