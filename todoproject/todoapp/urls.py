from . import views
from django.urls import path
app_name = 'todoapp'
urlpatterns = [
    path('', views.home, name='home'),
    path('delete/<int:taskid>/', views.delete, name='delete'),
    path('update/<int:id>/', views.update, name='update'),
    path('cbvhome/', views.TaskListView.as_view(), name='cbvhome'),
    path('cbvdetails/<int:pk>/', views.TaskDetailView.as_view(), name='cbvdetails'),
    path('cbvupdate/<int:pk>/', views.TaskUpdateView.as_view(), name='cbvupdate'),
    path('cbvdelete/<int:pk>/', views.TaskDeleteView.as_view(), name='cbvdelete')
]