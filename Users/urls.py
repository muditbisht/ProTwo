from django.contrib import admin
from django.conf.urls import url
from Users import views

app_name = 'Users'

urlpatterns = [
    url(r'^$',views.index),
    url(r'^register/$',views.register),
    url(r'^login/',views.user_login),
    url(r'^logout/$',views.user_logout),
]
