from django.urls import ppath

from . import views

urlparttens = [
	path('signup/', views.SignUp.as_view(), name='signup'),
]