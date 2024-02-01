from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name = "home"),
    path('soccebot-registration/', views.soccerbot_registration, name = "soccer"),
    path('line-follower-robot-registration/', views.linefollow_registration, name = "line-follow"),
    path('robo-racing-registration/', views.robo_race_registration, name = "robo-racing"),
    path('prompt-engineering-registration/', views.chatbot_registration, name = "chatbot"),
    path('idea-competetion-registration/', views.idea_gen_registration, name = "idea-gen"),
    
]