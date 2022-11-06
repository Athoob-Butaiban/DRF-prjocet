from django.shortcuts import render
from rest_framework.generics import ListAPIView, ListCreateAPIView, CreateAPIView 
from movies import serializer
from movies.models import Movie, Booking
from rest_framework.response import Response 
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST
from rest_framework.views import APIView
# Create your views here.

class RegisterView(CreateAPIView):
    serializer_class = serializer.RegisterSerializer


class MovieList(ListAPIView):
    queryset = Movie.objects.all()
    serializer_class = serializer.MovieSerSerializer

class LoginView(APIView):
    serializer_class = serializer.LoginSerializer

    def post(self, req):
        data = req.data 
        serializer = serializer.LoginSerializer(data=data)
        if serializer.is_valid(raise_exception=True):
            valid_data = serializer.data
            return Response(valid_data, status=HTTP_200_OK)
        else:
            return Response(serializer.errors, HTTP_400_BAD_REQUEST)