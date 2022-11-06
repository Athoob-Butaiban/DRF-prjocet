from django.shortcuts import render
from rest_framework.generics import ListAPIView, ListCreateAPIView, CreateAPIView 
from movies import serializer
from movies.models import Movie, Booking

# Create your views here.

class RegisterView(CreateAPIView):
    serializer_class = serializer.RegisterSerializer


class MovieList(ListAPIView):
    queryset = Movie.objects.all()
    serializer_class = serializer.MovieSerSerializer

