from django.shortcuts import render
from rest_framework.generics import ListAPIView, ListCreateAPIView, CreateAPIView 
from movies import serializer
from movies.models import Movie, Booking
from rest_framework.response import Response 
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST
from rest_framework.views import APIView
from .permissions import Authenticated
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser 
# Create your views here.

class RegisterView(CreateAPIView):
    serializer_class = serializer.RegisterSerializer
    permission_classes = [AllowAny]

class MovieList(ListAPIView):
    queryset = Movie.objects.all()
    serializer_class = serializer.MovieSerSerializer
    permission_classes = [IsAuthenticated]


class LoginView(APIView):
    serializer_class = serializer.LoginSerializer
    permission_classes = [IsAuthenticated, IsAdminUser]
    def post(self, req):
        data = req.data 
        serializer = serializer.LoginSerializer(data=data)
        if serializer.is_valid(raise_exception=True):
            valid_data = serializer.data
            return Response(valid_data, status=HTTP_200_OK)
        else:
            return Response(serializer.errors, HTTP_400_BAD_REQUEST)

class ListView(APIView):
    serializer_class = serializer.ListSerializer
    permission_classes = [Authenticated] 

class Add(CreateAPIView):
    serializer_class = serializer.MovieSerSerializer
    parser_classes = [IsAuthenticated]
    '''
    def poat(self,):
        movie.append()
        

    '''