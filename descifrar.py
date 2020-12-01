from Crypto.Cipher import AES
import hashlib
import archivos

archivo_cif = "hola.txt"
archivo_des = "archivo_cifrado.aes"
archivo_descifrado = "archdescif.txt"

contrasena = str(input("Ingrese contraseña: "))
print(len(contrasena)) #imprimimos el tamaño de bits de la variable
password = contrasena.encode() #codificamos la contraseña
#print(pas)
key = hashlib.sha256(password).digest()
mode = AES.MODE_CBC
IV = 'This is an IV456' #El vector de inicializacion debe ser aleatorio para cada nueva codificacion
#para esta ocacion esta predefinido.

cipher = AES.new(key,mode,IV)

mensaje_encriptado = archivos.leerArchivo(archivo_des)
print(mensaje_encriptado)
message_decrypted = cipher.decrypt(mensaje_encriptado)
print(message_decrypted)
print(message_decrypted.decode('ascii'))

archivos.escribirArchivo(message_decrypted, archivo_descifrado)

