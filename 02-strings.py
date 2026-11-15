texto = "Hola Mundo"
         
print(texto)
print(texto.upper())
print(texto.lower())
print(texto.find("Mun"))
print(texto.find("Ho"))
print(texto.replace("Mundo", "Karla"))
nuevoTexto = texto.replace("Mundo", "Karla")
print (texto, nuevoTexto)
print(texto.startswith("Hola"))
print(texto.endswith("Mundo"))
print ("Mundo" in texto)
print ("Karla" in nuevoTexto)