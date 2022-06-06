import os
from datetime import datetime

class Pos_Analisis_Resultados():
    def main(self):

    #ruta_app = os.getcwd()  # obtiene ruta del script 
    ruta_app = '/home/carlos/Escritorio/Analisis_Resultados/027/'

    contenido = os.listdir(ruta_app)  # obtiene lista con archivos/dir 
    contenido=sorted(contenido)


    total = 0
    archivos = 0
    formato = '%d-%m-%y %H:%M:%S'  # establece formato de fecha-hora
    linea = '-' * 40
    arch=[]
    #for i in range(len(contenido)):
    for i in range(1):    
        aux=[]
        ruta_archivo=ruta_app+'/'+contenido[i]

        print ruta_archivo
        contenido_files= os.listdir(ruta_archivo)
        contenido_files=sorted(contenido_files)
        #print contenido_files
        for elemento in range(len(contenido_files)):
            print contenido_files[elemento]
            if contenido_files[elemento].find('.txt')!= -1:
                aux.append(contenido_files[elemento])
        print aux





inicio=Pos_Analisis_Resultados()
inicio.main()
'''
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
        arch.append(elemento)
        print(linea)
        print('archivo      :', elemento)
'''

print(linea)
print('Num. archivos:', archivos)
print('Total (kb)   :', round(total/1024, 1))

for i in arch:
    print i