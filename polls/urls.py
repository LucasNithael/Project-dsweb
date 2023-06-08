from django.urls import path
from . import views

app_name = 'polls'

urlpatterns = [
    path('', views.index_view, name='index'),
    path('polls/alternative/<int:question_id>/', views.alternative_view, name='alternative'),
    path('polls/vote/<int:alternative_id>/', views.vote_view, name='vote'),
    path('polls/register/', views.register_view, name='register'),
]
