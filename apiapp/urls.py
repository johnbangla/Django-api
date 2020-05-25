from django.urls import path
from . import views



urlpatterns = [
    path('',views.apiOverview,name="apiOverviews"),
    path('task-list',views.taskList,name="task-list"),
    path('details/<str:pk>/',views.taskDetail,name="task-detail"),
    path('task-create/',views.createRecord,name="taskpcreate"),
    path('task-update/<str:pk>/',views.updateRecord,name="taskupdate"),
    path('task-delete/<str:pk>/',views.deleteRecord,name="taskdelete")
]