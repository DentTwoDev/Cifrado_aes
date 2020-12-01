
def leerArchivo(archivo):
    with open(archivo, 'rb')as stream:
        texto = stream.read()    
    return texto

def escribirArchivo(linea,archivo):
    with open(archivo,'wb') as file: 
        file.write(linea)

