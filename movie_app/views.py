from django.shortcuts import render
from rest_framework.decorators import api_view
from movie_app.models import Director, Movie, Review
from .serializers import DirectorSerializer, MovieSerializer, ReviewSerializer
from rest_framework import serializers
from rest_framework.response import Response
from rest_framework import status

@api_view(http_method_names=["GET"])
def director_list_api_view(request):
    moview_app = Director.objects.all()
    list_ = DirectorSerializer(instance = moview_app, many = True).data

    directors = Director.objects.all()
    # Добавляем количество фильмов для каждого режиссера
    for director_data in list_:
        director = Director.objects.get(id=director_data['id'])
        director_data['movies_count'] = director.movies.count()
    return Response(data = list_, status = status.HTTP_200_OK)

@api_view(http_method_names=['GET'])
def director_detail_api_view(request, id):
    try:
        director = Director.objects.get(id=id)
    except Director.DoesNotExist:
        return Response(data={'error': 'Page not found'}, status=status.HTTP_404_NOT_FOUND)
    data = DirectorSerializer(instance=director, many=False).data
    return Response(data=data)




@api_view(http_method_names=['GET'])
def movies_list_api_view(request):
     movies = Movie.objects.all()
     data = MovieSerializer(instance=movies, many=True).data
     return Response(data=data)

@api_view(http_method_names=['GET'])
def movies_detail_api_view(request, id):
    try:
        movies = Movie.objects.get(id=id)
    except Movie.DoesNotExist:
        return Response(data={'error': 'Page not found'}, status=status.HTTP_404_NOT_FOUND)
    data = MovieSerializer(instance=movies, many=False).data
    return Response(data=data)


@api_view(http_method_names=['GET'])
def reviews_list_api_view(request):
     reviews = Review.objects.all()
     data = ReviewSerializer(instance=reviews, many=True).data
     return Response(data=data)

@api_view(http_method_names=['GET'])
def reviews_detail_api_view(request, id):
    try:
        reviews = Review.objects.get(id=id)
    except Review.DoesNotExist:
        return Response(data={'error': 'Page not found'}, status=status.HTTP_404_NOT_FOUND)
    data = ReviewSerializer(instance=reviews, many=False).data
    return Response(data=data)



