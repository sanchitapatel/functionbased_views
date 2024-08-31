from django.shortcuts import render

# Create your views here.
# Create your views here.
from app.models import Movie 
from app.serializers import MovieSerializer 
from rest_framework.decorators import api_view 
from rest_framework.response import Response 
from rest_framework import status

@api_view(['GET', 'POST'])  
def movie_list(request): 
    if request.method=='GET':
        movies = Movie.objects.all() 
        serializer=MovieSerializer(movies,many=True)
        return Response(serializer.data) 
    
    elif request.method=='POST':
        serializer=MovieSerializer(data=request.data) 
        if serializer.is_valid(): 
            serializer.save() 
            return Response(serializer.data) 
        else: return Response(serializer.errors)

@api_view(['GET', 'PUT','DELETE']) 
def movie_details(request,pk):
    id = Movie.objects.filter(pk=pk)
    if id:
        if request.method=='GET': 
            movie=Movie.objects.get(pk=pk) 
            serializer = MovieSerializer(movie) 
            return Response(serializer.data) 
        
        elif request.method=='PUT': 
            movie=Movie.objects.get(pk=pk) 
            serializer = MovieSerializer(movie,data=request.data,partial=True) 
            if serializer.is_valid(): 
                serializer.save() 
                return Response(serializer.data) 
            else: return Response(serializer.errors) 
        
        elif request.method=='DELETE': 
                movie=Movie.objects.get(pk=pk) 
                movie.delete() 
                return Response({'msg':"data deleted Successfully"}, status=status.HTTP_204_NO_CONTENT)
    else:
        res = {'msg': 'Id Not Present In Database'}
        return Response(res)
     
