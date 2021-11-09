from django.shortcuts import render,HttpResponse
from . import models

# Create your views here.
def articles_handler(request):
 article = models.Articles.objects.all().order_by('date')
 args ={'articles':article}
 return render(request, 'articles/article.html',args)
 
def articles_slug(request,slug):
 article = models.Articles.objects.get(slug=slug)
 args ={'articles':article}
 return render(request, 'articles/slug.html',args )