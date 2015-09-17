from django.conf.urls import include, url, patterns
from django.contrib import admin
from app.views import Home, AddFollow, RemoveFollow, login, logout
from django.conf import settings
from django.contrib.auth.decorators import login_required


urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', login_required(Home.as_view()), name='home'),
    url(r'^add_follow/(?P<id>\d{1,})/$', AddFollow.as_view(), name="add_follow"),
    url(r'^remove_follow/(?P<id>\d{1,})/$', RemoveFollow.as_view(), name="remove_follow"),
    url(r'^accounts/login/', login, name="login"),
    url(r'^logout/', logout, name="logout")
]
