productos=["Samsung","Xiaomi","Motorola","Huawei","Alcatel"]
precios = [950,750,720,890,670]

def total_compra(telefonos, cantidades):
#Escribe tu código de la función
  total_compra = 0

  if len(telefonos)==len(cantidades): # SI LOS DOS TIENEN LA MISMA DIMENSIÓN, AVANZO

    for i in range(len(telefonos)):   # 0 1 2 3 
      for j in range(len(productos)): # 0 1 2 3 4
        if telefonos[i] == productos[j]:
          total_compra = total_compra + precios[j]*cantidades[i]
          break 
    return total_compra  
  else:
    return 'Error'
print(total_compra)

telefonos = ["Samsung","Xiaomi","Motorola","Alcatel"]
cantidades = [1,2,1,1]
total = total_compra(telefonos,cantidades)
#def descuento(telefonos,cupon,total):
