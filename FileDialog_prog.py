import os
from datetime import datetime

ruta_app = os.getcwd()  # obtiene ruta del script 
contenido = os.listdir(ruta_app)  # obtiene lista con archivos/dir 
total = 0
archivos = 0
formato = '%d-%m-%y %H:%M:%S'  # establece formato de fecha-hora
linea = '-' * 40

for elemento in contenido:
    archivo = ruta_app + os.sep + elemento
    if not os.access(archivo, os.X_OK) and os.path.isfile(archivo):
        archivos += 1
        estado = os.stat(archivo)  # obtiene estado del archivo
        tamano = estado.st_size  # obtiene de estado el tamano 
        
        # Obtiene del estado fechas de ultimo acceso/modificacion
        # Como los valores de las fechas-horas vienen expresados
        # en segundos se convierten a tipo datetime. 
        
        ult_acceso = datetime.fromtimestamp(estado.st_atime)
        modificado = datetime.fromtimestamp(estado.st_mtime)
        
        # Se aplica el formato establecido de fecha y hora
        
        ult_acceso = ult_acceso.strftime(formato)
        modificado = modificado.strftime(formato)
        
        # Se acumulan tamanos y se muestra info de cada archivo
        
        total += tamano
        print(linea)
        print('archivo      :', elemento)
        print('modificado   :', modificado)        
        print('ultimo acceso:', ult_acceso)
        print('tamano (Kb)  :', round(tamano/1024, 1))

print(linea)
print('Num. archivos:', archivos)
print('Total (kb)   :', round(total/1024, 1))