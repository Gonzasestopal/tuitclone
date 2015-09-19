from django.conf.urls import include, url, patterns
from django.contrib import admin
from app.views import Home, AddFavorite, ListaRt, Timeline, signup, RemoveFavorite, AddFollow, RemoveFollow, login, logout, RemoveRetweet, AddRetweet, new_tweet, update_tweet, delete_tweet
from django.conf import settings
from django.contrib.auth.decorators import login_required


urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', login_required(Home.as_view()), name='home'),
    url(r'^lista_rt/$',ListaRt.as_view(), name="lista_rt"),
    url(r'^timeline/$', Timeline.as_view(), name="timeline"),
    url(r'^add_follow/(?P<id>\d{1,})/$', AddFollow.as_view(), name="add_follow"),
    url(r'^remove_follow/(?P<id>\d{1,})/$', RemoveFollow.as_view(), name="remove_follow"),
    url(r'^accounts/login/', login, name="login"),
    url(r'^logout/', logout, name="logout"),
    url(r'^signup/', signup, name="signup"),
    url(r'^new_tweet/$',new_tweet, name='new_tweet'),
    url(r'^update_tweet/(?P<id_tweet>\d{1,})/$', update_tweet, name='update_tweet'),
    url(r'^delete_tweet/(?P<id_tweet>\d{1,})/$', delete_tweet, name='delete_tweet'),
    url(r'^add_favorite/(?P<id_tweet>\d{1,})/$', AddFavorite.as_view(), name='add_favorite'),
    url(r'^remove_favorite/(?P<id_tweet>\d{1,})/$', RemoveFavorite.as_view(), name='remove_favorite'),
    url(r'^add_retweet/(?P<id_tweet>\d{1,})/$', AddRetweet.as_view(), name='add_retweet'),
    url(r'^remove_retweet/(?P<id_tweet>\d{1,})/$', RemoveRetweet.as_view(), name='remove_retweet')
]
