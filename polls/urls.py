from django.urls import path
from . import views

app_name = 'polls'

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:question_id>/', views.detail, name='detail'),
    path('<int:question_id>/results/', views.results, name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
    path('<int:question_id>/first/', views.first, name='first'),
    path('newquestion/', views.newquestion, name='newquestion'),
    path('newchoice/', views.newchoice, name='newchoice'),
    path('list/', views.list, name='list'),
    path('<int:pk>/edit/', views.editquestion, name='editquestion'),
    path('<int:pk>/delete/', views.deletequestion, name='deletequestion'),
    path('choices/list/', views.listchoices, name='listchoices'),
    path('choices/<int:pk>/edit/', views.editchoice, name='editchoice'),
    path('choices/<int:pk>/delete/', views.deletechoice, name='deletechoice'),
]