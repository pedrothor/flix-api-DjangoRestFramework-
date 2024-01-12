from rest_framework import generics
from genres.models import Genre
from genres.serializers import GenreSerializer


# lista (GET) e cria gêneros (POST)

class GenreCreateListView(generics.ListCreateAPIView):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer


# faz buscas, edita e deleta gêneros
class GenreRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
