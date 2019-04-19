from django.urls import path
from . import views


app_name='movie'
urlpatterns = [
    path('', views.list, name='list'),
    path('<int:id>/',views.read, name='read'),
    path('<int:id>/delete/',views.delete, name='delete'),
    path('<int:id>/scores/new/',views.new_score, name='new_score'),
    path('<int:id>/scores/<int:idid>/delete/',views.delete_score, name='delete_score'),
    ]