from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^profile/$', views.update_profile, name='profile'),
    url(r'^account/logout/$', views.logout, name='logout'),
    url(r'^signup/$', views.signup, name='signup'),
    url(r'^class_search/$', views.class_search, name='class_search'),
    url(r'^advisor/$', views.advisor, name='advisor'),
]
