'''
Practicas parcial 1
'''

import os

class reorden:
  
    
    #declaracions de constructor
    def __init__(self):
         print("Colocaremos 10 numeros")
         self.lista1=[]
         i =0
         while i < 10:
            print("Dame el valor {} ".format(i+1))
            num1= int(input())
            self.lista1.append(num1)
        
            i+=1
    #declaracion de metodos de clase
    def paresImpares(self):
        lista2= []
        lista3= []
        listaExistentes= []
        for i in self.lista1:
            if i % 2 == 0 and i not in lista2 and i not in lista3:
                lista2.append(i)
                
            elif i not in lista3 and i not in lista2:
                lista3.append(i)
                
            elif i not in listaExistentes:
                listaExistentes.append(i)
        frecuencia_numeros = {num: self.lista1.count(num) for num in set(listaExistentes)}
        lista2.sort()      
        lista3.sort()    
        print("La lista original es {}".format(self.lista1))   
        print("La lista de pares es: {}".format(lista2))
        print("La lista de impares es: {}".format(lista3)) 
        print("La lista de numeros repetidos es  {}".format(frecuencia_numeros))
        
    def reordenamiento(self):
        listaOrdenada = []
        listaExistentes= []
        for i in self.lista1:
            if i not in listaOrdenada:
                listaOrdenada.append(i)
            else:
                listaExistentes.append(i)
                
        print("La lista original es: ", self.lista1)  
                 
        frecuencia_numeros = {num: self.lista1.count(num) for num in set(listaExistentes)}
        print("la frecuencia de numeros repetidos es: ",frecuencia_numeros)
             
        listaOrdenada.sort()
        print("La lista ordenada es: ",listaOrdenada)
        
        
        
        
             
             
def main():
    #Linea para limpiar la terminal
    os.system('cls')
    claseAEjecutar=reorden()
    claseAEjecutar.paresImpares()
    
    claseAEjecutar.reordenamiento()
if __name__ == "__main__":
    main()
    
