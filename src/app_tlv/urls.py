from django.urls import path
from . import views
from django.contrib.auth.views import LoginView, LogoutView
from app_tlv.views import IndexView, agregar_producto


urlpatterns = [
    path('home/', IndexView.as_view(), name='home'),
    path('bienvenido/', views.bienvenido, name='bienvenido'),
    path('login/', LoginView.as_view(template_name='app_tlv/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='app_tlv/logout.html'), name='logout'),
    path('producto_detail/',views.producto_detail, name='producto_detail' ),
    path('carrito/',views.agregar_producto, name='carrito' ),
    path("agregar/<int:producto_id>", agregar_producto, name="Add"),
]