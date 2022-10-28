from .models import Director, Movie, Review
from rest_framework import serializers


class DirectorSerializer(serializers.ModelSerializer):
    movies_count = serializers.SerializerMethodField()

    class Meta:
        model = Director
        fields = 'id name movies_count'.split()

    def get_movies_count(self, director):
        return director.movies.count()


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = 'id text stars_str'.split()


class MovieSerializer(serializers.ModelSerializer):

    class Meta:
        model = Movie
        fields = 'id title description duration'.split()


class MovieReviewsSerializers(serializers.ModelSerializer):
    reviews = ReviewSerializer(many=True)

    class Meta:
        model = Movie
        fields = 'title reviews rating'.split()
