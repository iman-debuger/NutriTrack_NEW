from django.urls import path
from . import views

urlpatterns = [
    # When someone goes to the base URL of the app, run home_view
    path('', views.home_view, name='home'),
    path('diary/', views.diary_view, name='diary'),
]