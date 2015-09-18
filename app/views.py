from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import TemplateView, View
from app.models import MyUser, Tweet, Retweet, Favorite
from app.forms import TweetForm
from django.db.models import Q
from django.core.urlresolvers import reverse
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.http import HttpResponse
from django.contrib import messages

# Create your views here.

class Home(TemplateView):
	template_name = 'home.html' 

	def get_context_data(self, **kwargs):
		context = super(Home,self).get_context_data(**kwargs)
		context['all'] = MyUser.objects.all()
		context['notme'] = MyUser.objects.filter(~Q(usuario=self.request.user))
		context['follow'] = MyUser.objects.filter(follow__usuario=self.request.user)
		context['notfollow'] = MyUser.objects.filter(~Q(follow__usuario=self.request.user))
		context['users'] = MyUser.objects.get(usuario=self.request.user).follow.all()
		context['retweets'] = Retweet.objects.all().values_list('tweet__id', flat=True)
		context['favorites'] = Favorite.objects.all().values_list('tweet__id', flat=True)
		return context

def new_tweet(request):
	if request.method == 'POST':
		tweet = Tweet(tweet = request.POST['tweet'], user=request.user)
		tweet.save()
		messages.success(request, 'Twiteado')
		return redirect(reverse('home'))

	return render(request, 'new_tweet.html')

def update_tweet(request, id_tweet):
	instance = Tweet.objects.get(id=id_tweet)

	if request.method == 'POST':
		form = TweetForm(request.POST, instance=instance)

		if form.is_valid():
			form.save()
			return redirect(reverse('home'))
		else:
			return render(request, 'update_tweet.html', {'form' : form})

	form = TweetForm(instance=instance)
	return render(request, 'update_tweet.html', {'form' : form})

def delete_tweet(request, id_tweet):
	Tweet.objects.filter(id=id_tweet).delete()
	return redirect(reverse('home'))

		
class AddFollow(View):
	def get(self,request,id):
		me = MyUser.objects.get(usuario=request.user)
		followed = MyUser.objects.get(id=id)
		me.follow.add(followed)
		return redirect(reverse('home'))

class RemoveFollow(View):
	def get(self,request,id):
		me = MyUser.objects.get(usuario=request.user)
		followed = MyUser.objects.get(id=id)
		me.follow.remove(followed)
		return redirect(reverse('home'))

def login(request):
	if request.method == 'POST':		
		usuario = request.POST['usuario']
		password = request.POST['password']
		user = authenticate(usuario=usuario, password=password)
		if user:
			auth_login(request, user)
			return redirect(reverse('home'))
		else:
			return render(request, "login.html")
	else:
		return render(request, "login.html")

def logout(request):
	auth_logout(request)
	return redirect(reverse('home'))

class AddRetweet(View):
	def get(self, request, id_tweet):
		try:
			tweet = Tweet.objects.get(~Q(user=request.user), id=id_tweet)
			retweet = Retweet.objects.get_or_create(user=request.user, tweet=tweet)
		except:
			messages.warning(request, 'No se puede anadir a retweets')
			return redirect(reverse('home'))

		messages.success(request, 'Retwiteado')
		return redirect(reverse('home'))

class RemoveRetweet(View):
	def get(self,request, id_tweet):
		try:
			tweet = Tweet.objects.get(~Q(user=request.user), id=id_tweet)
			retweet = Retweet.objects.get(user=request.user, tweet=tweet).delete()
		except:
			messages.warning(request, 'No se puede eliminar de retweets')
			return redirect(reverse('home'))

		messages.success(request, 'Retwit eliminado')
		return redirect(reverse('home'))

class AddFavorite(View):
	def get(self, request, id_tweet):
		try:
			tweet = Tweet.objects.get(~Q(user=request.user), id=id_tweet)
			favorite = Favorite.objects.get_or_create(user=request.user, tweet=tweet)
		except:
			messages.warning(request, 'No se puede anadir')
			return redirect(reverse('home'))
		
		messages.success(request, 'Anadido a favoritos')
		return redirect(reverse('home'))

class RemoveFavorite(View):
	def get(self, request, id_tweet):
		try:
			tweet = Tweet.objects.get(~Q(user=request.user), id=id_tweet)
			favorite = Favorite.objects.get(user=request.user, tweet=tweet).delete()
		except:
			messages.warning(request, 'No se puede eliminar')
			return redirect(reverse('home'))

		messages.success(request, 'Favorito eliminado')
		return redirect(reverse('home'))
