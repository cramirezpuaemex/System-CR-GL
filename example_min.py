import numpy as np
import random
from sklearn import linear_model
from sklearn.metrics import mean_squared_error, r2_score
import matplotlib.pyplot as plt
#matplotlib inline
 
# Generador de distribucion de datos para regresion lineal simple
def generador_datos_simple(beta, muestras, desviacion):
# Genero n (muestras) valores de x aleatorios entre 0 y 100
x = np.random.random(muestras) * 100
# Genero un error aleatorio gaussiano con desviación típica (desviacion)
e = np.random.randn(muestras) * desviacion
# Obtengo el y real como x*beta + error
y = x * beta + e
return x.reshape((muestras,1)), y.reshape((muestras,1))
 
# Parámetros de la distribución
desviacion = 200
beta = 10
n = 50
x, y = generador_datos_simple(beta, n, desviacion)
 
# Represento los datos generados
plt.scatter(x, y)
plt.show()
