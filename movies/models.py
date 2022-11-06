from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Movie(models.Model):
    title = models.TextField()
    description = models.CharField(max_length=150)

class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="booking")
    date = models.DateField()
    movie_name = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name="booking")

    def __str__(self):
        return (self.user, str(self.movie_name))