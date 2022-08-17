from django.shortcuts import render

from django.http import JsonResponse


from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Task
from .serializers import TaskSerializer

@api_view(['GET'])
def apiOverview(requst):
    api_urls = {
        'Create':'/taskcreate',
        'List':'/tasklist',        
        'Detail view':'/taskdetail/<str:pk>',        
        'Update':'/taskupdate/<str:pk>',
        'Delete':'/taskdalete/<str:pk>',
        }
    # return Response("API BASE POINT ", safe=False)
    return Response(api_urls)


@api_view(['GET'])
def tasklist(request):
    tasks = Task.objects.all()
    serializer = TaskSerializer(tasks, many = True)
    return Response(serializer.data)


@api_view(['GET'])
def taskdetail(request, pk):
    tasks = Task.objects.get(id = pk)
    serializer = TaskSerializer(tasks, many = False)
    return Response(serializer.data)

@api_view(['POST'])
def taskcreate(request):
    serializer = TaskSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()    
    return Response(serializer.data)


@api_view(['POST'])
def taskupdate(request, pk):
    task =Task.objects.get(id = pk)
    serializer = TaskSerializer(instance=task, data = request.data) #instead of creating a new data, 
    # we are passing over the existing data. 
    if serializer.is_valid():
        serializer.save()    
    return Response(serializer.data)


@api_view(['DELETE'])
def taskdelete(request, pk):
    task =Task.objects.get(id = pk)
    task.delete()    
    return Response("Item deleted Succesfully")