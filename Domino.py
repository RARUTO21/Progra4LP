
#Tablero que se carga del txt, solo sirve para uno hasta el momento
#Es una matriz de pips
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
            result=[]
            for x in partes:
                result.append(Pip(int(x)))
            self.matriz.append(result)
        archivo.close()

    def mostrarMatriz(self):
        for i in range(7):
            for j in range(8):
                print(self.matriz[i][j].getNum())
            print ("++++++++++")
        print ("-----------")
        
    def getMatriz(self):
        return self.matriz
    
#Ficha con su numero y 2 pips
class Bone:
    def __init__(self, num, x, y):
        self.numero = num
        self.pip1 = Pip(x)
        self.pip2 = Pip(y)
        self.repeticiones = 0
    def seRepite(self):
        self.repeticiones+=1
    def seDisminuye(self):
        self.repeticiones-=1
    def getRepeticiones(self):
        return self.repeticiones
    def getId(self):
        return self.numero
        
#Lista con las 28 fichas (Bones)de domino validas
#Los metodos son de la manera que lo estaba haciento antes (sin el grafo) ahora son diferentes fijo
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
        self.mostrarFichas()
        print("Fichas cargadas")

    #Lo usaba antes, cuando trate con una matriz
    def compara(self, num1, num2):
        for i in range(28):
            if ((self.listaFichas[i].pip1 == num1 and
                self.listaFichas[i].pip2 == num2)
                or (self.listaFichas[i].pip1 == num2 and
                self.listaFichas[i].pip2 == num1)):
                #Aumentar en 1 la cantidad de repeticiones
                self.listaFichas[i].seRepite()
                return( self.listaFichas[i].getId())
    #Lo usaba antes, cuando trate con una matriz
    def comparaSin(self, num1, num2):
        for i in range(28):
            if ((self.listaFichas[i].pip1 == num1 and
                self.listaFichas[i].pip2 == num2)
                or (self.listaFichas[i].pip1 == num2 and
                self.listaFichas[i].pip2 == num1)):
                return( self.listaFichas[i].getId())
            
    def cantRepeticiones(self, num):
        for i in range(28):
            if (self.listaFichas[i].getId() == num):
                return( self.listaFichas[i].getRepeticiones())
    def quitarRepeticion(self, num):
        for i in range(28):
            if (self.listaFichas[i].getId() == num):
                self.listaFichas[i].seDisminuye()
        
    def mostrarFichas(self):
        for i in range(28):
            print(self.listaFichas[i].numero,
                  self.listaFichas[i].pip1.getNum(), self.listaFichas[i].pip2.getNum())
#Esta clase es para hacer el mapa de bones, es que antes lo hacia de otra manera pero ya es diferente por el grafo entonces
#borrè algunos metodos
#Esta clase hay que ajustarla a lo que hagamos con el grafo, yo la usaba antes asi para la matriz(primera vez que intente
class Mapa:
    def __init__(self):
        self.mapa = []
        self.mapaFinal = []
    
    def cargarMapaH(self, l):
        n = 7
        splited = []
        len_l = len(l)
        for i in range(n):
            start = int(i*len_l/n)
            end = int((i+1)*len_l/n)
            self.mapa.append(l[start:end])
        #print(self.mapa)
        self.mostrar()
        print("El final")
        self.cargarMapaFinal()
    
    def cargarMapaFinal(self):
        for i in range(7):
            self.mapaFinal.append([])
            for j in range(8):
                self.mapaFinal[i].append(0)
        self.mostrarFinal()
        
    def mostrar(self):
        for x in range(len(self.mapa)):
            print(self.mapa[x])
    def mostrarFinal(self):
        for x in range(len(self.mapaFinal)):
            print(self.mapaFinal[x])
                         
class Pip:
    def __init__(self, n):
        self.num = n
        self.usado = 0
    #Uso 0 para no visitado y 1 para visitado, se me fue usar booleanos jaja
    def setUsado(self):
        self.usado=1
        
    def getNum(self):
        return self.num
    
    def getUsado(self):
        return self.usado
        
        
