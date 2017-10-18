#Lee el archivo y hace una matriz, cada fila es cada linea del archivo separada x espacios
def leer():
    archivo = open("datos.txt", "r")
    matriz=[]
    line=[]
    for linea in archivo.readlines(): # lee todas las líneas del archivo, conserva saltos de línea
        partes = linea.split()
        matriz.append(partes)
    archivo.close()
    for x in matriz:
        print(x)

class Bone:
    def __init__(self, num, x, y):
        self.numero = num
        self.pip1 = x
        self.pip2 = y

# No se si creamos la class Pip: o mejor una solo que sea BONE

        
    



