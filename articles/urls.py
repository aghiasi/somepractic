from django.contrib import admin
from django.urls import path,include
from .import views

app_name = 'articles'
urlpatterns = [

    path('',views.articles_handler,name='list')
    ,path('<slug>',views.articles_slug,name ='detail')

]


