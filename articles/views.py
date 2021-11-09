from django.shortcuts import render
from . import models

# Create your views here.
def articles_handler(request):
 article = models.Articles.objects.all().order_by('date')
 args ={'articles':article}
 return render(request, 'articles/article.html',args)
 