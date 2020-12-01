from Crypto.Cipher import AES
import hashlib
import archivos

archivo = "hola.txt"
archivo_cif = "archivo_cifrado.aes"

contrasena = str(input("Ingrese contraseña: "))

print(len(contrasena)) #imprimimos el tamaño de bits de la variable
contrasena = contrasena.encode('ascii')
print(contrasena)
contrasena = contrasena.decode('ascii')
password = contrasena.encode() #codificamos la contraseña


#print(pas)
key = hashlib.sha256(password).digest()
mode = AES.MODE_CBC
IV = 'This is an IV456' #El vector de inicializacion debe ser aleatorio para cada nueva codificacion
#para esta ocacion esta predefinido.

def pad_message(message):
    while len(message)% 16 !=0:
        message = message + b" "
    return message
    

cipher = AES.new(key, mode, IV)

message = archivos.leerArchivo(archivo)
paded_message = pad_message(message)
print(paded_message)
print(len(paded_message))

encrypted_message = cipher.encrypt(paded_message)

print(encrypted_message)

archivos.escribirArchivo(encrypted_message, archivo_cif)
print(archivos.leerArchivo(archivo_cif))