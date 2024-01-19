class Piramide:
    def __init__(self):
        pass

    def imprimir_mitad_derecha(self, altura):
        for i in range(altura + 1):
            # Imprimir espacios en blanco
            for _ in range(i):
                print('*', end=' ')
            print()

def main():
    piramide = Piramide()
    altura = int(input("Ingrese la altura de la mitad derecha de la pirámide: "))
    if altura > 0:
        piramide.imprimir_mitad_derecha(altura)

if __name__ == "__main__":
    main()
