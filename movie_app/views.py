from django.shortcuts import render
from rest_framework.decorators import api_view
from movie_app.models import Director, Movie, Review
from .serializers import DirectorSerializer, MovieSerializer, ReviewSerializer
from rest_framework import serializers
from rest_framework.response import Response
from rest_framework import status

@api_view(http_method_names=["GET", "POST"])
def director_list_create_api_view(request):
    if request.method == 'GET':
        movie_app = Director.objects.all()

        list_ = DirectorSerializer(instance=movie_app, many=True).data

        return Response(data=list_, status=status.HTTP_200_OK)



    #moview_app = Director.objects.all()
    #list_ = DirectorSerializer(instance = moview_app, many = True).data

    elif request.method == 'POST':
        name = request.data.get('name')
        category_id = request.data.get('category_id')
        print(name, category_id)

        director = Director.objects.all()
        print(director, category_id)

        return Response(data=DirectorSerializer(Director).data, status=status.HTTP_201_CREATED)


@api_view(http_method_names=['GET', 'PUT', 'DELETE'])
def director_detail_api_view(request, id):
    try:
        director = Director.objects.get(id=id)
    except Director.DoesNotExist:
        return Response(data={'error': 'Page not found'}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        data = DirectorSerializer(instance=director, many=False).data
        return Response(data=data)

    elif request.method == 'PUT':
        director.name = request.data.get('name')
        director.category_id = request.data.get('category_id')
        director.save()
        return Response(data=DirectorSerializer(director).data, status=status.HTTP_200_OK)

    elif request.method == 'DELETE':
        director.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)




@api_view(http_method_names=['GET', 'POST'])
def movies_list_create_api_view(request):

    if request.method == 'GET':
        movie_app = Movie.objects.all()

        data = MovieSerializer(instance=movie_app, many=True).data

        director = Movie.objects.all()




    elif request.method == 'POST':
        title = request.data.get('title')
        description = request.data.get('description')
        is_active = request.data.get('is_active')
        tags = request.data.get('tags')
        duration = request.data.get('duration')
        director = request.data.get('director')
        genre = request.data.get('genre')
        created = request.data.get('created')
        updated = request.data.get('updated')

        movies =Review.objects.create(
            title=title,
            description=description,
            is_active=is_active,
            tags=tags,
            duration=duration,
            director=director,
            genre=genre,
            created=created,
            updated=updated,
        )
        print(movies)
        return Response(data=movies, status=status.HTTP_201_CREATED)



@api_view(http_method_names=['GET', 'PUT', 'DELETE'])
def movies_detail_api_view(request, id):
    try:
        movies = Movie.objects.get(id=id, is_active=True)
    except Movie.DoesNotExist:
        return Response(data={'error': 'Page not found'}, status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        data = MovieSerializer(instance=movies, many=False).data
        return Response(data=data)

    elif request.method == 'PUT':
        Movie.title = request.data.get('title')
        Movie.description = request.data.get('description')
        Movie.is_active = request.data.get('is_active')
        Movie.tags = request.data.get('tags')
        Movie.duration = request.data.get('duration')
        Movie.director = request.data.get('director')
        Movie.genre = request.data.get('genre')
        Movie.created = request.data.get('created')
        Movie.updated = request.data.get('updated')
        movies.save()
        return Response(data=MovieSerializer(Movie).data, status=status.HTTP_201_CREATED)

    elif request.method == 'DELETE':
        movies.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)








@api_view(http_method_names=['GET', 'POST'])
def reviews_list_create_api_view(request):
    movie_app= Review.objects.all()
    data = ReviewSerializer(instance=movie_app, many=True).data

    if request.method == 'GET':
        movie_app = Review.objects.all(
            'text'
        ).prefetch_related(
            'movie',
            'stars'
        ).all()



        data = ReviewSerializer(instance=movie_app, many=True).data
        director = Director.objects.all()
        for director_data in data:
            director = Director.objects.get(id=director_data['id'])
            director_data['movies_c'] = director.movies.count()
        return Response(data=data, status=status.HTTP_200_OK)

    elif request.method == 'POST':
        text = request.data['text']
        movie = request.data['movie']

        director = request.data['director']
        stars = request.data['stars']
        print(text, movie, director, stars)
        review = Review.objects.create(
            text=text,
            movie=movie,
            director=director,
            stars=stars,
        )
        print(review)
        return Response(data=review, status=status.HTTP_201_CREATED)






@api_view(http_method_names=['GET', 'PUT', 'DELETE'])
def reviews_detail_api_view(request, id):
    try:
        reviews = Review.objects.get(id=id)
    except Review.DoesNotExist:
        return Response(data={'error': 'Page not found'}, status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        data = ReviewSerializer(instance=reviews, many=False).data
        return Response(data=data)
    elif request.method == 'PUT':
        Review.text = request.data['text']
        Review.movie = request.data['movie']
        Review.director = request.data['director']
        Review.stars = request.data['stars']
        Review.save()
        return Response(data=ReviewSerializer(Review).data, status=status.HTTP_201_CREATED)
    elif request.method == 'DELETE':
        Review.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)





