from django.urls import path
from . import views
from .views import *
from django.contrib.auth.views import LogoutView

urlpatterns = [

    path('', HomePageView.as_view(), name='index'),
    path('dashboard/', DashboardPageView.as_view(), name='home'),
     path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', CustomLogoutView.as_view(), name='logout'),
]
