from django.shortcuts import render, redirect
from django.views.generic import TemplateView, View
from app.models import MyUser, Tweet
from django.db.models import Q
from django.core.urlresolvers import reverse
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout

# Create your views here.

class Home(TemplateView):
	template_name = 'home.html' 

	def get_context_data(self, **kwargs):
		context = super(Home,self).get_context_data(**kwargs)
		context['all'] = MyUser.objects.all()
		context['me'] = MyUser.objects.get(usuario=self.request.user)
		context['notme'] = MyUser.objects.filter(follow__usuario=self.request.user)
		context['notfollow'] = MyUser.objects.filter(~Q(follow__usuario=self.request.user))
		context['tweets'] = Tweet.objects.filter(user=self.request.user)
		return context

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
