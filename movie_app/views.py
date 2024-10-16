from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from movie_app.models import Director, Movie, Review
from .serializers import DirectorSerializer, MovieSerializer, ReviewSerializer, MovieValidateSerializer, DirectorValidateSerializer, ReviewValidateSerializer # , DirectorValidateSerializer, MovieValidateSerializer, ReviewValidateSerializer
from rest_framework.response import Response
from rest_framework import status
from django.db.migrations import serializer
from rest_framework.permissions import IsAuthenticated


@api_view(http_method_names=["GET", "POST"])
@permission_classes([IsAuthenticated])
def director_list_create_api_view(request):
    # print(request.user)
    if request.method == 'GET':
        directors = Director.objects.all()
        return Response(data=DirectorSerializer(directors, many=True).data, status=status.HTTP_200_OK)

    elif request.method == 'POST':
        serializer = DirectorValidateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)
        return Response(data =serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(http_method_names=['GET', 'PUT', 'DELETE'])
def director_detail_api_view(request, id):
    try:
        director = Director.objects.get(id=id)
    except Director.DoesNotExist:
        return Response(data={'error': 'Page not found'}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        return Response(data=DirectorSerializer(instance=director).data)

    elif request.method == 'PUT':
        serializer = MovieValidateSerializer(instance=director, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_200_OK)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        director.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(http_method_names=['GET', 'POST'])
def movies_list_create_api_view(request):
    if request.method == 'GET':
        movies = Movie.objects.all()
        return Response(data=MovieSerializer(movies, many=True).data, status=status.HTTP_200_OK)

    elif request.method == 'POST':
        serializer = MovieValidateSerializer(data=request.data)
        if serializer.is_valid():
            Movie.objects.create(**serializer.validated_data)

            return Response(data=serializer.data, status=status.HTTP_201_CREATED)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(http_method_names=['GET', 'PUT', 'DELETE'])
def movies_detail_api_view(request, id):
    try:
        movie = Movie.objects.get(id=id)
    except Movie.DoesNotExist:
        return Response(data={'error': 'Page not found'}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        return Response(data=MovieSerializer(instance=movie).data)

    elif request.method == 'PUT':
        serializer = MovieValidateSerializer(instance=movie, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_200_OK)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        movie.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(http_method_names=['GET', 'POST'])
def reviews_list_create_api_view(request):
    if request.method == 'GET':
        reviews = Review.objects.all()
        return Response(data=ReviewSerializer(reviews, many=True).data, status=status.HTTP_200_OK)

    elif request.method == 'POST':
        serializer = ReviewValidateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(http_method_names=['GET', 'PUT', 'DELETE'])
def reviews_detail_api_view(request, id):
    try:
        review = Review.objects.get(id=id)
    except Review.DoesNotExist:
        return Response(data={'error': 'Page not found'}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        return Response(data=ReviewSerializer(instance=review).data)

    elif request.method == 'PUT':
        serializer = ReviewValidateSerializer(instance=review, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_200_OK)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        review.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# Optional root API view
# @api_view(http_method_names=['GET'])
# def api_root(request):
#     return Response({
#         'Admin': '/admin/',
#         'Directors': '/api/v1/director/',
#         'Movies': '/api/v1/movies/',
#         'Reviews': '/api/v1/reviews/',
#     })
