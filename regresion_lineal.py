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
	# Genero un error aleatorio gaussiano con desviacion tipica (desviacion)
	e = np.random.randn(muestras) * desviacion
	# Obtengo el y real como x*beta + error
	y = x * beta + e
	return x.reshape((muestras,1)), y.reshape((muestras,1))
 
# Parametros de la distribucion
desviacion = 200
beta = 10
n = 50
x, y = generador_datos_simple(beta, n, desviacion)
 
# Represento los datos generados
plt.scatter(x, y)




# Creo un modelo de regresion lineal
modelo = linear_model.LinearRegression()
 
# Entreno el modelo con los datos (X,Y)
modelo.fit(x, y)
# Ahora puedo obtener el coeficiente b_1
print u'Coeficiente beta1: ', modelo.coef_[0]
 
# Podemos predecir usando el modelo
y_pred = modelo.predict(x)
 
# Por ultimo, calculamos el error cuadratico medio y el estadistico R^2
print u'Error cuadratico medio: %.2f' % mean_squared_error(y, y_pred)
print u'Estadistico R_2: %.2f' % r2_score(y, y_pred)

# Representamos el ajuste (rojo) y la recta Y = beta*x (verde)
plt.scatter(x, y)
plt.plot(x, y_pred, color='red')
x_real = np.array([0, 100])
y_real = x_real*beta
plt.plot(x_real, y_real, color='green')
plt.show()
