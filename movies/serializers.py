from rest_framework import serializers
from movies.models import Movies


class MoviesSerializer(serializers.ModelSerializer):

    class Meta:
        model = Movies
        fields = '__all__'
