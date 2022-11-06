from django.contrib.auth.models import User
from django.contrib.auth import get_user_model 
from rest_framework import serializers 
from movies.models import Movie, Booking
from rest_framework_simplejwt.tokens import RefreshToken

User = get_user_model()

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True) # for hashing 
    class Meta:
        model = User
        fields = ["username", "password","first_name","last_name"]

        def create(self, validated_data):
            username = validated_data["username"]
            password = validated_data["password"]
            first_name = validated_data["first_name"]
            last_name = validated_data["last_name"]
            new_user = User(username=username, first_name=first_name, last_name=last_name)
            new_user.set_password(password)
            new_user.save()
            return validated_data

class MovieSerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie 
        fields = ["title", "description"]

class LoginSerializer(serializers.ModelSerializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        username = data.get("username")
        password = data.get("password")
        id = data.get("ID")
        email = data.get ("email")
        
        token = serializers.CharField(allow_blank=True,read_only=True)
        
        try:
            user_obj = User.objects.get(username=username)
        except User.DoesNotExist:
            raise serializers.ValidationError("no shuch username")
        if not user_obj.check_password(password):
            raise serializers.ValidationError("worng password")
        
        payload = RefreshToken.for_user(user_obj)
        token = str(payload.access_token)
        data["token"] = token  
        return data 

    def get_token(cls, user_obj):
        token = super().get_token(user_obj)
        token["id"] = user_obj.id
        token["username"] = user_obj.username
        token["email"] = user_obj.email
        token["expiration"] = user_obj.expiration

        return token

class ListSerializer(serializers.ModelSerializer): # need permission
    class Meta:
        model = Movie
        fields = ["name", "date"]