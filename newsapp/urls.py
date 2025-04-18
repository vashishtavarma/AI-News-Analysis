from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('logout/', views.logout_view, name='logout'),
    
    # Region, Sentiment, and Category URLs
    path('<str:region_name>/', views.region_view, name='region'),
    path('<str:region_name>/<str:sentiment_name>/', views.sentiment_view, name='sentiment'),
    path('<str:region_name>/<str:sentiment_name>/<str:category_name>/', views.category_view, name='category'),
]