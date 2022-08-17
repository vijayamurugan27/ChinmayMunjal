from django.urls import path
from . import views



urlpatterns = [
    path('', views.apiOverview, name='apiOverview'),
    path('tasklist', views.tasklist, name='tasklist'),
    path('taskdetail/<str:pk>', views.taskdetail, name='taskdetail'),
    path('taskcreate', views.taskcreate, name='taskcreate'),
    path('taskupdate/<str:pk>', views.taskupdate, name='taskupdate'),
    path('taskdelete/<str:pk>', views.taskdelete, name='taskdelete'),

]