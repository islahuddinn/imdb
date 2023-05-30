from rest_framework import generics
from .models import Movie
from .serializers import MovieSerializer
from bson import ObjectId
from rest_framework.response import Response
from rest_framework.decorators import api_view
from pymongo import MongoClient


class AddData(generics.ListCreateAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

# class GetData(generics.ListAPIView):
#     queryset = Movie.objects.using('api_movie').all()
#     # queryset = Movie.objects.all()
#     serializer_class = MovieSerializer


@api_view(['GET'])
def get_movies(request):
    client = MongoClient('mongodb://host.docker.internal:27017/')
    # client = MongoClient('mongodb://localhost:27017/')

    if 'demo' in client.list_database_names():
        database = client['demo']
        collection = database['api_movie']
        movies = list(collection.find())

        
        for movie in movies:
            movie['_id'] = str(movie['_id'])

        
        client.close()

    
        return Response(movies)
    else:
        return Response({'message': 'Database does not exist'}, status=404)









