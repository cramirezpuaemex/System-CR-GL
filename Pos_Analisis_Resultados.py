import os
from datetime import datetime
from posAnalisis import *



class Pos_Analisis_Resultados():
    def main(self, cont):
        inicio_read_file=posAnalisis()
        

        path_salve_resultados="/home/b_res"
        if not os.path.exists(path_salve_resultados):
                os.makedirs(path_salve_resultados)

        dia_a=str(cont)
        #ruta_app = os.getcwd()  # obtiene ruta del script
        if len(dia_a)==1:
            ruta_app = path_salve_resultados+'/00'+dia_a+'/'
        elif len(dia_a)==2:
            ruta_app = path_salve_resultados+'/0'+dia_a+'/'
        else:
            ruta_app = path_salve_resultados+'/'+dia_a+'/'
        print ruta_app
        contenido = os.listdir(ruta_app)  # obtiene lista con archivos/dir 
        contenido=sorted(contenido)

        #print contenido
        total = 0
        archivos = 0
        formato = '%d-%m-%y %H:%M:%S'  # establece formato de fecha-hora
        linea = '-' * 40
        arch=[]
        for i in range(len(contenido)):
        #for i in range(3):    
            aux=[]
            ruta_archivo=ruta_app+contenido[i]

            print ruta_archivo
            contenido_files= os.listdir(ruta_archivo)
            contenido_files=sorted(contenido_files)
            #print contenido_files
            for elemento in range(len(contenido_files)):
                #print contenido_files[elemento]
                if contenido_files[elemento].find('.txt')!= -1:
                    aux.append(contenido_files[elemento])
            #print aux

            for file in range(len(aux)):
                path = ruta_archivo+'/'+aux[file]
                #print path
                inicio_read_file.main(path, dia_a)












inicio=Pos_Analisis_Resultados()
cont=0
inicio.main(cont)
#while cont>=191 and  cont <= 191:
	#inicio.main(cont)
	#cont+=1