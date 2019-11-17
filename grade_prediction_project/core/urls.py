from django.contrib import admin
from django.urls import path
from django.conf.urls import include, url

urlpatterns = [
    url(r'^admin/', admin.site.urls, name='admin'),
    url(r'', include('grade_prediction.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    url(r'^account/', include(('social_django.urls','social'), namespace='social')),
    url(r'^account/', include(('django.contrib.auth.urls','auth'), namespace='auth')),
]




