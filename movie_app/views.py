from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from rest_framework.views import APIView
from movie_app.models import Director, Movie, Review, Category, SearchTag
from .serializers import DirectorSerializer, MovieSerializer, ReviewSerializer, MovieValidateSerializer, \
    DirectorValidateSerializer, ReviewValidateSerializer, CategorySerializer, SearchTagSerializer  # , DirectorValidateSerializer, MovieValidateSerializer, ReviewValidateSerializer
from rest_framework.response import Response
from rest_framework import status
from django.db.migrations import serializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import ListAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.pagination import PageNumberPagination
from rest_framework.viewsets import ModelViewSet


class SearchTagViewSet(ModelViewSet):
    queryset = SearchTag.objects.all()
    serializer_class = SearchTagSerializer
    lookup_field = 'id'
    pagination_class = PageNumberPagination


class CustomPagination(PageNumberPagination):
    def get_paginated_response(self, data):
        return Response({
            'total': self.page.paginator.count,
            'next': self.get_next_link(),
            'previous': self.get_previous_link(),
            'results': data,
        })

class CategoryListAPIView(ListCreateAPIView):
    queryset = Category.objects.all() #list of objects from DB
    serializer_class = CategorySerializer #serializer inherited by ModelSerializer
    # permission_classes= [IsAuthenticated]
    pagination_class = CustomPagination
    # def list(self, request, *args, **kwargs):
    #     queryset = self.filter_queryset(self.get_queryset())
    #
    #     page = self.paginate_queryset(queryset)
    #     if page is not None:
    #         serializer = self.get_serializer(page, many=True)
    #         return self.get_paginated_response(serializer.data)
    #
    #     serializer = self.get_serializer(queryset, many=True)
    #     return Response(serializer.data)


class CategoryDetailAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    lookup_field = 'id' #pk




