"""
Definition of urls for blog_project.
"""

from django.conf.urls import include, url
from django.contrib.auth import views

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = [
    url(r'', include('blog.urls')),
    url(r'admin/', admin.site.urls),
    url(r'accounts/login/$', views.login, name='login'),
    url(r'account/logout/$', views.logout, name='logout', kwargs={ 'next_page' : '/' }),
]
