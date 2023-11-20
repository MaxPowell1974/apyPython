import requests
import json
import os

#def guardar_contenido_archivo(ubicacion, contenido):
#Variable: todo en minuscula seeparado por guiones bajos
#Objetos con Mayuscula CamelCase
#usar diccionario o vector para urls y variables en general

#funciòn getmovie que reciba argumentos y me devuelve el contenido
#dividir en main logica guardar y funciones 
#investigar reglas de escritura de python 
#investigar subirlo a Git
#Agregamos algo en Stagging

def valid_create(ruta):
        if not os.path.exists(ruta):
                head_tail = os.path.split(ruta) 
                os.makedirs(head_tail[0])        
        return True


def guardar_contenido_archivo(ubicacion, contenido):
    #Guardo el json obtenido en un archivo
        valid_create(ubicacion)
        t = open(ubicacion,"a+") 
        t.write(contenido)
        t.close()
        return True

def guardar_titulo_Search(rta, file):
        titulo = ""
        for rta  in rta['Search']:
                titulo = titulo + rta['Title'] + '\n'
        valid_create(file)
        f = open(file, "a+")
        f.write(titulo)
        f.close() 
        return True

def llamar_endpoint(d, ubicacion):
        for Key in d.keys():
            rtas[Key] = requests.get(d[Key])
            if rtas[Key].status_code ==200:
                    ls_pelis= json.dumps(rtas[Key].json(), indent=4)       
                    if (guardar_contenido_archivo(ubicacion,ls_pelis)):
                            print(r"grabo bien")


if __name__ == "__main__":

        d = {
        "urlTitu": os.environ.get("urlTitu"),
        "urlBusc": os.environ.get("urlBusc"),
        }

        rtas = {
                "urlTitu": '',
                "urlBusc": ''
        }

        

        file_Out = os.environ.get("file_Out")
        file_title_search = os.environ.get("file_title_search")

        #ejecuta EndPoint y guarda la respuesta
        llamar_endpoint(d, file_Out)
        
        #Filtramos solo los titulos y los guardamos en un archivo
        guardar_titulo_Search(rtas.get('urlBusc').json(), file_title_search)

