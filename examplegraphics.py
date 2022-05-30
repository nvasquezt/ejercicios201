#import matplotlib as plt
import pandas as pd

datos = {
    "Alimentos": ["manzana", "Pera", "Piña", "arandano","fresa"],
    "calorias":[52,55,55,35,32]
}

df = pd.DataFrame(datos)

print(df)
df.info()
df.describe()



