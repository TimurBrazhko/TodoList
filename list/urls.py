from django.urls import path
from list import views

urlpatterns = [
    path('task-list/', views.TaskAPIView.as_view(), name='task-list'),
    path('task-list/create/', views.TaskCreateAPIView.as_view(), name='task-list-create'),
    path('task-list/<int:id>/', views.TaskDetailAPIView.as_view(), name='task-detail'),

]
