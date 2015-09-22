from django.shortcuts import render
from rest_framework import viewsets
from app.models import MyUser, Tweet
from api.serializers import TweetSerializer, MyUserSerializer

class TweetViewSet(viewsets.ModelViewSet):
	serializer_class = TweetSerializer
	queryset = Tweet.objects.all().order_by('-date')

class MyUserViewSet(viewsets.ModelViewSet):
	serializer_class = MyUserSerializer
	queryset = MyUser.objects.all()