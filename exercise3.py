def recibe(arreglo, objetivo):
    result=[]
    for i in arreglo:
        for j in arreglo:

            sumaArreglo= i+j
            if sumaArreglo == objetivo:
                result.append(arreglo.index(i))
                result.append(arreglo.index(j))
    return result

print(recibe([8,2,4],6))
        

