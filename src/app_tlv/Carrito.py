#aca se manejara el contenido de nuestro carrito
class Carrito:
  def __init__(self, request):
    self.request= request
    self.session= request.session
    carrito = self.session.get('carrito')
    if not carrito:
      self.session['carrito'] = {}
      self.carrito = self.session['carrito']
    else:
       self.carrito = carrito


  # para agregar un nuevo productp, pedimos el producto que es del tipo models
  def agregar(self, producto):
    id=str(producto.id)
    if id not in self.carrito.keys():
      self.carrito[id]={
        'producto_id':producto.id,
        'nombre':producto.name,
        'acumulado':producto.price,
        'cantidad':1,
      }
    else:
      self.carrito[id]['cantidad'] += 1
      self.carrito[id]['acumulado'] += producto.price
    self.guardar_carrito()


  def guardar_carrito(self):
    self.session['carrito']= self.carrito
    self.session.modified = True