class Grafo:
    def __init__(self):
        self.dic = {}
        
    def vertices(self):
        return list(self.dic.keys())
    
    def edges(self):
        return self.generateEdges()
    
    def addVertice(self, vertex):
        if vertex not in self.dic:
            self.dic[vertex] = []
            

    def generateEdges(self):
        edges = []
        for vertex in self.dic:
            for sgt in self.dic[vertex]:
                if {sgt, vertex} not in edges:
                    edges.append({vertex, sgt})
        return edges

            
    def toStr(self):
        print(self.dic)
        for key in self.dic:
            if (key.getUsado==1):
                print (key.getnum())

    def agregar(self, grafo, ele):
        grafo.dic.update({ele:[]})
        
    #estaba probando algun recorido
    def profundidadPrimero(self, grafo):
        elementosRecorridos = []
        for p in grafo.dic:
            if (p.getUsado() == 0):
                l=[]
                if p in elementosRecorridos:
                    break
                else:
                    for x in grafo.dic[p]:
                        x.setUsado()
                        l.append(x.getNum())
                    
                    print(p.getNum(), " tiene pips: ",l)

                    print("")
                    elementosRecorridos.append(p)
            else:
                print(p.getNum(), " ya se uso")
                                
    def devuelve(self, grafo, num):
        for pip in grafo.relaciones:
            if( grafo.relaciones[p].getNum() == num):
                return grafo.relaciones[p][0].self()
            
    def relacionar(self, grafo, ele1, ele2):
        grafo.relacionarUnilateral(grafo, ele1,ele2)
        
    def relacionarUnilateral(self, grafo, origen, destino):
        #Siempre va a estar
        if origen in self.dic:
            grafo.dic[origen].append(destino)
    #Carg el grafo con los nodos y las conexiones con otros nodos
    #las conexiones son una lista EG 6:[6,1]
    #el 6 de la lista es el nodo siguiente y 1 es el de abajo 
    #IMPORTANTE: el 6 y el 1 son el mismo objeto que el nodo
    def cargar(self, grafo, matriz):
        for i in range(7): #de 0 a 6 FILAS
            for j in range(8):#de 0 a 7 COLUMNAS
                if(i!=6):
                    if (j!=7):
                        pip = matriz[i][j]
                        pipSgt= matriz[i][j+1]
                        pipAbajo=matriz[i+1][j]
                        self.agregar(grafo, pip)
                        self.agregar(grafo, pipSgt)
                        self.agregar(grafo, pipAbajo)
                        self.relacionar(grafo, pip, pipSgt)
                        self.relacionar(grafo, pip, pipAbajo)
                    else:
                        pip = matriz[i][j]
                        pipAbajo=matriz[i+1][j]
                        self.agregar(grafo, pip)
                        self.agregar(grafo, pipAbajo)
                        self.relacionar(grafo, pip, pipAbajo)
                else:
                    if( j!=7):
                        pip = matriz[i][j]
                        self.agregar(grafo, pip)
                        pipSgt= matriz[i][j+1]
                        self.relacionar(grafo, pip, pipSgt)
                    else:
                        pip = matriz[i][j]
                        self.agregar(grafo, pip)
    #Es solo para mostrar el nodo y las conexiones que tiene en las conexiones se tiene el mismo objeto que en el nodo
    def mostrarConexiones(self, grafo):
        elementosRecorridos = []
        for p in grafo.dic:
            if (p.getUsado() == 0):
                l=[]
                if p in elementosRecorridos:
                    break
                else:
                    for x in grafo.dic[p]:
                        #Pense que este era como un checkpoint
                        #o condicion pero NO
                        #if(x.getNum() == p.getNum()):
                            #x.setUsado() asi se dice si un nodo ya se visito
                        l.append(x.getNum())
                    print(p.getNum(), " tiene pips: ",l)
                    print("")
                    elementosRecorridos.append(p)
            else:
                print(p.getNum(), " ya se uso")

                    
     #Falta hacer el backtracking. no hay soluciones si el bone siguiente y abajo ya fueron usados, entonces buscar otra ruta
     #La idea es poder deshacer y rehacer
        
    
#Test
matriz=Tablero()
matriz.llenarMatriz()
#matriz.mostrarMatriz()



f = Fichas()
f.cargarFichas()

mapa = Mapa()
#mapa.bonesHorizontal(matriz.getMatriz(), f)
print("------------------------------")
#mapa.backTrackingCopia(matriz.getMatriz(), f)
#mapa.bonesVertical(matriz.getMatriz(), f)
grafo = Grafo()
grafo.cargar(grafo, matriz.getMatriz())
grafo.mostrarConexiones(grafo)
