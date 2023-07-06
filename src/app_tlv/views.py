from django.shortcuts import render
from django.views.generic import TemplateView

class IndexView(TemplateView):
  template_name='app_tlv/landing.html'

def bienvenido(request):
  return render(request, 'app_tlv/bienvenido.html') 
