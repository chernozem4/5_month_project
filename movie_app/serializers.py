from rest_framework import serializers
from .models import Director, Movie, Review, Category, SearchTag

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class SearchTagSerializer(serializers.ModelSerializer):
    class Meta:
        model = SearchTag
        fields = '__all__'

class DirectorSerializer(serializers.ModelSerializer):
    movie_count = serializers.SerializerMethodField()

    class Meta:
        model = Director
        fields = ['id', 'name', 'movie_count']

    def get_movie_count(self, obj):
        return obj.movies.count()

class MovieSerializer(serializers.ModelSerializer):
    genre = CategorySerializer(many=False)
    tags = SearchTagSerializer(many=True)
    director = DirectorSerializer(many=False)
    average_rating = serializers.SerializerMethodField()

    class Meta:
        model = Movie
        fields = ['id', 'title', 'description', 'duration', 'director', 'genre', 'tags', 'average_rating']

    def get_average_rating(self, obj):
        return obj.average_rating() or 0  # Default to 0 if no ratings

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ['id', 'text', 'stars', 'movie', 'director']