class DirectorListCrateAPIView(ListCreateAPIView):
    queryset = (Director.objects.all())
    serializer_class = DirectorSerializer
    def post(self, request):
        serializer = DirectorValidateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class DirectorListCreateAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        directors = Director.objects.all()
        return Response(data=DirectorSerializer(directors, many=True).data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = DirectorValidateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class DirectorDetailAPIView(APIView):

    def get_object(self, id):
        try:
            return Director.objects.get(id=id)
        except Director.DoesNotExist:
            return None

    def get(self, request, id):
        director = self.get_object(id)
        if director is None:
            return Response(data={'error': 'Page not found'}, status=status.HTTP_404_NOT_FOUND)
        return Response(data=DirectorSerializer(instance=director).data)

    def put(self, request, id):
        director = self.get_object(id)
        if director is None:
            return Response(data={'error': 'Page not found'}, status=status.HTTP_404_NOT_FOUND)
        serializer = DirectorValidateSerializer(instance=director, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_200_OK)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        director = self.get_object(id)
        if director is None:
            return Response(data={'error': 'Page not found'}, status=status.HTTP_404_NOT_FOUND)
        director.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class MovieListCreateAPIView(APIView):

    def get(self, request):
        movies = Movie.objects.all()
        return Response(data=MovieSerializer(movies, many=True).data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = MovieValidateSerializer(data=request.data)
        if serializer.is_valid():
            Movie.objects.create(**serializer.validated_data)
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class MovieDetailAPIView(APIView):

    def get_object(self, id):
        try:
            return Movie.objects.get(id=id)
        except Movie.DoesNotExist:
            return None

    def get(self, request, id):
        movie = self.get_object(id)
        if movie is None:
            return Response(data={'error': 'Page not found'}, status=status.HTTP_404_NOT_FOUND)
        return Response(data=MovieSerializer(instance=movie).data)

    def put(self, request, id):
        movie = self.get_object(id)
        if movie is None:
            return Response(data={'error': 'Page not found'}, status=status.HTTP_404_NOT_FOUND)
        serializer = MovieValidateSerializer(instance=movie, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_200_OK)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        movie = self.get_object(id)
        if movie is None:
            return Response(data={'error': 'Page not found'}, status=status.HTTP_404_NOT_FOUND)
        movie.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class ReviewListCreateAPIView(APIView):

    def get(self, request):
        reviews = Review.objects.all()
        return Response(data=ReviewSerializer(reviews, many=True).data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = ReviewValidateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ReviewDetailAPIView(APIView):

    def get_object(self, id):
        try:
            return Review.objects.get(id=id)
        except Review.DoesNotExist:
            return None

    def get(self, request, id):
        review = self.get_object(id)
        if review is None:
            return Response(data={'error': 'Page not found'}, status=status.HTTP_404_NOT_FOUND)
        return Response(data=ReviewSerializer(instance=review).data)

    def put(self, request, id):
        review = self.get_object(id)
        if review is None:
            return Response(data={'error': 'Page not found'}, status=status.HTTP_404_NOT_FOUND)
        serializer = ReviewValidateSerializer(instance=review, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_200_OK)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        review = self.get_object(id)
        if review is None:
            return Response(data={'error': 'Page not found'}, status=status.HTTP_404_NOT_FOUND)
        review.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
# @api_view(http_method_names=["GET", "POST"])
# @permission_classes([IsAuthenticated])
# def director_list_create_api_view(request):
#     # print(request.user)
#     if request.method == 'GET':
#         directors = Director.objects.all()
#         return Response(data=DirectorSerializer(directors, many=True).data, status=status.HTTP_200_OK)
#
#     elif request.method == 'POST':
#         serializer = DirectorValidateSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(data=serializer.data, status=status.HTTP_201_CREATED)
#         return Response(data =serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
# @api_view(http_method_names=['GET', 'PUT', 'DELETE'])
# def director_detail_api_view(request, id):
#     try:
#         director = Director.objects.get(id=id)
#     except Director.DoesNotExist:
#         return Response(data={'error': 'Page not found'}, status=status.HTTP_404_NOT_FOUND)
#
#     if request.method == 'GET':
#         return Response(data=DirectorSerializer(instance=director).data)
#
#     elif request.method == 'PUT':
#         serializer = MovieValidateSerializer(instance=director, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(data=serializer.data, status=status.HTTP_200_OK)
#         return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#     elif request.method == 'DELETE':
#         director.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
#
# @api_view(http_method_names=['GET', 'POST'])
# def movies_list_create_api_view(request):
#     if request.method == 'GET':
#         movies = Movie.objects.all()
#         return Response(data=MovieSerializer(movies, many=True).data, status=status.HTTP_200_OK)
#
#     elif request.method == 'POST':
#         serializer = MovieValidateSerializer(data=request.data)
#         if serializer.is_valid():
#             Movie.objects.create(**serializer.validated_data)
#
#             return Response(data=serializer.data, status=status.HTTP_201_CREATED)
#         return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
# @api_view(http_method_names=['GET', 'PUT', 'DELETE'])
# def movies_detail_api_view(request, id):
#     try:
#         movie = Movie.objects.get(id=id)
#     except Movie.DoesNotExist:
#         return Response(data={'error': 'Page not found'}, status=status.HTTP_404_NOT_FOUND)
#
#     if request.method == 'GET':
#         return Response(data=MovieSerializer(instance=movie).data)
#
#     elif request.method == 'PUT':
#         serializer = MovieValidateSerializer(instance=movie, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(data=serializer.data, status=status.HTTP_200_OK)
#         return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#     elif request.method == 'DELETE':
#         movie.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
#
# @api_view(http_method_names=['GET', 'POST'])
# def reviews_list_create_api_view(request):
#     if request.method == 'GET':
#         reviews = Review.objects.all()
#         return Response(data=ReviewSerializer(reviews, many=True).data, status=status.HTTP_200_OK)
#
#     elif request.method == 'POST':
#         serializer = ReviewValidateSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(data=serializer.data, status=status.HTTP_201_CREATED)
#         return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
# @api_view(http_method_names=['GET', 'PUT', 'DELETE'])
# def reviews_detail_api_view(request, id):
#     try:
#         review = Review.objects.get(id=id)
#     except Review.DoesNotExist:
#         return Response(data={'error': 'Page not found'}, status=status.HTTP_404_NOT_FOUND)
#
#     if request.method == 'GET':
#         return Response(data=ReviewSerializer(instance=review).data)
#
#     elif request.method == 'PUT':
#         serializer = ReviewValidateSerializer(instance=review, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(data=serializer.data, status=status.HTTP_200_OK)
#         return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#     elif request.method == 'DELETE':
#         review.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)

# Optional root API view
# @api_view(http_method_names=['GET'])
# def api_root(request):
#     return Response({
#         'Admin': '/admin/',
#         'Directors': '/api/v1/director/',
#         'Movies': '/api/v1/movies/',
#         'Reviews': '/api/v1/reviews/',
#     })
