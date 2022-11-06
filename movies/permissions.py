from rest_framework.generics import ListAPIView
from movies.models import Booking
from .serializer import ListSerializer
from rest_framework.permissions import BasePermission

class Authenticated(BasePermission):
    messeage = " you will see the movies list if you are authenticated "

    def has_object_permission(self, request, view, obj):
        if request.user.auth or request.user == obj.user:
            return False
        return True