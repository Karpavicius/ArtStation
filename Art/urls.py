from django.urls import path
from . import views

app_name='arts'

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('MarketPlace/', views.MarketPlace, name='MarketPlace'),
    path('jobs/', views.JobsList, name='JobsList'),
    path('post/new/', views.post_new, name='post_new'),
    # path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
    path('novaArte/', views.cadastrarArte, name = 'newArt'),
    path('comprar/<int:pk>/', views.comprarArte, name='comprarArte'),
    path('cadastrar/', views.cadastrarJob, name='cadastrarJob'),
    path('confirm/<int:pk>', views.confirmPurchase, name = 'confirm')
]