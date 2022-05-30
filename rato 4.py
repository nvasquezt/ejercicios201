def total_compra(telefonos, cantidades):
  productos=["Samsung","Xiaomi","Motorola","Huawei","Alcatel"]
  precios = [950,750,720,890,670]
  total_compra= 0

  if len(telefonos) != len(cantidades):
    return "Error"
  else:
    for i in range(len(telefonos)):
      for j in range(len(productos)):
        if telefonos[i] == productos[j]:
          total_compra = total_compra + (int(cantidades[i])*int(precios[j]))
        else:
          continue
    return total_compra

def descuento(telefonos,cupon,total):
 
  if cupon != "H5K986W":
    return"Cupón inválido"
  else:
    if ("Samsung" in telefonos) and ("Motorola" in telefonos):
      descuento = 200
    elif ("Samsung" in telefonos) or ("Motorola" in telefonos):
      descuento = 100
    else:
      descuento= 0

    total_descuento =total-descuento
    return total_descuento


telefonos = ["Samsung","Huawei","Motorola","Alcatel"]
cantidades = [2,1,1,1]
cupon ="H5K986s"
total=total_compra(telefonos,cantidades)
print(total)
total_desc =descuento(telefonos,cupon,total)
print(total_desc)
