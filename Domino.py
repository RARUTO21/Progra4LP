#Tablero que se carga del txt, solo sirve para uno hasta el momento
class Tablero:
    def __init__(self):
        self.matriz=[]

    #Primero lo voy hacer para un solo tablero
    def llenarMatriz(self):
        archivo = open("datos.txt", "r")
        line=[]
        # lee todas las líneas del archivo, conserva saltos de línea
        for linea in archivo.readlines(): 
            partes = linea.split()
            self.matriz.append(partes)
        archivo.close()

    def mostrarMatriz(self):
        for i in range(7):
            print(self.matriz[i])
        print ("-----------")
        
    def getMatriz(self):
        return self.matriz
    
#Ficha con su numero y 2 pips
class Bone:
    def __init__(self, num, x, y):
        self.numero = num
        self.pip1 = x
        self.pip2 = y
        
#Lista con las 28 fichas de domino validas
class Fichas:
    def __init__(self):
        self.listaFichas =[]

    def cargarFichas(self):
        for i in range(7):
            self.listaFichas.append(Bone(i+1, 0, i))
        for i in range(6):
            self.listaFichas.append(Bone(i+8, 1, i+1))
        for i in range(5):
            self.listaFichas.append(Bone(i+14, 2, i+2))
        for i in range(4):
            self.listaFichas.append(Bone(i+19, 3, i+3))
        for i in range(3):
            self.listaFichas.append(Bone(i+23, 4, i+4))
        for i in range(2):
            self.listaFichas.append(Bone(i+26, 5, i+5))
        self.listaFichas.append(Bone(28, 6, 6))

    def mostrarFichas(self):
        for i in range(28):
            print(self.listaFichas[i].numero,
                  self.listaFichas[i].pip1, self.listaFichas[i].pip2)

                    

                                            
            
#Test
matriz=Tablero()
matriz.llenarMatriz()
matriz.mostrarMatriz()

f = Fichas()
f.cargarFichas()
f.mostrarFichas()
