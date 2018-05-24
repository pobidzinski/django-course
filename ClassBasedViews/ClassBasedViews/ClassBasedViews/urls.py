"""
Definition of urls for ClassBasedViews.
"""

from django.conf.urls import include, url
from basic_app import views

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = [
    url(r'^$', views.IndexView.as_view()),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^basic_app/', include('basic_app.urls', namespace='basic_app'))
]
