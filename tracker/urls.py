from django.urls import path
from django.views.generic import TemplateView
from django.views.static import serve
from django.conf import settings
from . import views
import os

urlpatterns = [
    # When someone goes to the base URL of the app, run home_view
    path('', views.home_view, name='home'),
    path('diary/', views.diary_view, name='diary'),
    path('profile/', views.profile_view, name='profile'),
    path('analyze/', views.analyze_food_view, name='analyze'),
    path('trends/', views.trends_view, name='trends'),
    path('login/', views.login_view, name='login'),
    path('signup/', views.signup_view, name='signup'),
    path('logout/', views.logout_view, name='logout'),
    path('sw.js', TemplateView.as_view(template_name='tracker/sw.js', content_type='application/javascript')),
]