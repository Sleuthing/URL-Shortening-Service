from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import URL
from .serializer import URLSerializer, URLSerializerRestricted
from django.shortcuts import render, redirect

# Create your views here.
@api_view(['GET'])
def get_url(request):
    urls = URL.objects.all()
    serializer = URLSerializer(urls, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def create_url(request):
    serialized = URLSerializerRestricted(data=request.data)
    if serialized.is_valid():
        serialized.save()
        return Response(serialized.data, status=status.HTTP_201_CREATED)
    return Response(serialized.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def url_detail(request, pk=None, shortCode=None):
    try:
        if pk is not None:
            url = URL.objects.get(pk=pk)
        else:
            url = URL.objects.get(shortCode=shortCode)
    except URL.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = URLSerializerRestricted(url)
        return Response(serializer.data)
    
    elif request.method == 'PUT':
        serializer = URLSerializerRestricted(url, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        url.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET', 'PUT', 'DELETE'])  
def redirect_url(request, short_code):
    try:
        url = URL.objects.get(shortCode=short_code)
        url.accessCount += 1
        url.save()
        serializer = URLSerializerRestricted(url)
        return Response(serializer.data)
        #return redirect(url.url)
    except URL.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
@api_view(['GET'])  
def stats_url(request, shortCode):
    try:
        url = URL.objects.get(shortCode=shortCode)
        serializer = URLSerializer(url)
        return Response(serializer.data)
    except URL.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    

        