from io import open

class ManejadorArchivo:
    def __init__(self, nombre_archivo):
        self.nombre_archivo = nombre_archivo

    def insertar(self, palabra1, palabra2):
        with open(self.nombre_archivo, 'a') as archivo_texto:
            archivo_texto.write(f'{palabra1} - {palabra2}\n')

    def mostrar_contenido1(self, palabra):
        with open(self.nombre_archivo, 'r') as archivo_texto:
            for linea in archivo_texto.readlines():
                if palabra.lower() in linea:
                    palabras = linea.split(' - ')
                    if  palabra.lower()+'\n' == palabras[1].lower():
                        return palabras[0].rstrip()
                    else:
                        return 'Palabra no encontrada en el diccionario' 
        return 'Palabra no encontrada en el diccionario'  
                    
    def mostrar_contenido2(self, palabra):
        with open(self.nombre_archivo, 'r') as archivo_texto:
            for linea in archivo_texto.readlines():
                if palabra.lower() in linea:
                    palabras = linea.split(' - ')
                    if palabra.lower() == palabras[0].lower():
                        return palabras[1].rstrip()
                    
                    else:
                        return 'Palabra no encontrada'   
        return 'Palabra no encontrada en el diccionario'       
                                    
            
                    
                 


