from django.urls import path
from . import views
from django.contrib.auth.views import LoginView, LogoutView
from app_tlv.views import IndexView


urlpatterns = [
    path('home/', IndexView.as_view(), name='home'),
    path('bienvenido/', views.bienvenido, name='bienvenido'),
    path('login/', LoginView.as_view(template_name='app_tlv/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='app_tlv/logout.html'), name='logout'),

]