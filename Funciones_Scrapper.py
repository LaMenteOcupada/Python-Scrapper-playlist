
#Monitoriza el precio historico
def Monitor_Cambios_Precio(precioActual , precioHistorico):
  if(precioActual < precioHistorico):
      print("Atención , el producto ha bajado de precio a " + str(precioActual) + "€")
      #avisar al usuario
  elif(precioActual > precioHistorico):
      print("Ha subido de precio a "+ precioActual + "€")
  else:
      print("No hay una oferta de momento, Sigue a su precio de " + str(precioActual) + "€")

#Monitoriza el precio deseado
def Oferta_Precio_Deseado(precioActual,precioDeseado):
  if(precioActual < precioDeseado):
      print("Atención , OFERTA!!! El artículo está por debajo del precio máximo deseado de "+str(precioDeseado)+"€.Está a " + str(precioActual) + "€. Ahorras "+ str(precioDeseado - precioActual) + "€!!!")
      return True
  elif(precioActual > precioDeseado):
      print("Ha subido de precio a "+ str(precioActual) + "€")
      return False
  else:
      print("No hay una oferta de momento, Sigue a su precio de " + str(precioActual) + "€")
      return False
