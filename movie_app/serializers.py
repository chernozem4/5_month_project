from rest_framework import serializers
from .models import Director, Movie, Review, Category, SearchTag, STARS
from rest_framework.exceptions import ValidationError

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
        fields = ['id', 'title', 'description', 'duration', 'director','created', 'genre', 'tags', 'average_rating']

    def get_average_rating(self, obj):
        return obj.average_rating() or 0  # Default to 0 if no ratings

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ['id', 'text', 'stars', 'movie']


class DirectorValidateSerializer(serializers.Serializer):
    name = serializers.CharField(required=True, min_length=1)
    movie_count = serializers.IntegerField(required=False)
    category = serializers.SerializerMethodField()

    def validate_category(self, value):
        if not Category.objects.filter(id=value).exists():
            raise serializers.ValidationError("Category does not exist.")
        return value

    def validate_name(self, value):
        if not value or len(value) < 1:
            raise serializers.ValidationError("Name is required and cannot be empty.")
        return value


#
class MovieValidateSerializer(serializers.Serializer):
    title = serializers.CharField(required=True, min_length=1)
    description = serializers.CharField()
    duration = serializers.IntegerField()
    director_id = serializers.IntegerField()

    def validate_duration(self, value):
        if value <= 0:
            raise serializers.ValidationError("Duration must be greater than zero.")
        return value

    def validate_director(self, value):
        if not Director.objects.filter(id=value).exists():
            raise serializers.ValidationError("Director does not exist.")
        return value



    # title = serializers.CharField(required=True, max_length=1)
    # description = serializers.CharField(required=False, min_length=10)
    # duration = serializers.IntegerField(required=False)
    # director = serializers.SerializerMethodField(required=True, min_length=2)
    # is_active = serializers.BooleanField()
    # created = serializers.DateTimeField(required=False)
    # genre = serializers.SerializerMethodField()
    # tags = serializers.SerializerMethodField()
    # average_rating = serializers.SerializerMethodField()

class ReviewValidateSerializer(serializers.Serializer):
    text = serializers.CharField(required=True, max_length=999)
    movie = serializers.SerializerMethodField()
    stars = serializers.IntegerField(required=False)
    director = serializers.SerializerMethodField()

    def validate_movie(self, value):
        if not Movie.objects.filter(id=value).exists():
            raise serializers.ValidationError("Movie does not exist.")
        return value

    def validate_stars(self, value):
        if value not in dict(STARS).keys():
            raise serializers.ValidationError("Invalid number of stars.")
        return value

