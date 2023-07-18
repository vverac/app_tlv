from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from app_tlv.Carrito import Carrito
from .models import Producto

class IndexView(TemplateView):
  template_name='app_tlv/landing.html'

def bienvenido(request):
  return render(request, 'app_tlv/bienvenido.html') 

# muestra productos de la tienda
def producto_detail(request):
      productos = Producto.objects.all()
      return render ( request,'app_tlv/producto_detail.html', {'productos':productos})


def agregar_producto(request, producto_id):
  carrito= Carrito(request)
  producto=Producto.objects.get(id=producto_id)
  carrito.agregar(producto)
  return redirect('producto_detail')