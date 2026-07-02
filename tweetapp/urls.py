from django.urls import path
from . import views

app_name = 'tweetapp'

urlpatterns = [
    path('', views.listtweet, name='listtweet'),
    path('add/', views.addtweet, name='addtweet'),
    path('addbyform/', views.addtweet_with_form, name='addtweetbyform'),
    path('addbymodelform/', views.addtweet_with_model_form, name='addtweetbymodelform'),
    path('signup/', views.SignUpView.as_view(), name='signup'),
    path('delete/<int:tweet_id>/', views.deletetweet, name='deletetweet'),
]
