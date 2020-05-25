from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serilizers import TaskSerilizers
from .models import Task
# Create your views here.

@api_view(['GET'])
def apiOverview(request):
    api_urls = {
        'List' : '/task-list/',
        'Details' : '/details/<str : pk>/',
        'Create' : '/task-create/',
        'Update' : '/task-update/<str : pk>/',
        'Delete' : '/task-delete/<str: pk>/',



    }
    return Response(api_urls)
    
@api_view(['GET'])
def taskList(request) :
    tasks = Task.objects.all()
    serializer = TaskSerilizers(tasks,many=True) 
    return Response(serializer.data)

@api_view(['GET'])
def taskDetail(request,pk):
    task = Task.objects.get(id=pk)
    serializer = TaskSerilizers(task,many=False)
    return Response(serializer.data)

@api_view(['POST'])
def createRecord(request):
   
    serializer = TaskSerilizers(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['POST'])
def updateRecord(request,pk):
    task = Task.objects.get(id=pk)
    serializer = TaskSerilizers(instance=task,data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)    


@api_view(['DELETE'])
def deleteRecord(request,pk):
    task = Task.objects.get(id=pk)
    task.delete()
    return Response('I am successfully deleted')   
