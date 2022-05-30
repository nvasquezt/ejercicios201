ocupacion = [[False,False,False],
             [False,False,False],
             [False,False,False]]

puestos ={1:[0,0],2:[0,1],3:[0,2],
          4:[1,0],5:[1,1],6:[1,2],
          7:[2,0],8:[2,1],9:[2,2]  
          }

def validar(puesto, ocupacion):

  x = puestos[int(puesto)]  # x es el valor que tiene el diccionario en esa posición
  xi = x[0]                 
  xj= x[1]

  if ocupacion[xi][xj] == False             :
      return 'Libre'
  else:
      return 'Ocupado'

def ocupar(puesto, ocupacion, validacion):
  x = puestos[int(puesto)]  #  x es el valor que tiene el diccionario en esa posición
  xi = x[0]
  xj= x[1]

  if validacion == "Libre":
    ocupacion[xi][xj] = True

  return ocupacion
  
def liberar(puesto, ocupacion, validacion):
  x = puestos[int(puesto)]  #  x es el valor que tiene el diccionario en esa posición
  xi = x[0]
  xj= x[1]

  if validacion == "Ocupado":
    ocupacion[xi][xj] = False
      
  return ocupacion

validacion = validar(9,ocupacion)
print(validacion)
ocupacion = ocupar(9,ocupacion,validacion)
print(ocupacion[2][2])


validacion = validar(9,ocupacion)
print(validacion)
ocupacion = ocupar(9,ocupacion,validacion)
print(ocupacion[2][2])

validacion = validar(9,ocupacion)
print(validacion)
ocupacion = liberar(9,ocupacion,validacion)
print(ocupacion[2][2])
