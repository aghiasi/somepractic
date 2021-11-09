from django.contrib import admin
from django.urls import path,include
from .import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [

    path('',views.articles_handler)

]

