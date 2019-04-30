from django.urls import path
from . import views

urlpatterns = [
    path('ArtStation', views.post_list, name='post_list'),
    path('MarketPlace', views.MarketPlace, name='MarketPlace'),
    path('Jobs', views.Jobs, name='Jobs'),
    path('post/new/', views.post_new, name='post_new'),
    path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
]