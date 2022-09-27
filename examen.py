def Datos(): 

#Ingreso de datos


    Fuerza1=Fuerza(float(input("Inrese la componente en x de la fuerza 1: ")),
                   float(input("Inrese la componente en y de la fuerza 1: ")),
                   float(input("Inrese la componente en z de la fuerza 1: ")))
    Fuerza2=Fuerza(float(input("Inrese la componente en x de la fuerza 2: ")),
                   float(input("Inrese la componente en y de la fuerza 2: ")), 
                   float(input("Inrese la componente en z de la fuerza 2: ")))
    Fuerza3=Fuerza(float(input("Inrese la componente en x de la fuerza 3: ")), 
                   float(input("Inrese la componente en y de la fuerza 3: ")), 
                   float(input("Inrese la componente en z de la fuerza 3: ")))
    m=float(input("¿Cuál es la masa el objeto? "))
#Suma de las fuerzas
    Fuerza4=Fuerza1+Fuerza2+Fuerza3
#Imprimir
    print("")
    print("Los datos son:")
    print("La fuerza 1 es: ", Fuerza1)
    print("La fuerza 2 es: ", Fuerza2)
    print("La fuerza 3 es: ", Fuerza3)
    print("La superposición de las fuerzas sobre el objeto es: ", Fuerza4)
    print("La aceleración del objeto es: ", Fuerza4.Aceleracion(m))
#Objeto Fuerza
    
class Fuerza:
    def __init__(self, x=0, y=0, z=0):
        self.x=x
        self.y=y
        self.z=z
    def __add__(self, otro):
        suma = Fuerza(self.x+otro.x, self.y+otro.y, self.z+otro.z)
        return(suma)
    def __str__(self):
        return("({0} , {1} , {2})".format(self.x, self.y, self.z))
    def Aceleracion(self, m):
        return(Fuerza(self.x/m, self.y/m, self.z/m))
    
    
Datos()
