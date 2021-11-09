from django.shortcuts import render
from django.shortcuts import HttpResponse

def home_handler(request):
 return render(request, 'home.html')