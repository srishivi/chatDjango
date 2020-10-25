from django.urls import path

from . import views

urlpatterns = [
	path('', views.index, name='index'),
	path('room1/', views.abcd, name='abcd'),
]
