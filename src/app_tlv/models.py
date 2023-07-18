from django.db import models
import datetime

# PRODUCTO

class Producto(models.Model):
    name = models.CharField(max_length=60)
    price= models.IntegerField(default=0)
    description= models.CharField(max_length=250, default='', blank=True, null= True)
    image= models.ImageField(upload_to='uploads/products/')

    def __str__(self):
    # __str__ metodo para hacer una representacion de cadena
      return self.name

# metodos estaticos para acceder desde donde se requiera
    @staticmethod
    def get_producto_by_id(ids):
        return Producto.objects.filter (id__in=ids)

    @staticmethod
    def get_all_producto():
        return Producto.objects.all()




