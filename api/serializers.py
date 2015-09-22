from rest_framework import serializers
from app.models import MyUser, Tweet

class MyUserSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = MyUser
		fields = ('usuario','email')

class TweetSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Tweet
		fields = ['user','tweet','date']