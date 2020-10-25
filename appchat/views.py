from django.shortcuts import render

from django.http import HttpResponse

def abcd(request):
	return HttpResponse("<h1><marquee><font color=red>Hello, world. You're at the polls index.")

def index(request):
	return render(request, 'appchat/index.html')


# Create your views here.
