from django.urls import path
from . import views

app_name='arts'

urlpatterns = [
    path('conta', views.conta, name='conta'),
    path('', views.post_list, name='post_list'),
    path('MarketPlace/', views.MarketPlace, name='MarketPlace'),
    path('jobs/', views.JobsList, name='JobsList'),
    path('post/new/', views.post_new, name='post_new'),
    path('novaArte/', views.cadastrarArte, name = 'newArt'),
    path('comprar/<int:pk>/', views.comprarArte, name='comprarArte'),
    path('cadastrar/', views.cadastrarJob, name='cadastrarJob'),
    path('confirm/<int:pk>', views.confirmPurchase, name = 'confirm'),
    path('enviarMensagem/', views.EnviarEmail, name = 'enviarMensagem'),
    path('mensagemEnviada/', views.MensagemEnviada, name = 'mensagemEnviada')
]