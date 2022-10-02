from math import sqrt
m=10
class Vector:
    def __init__(self, x=0, y=0, z=0):
        self.x=x
        self.y=y
        self.z=z
    def __add__(self, otro,):
        suma = Vector((self.x+otro.x), (self.y+otro.y), (self.z+otro.z))
        return(suma)
    def __sub__(self, otro):
        resta = Vector(self.x-otro.x, self.y-otro.y, self.z-otro.z)
        return(resta)
    def Norma(self, otro):
        r = sqrt((self.x-otro.x)**2+(self.y-otro.y)**2+(self.z-otro.z)**2)
        return(r)
    def ProductoPunto(self, otro,otroo):
        pp = self.x*otro.x*otroo.x+self.y*otro.y*otroo.y+self.z*otro.z*otroo.z
        return(pp)
    def ProductoCruz(self, otro):
        PC = Vector((self.y*otro.z)-(otro.y*self.z), (otro.x*self.z)-(self.x*otro.z), 
                    (self.x*otro.y-otro.x*self.y))
        return(PC)
    def __str__(self):
        cadena = "("+str(self.x)+" , "+str(self.y)+" , "+str(self.z)+")"
        return(cadena)
    def Aceleracion(self, m):
        return(Vector(self.x/m, self.y/m, self.z/m))
    
#Bloque Principal
#Vectores 
Vector0=Vector()
Vector1=Vector(-1, 2, 3)
Vector2=Vector(5, 2, -2)
Vector3=Vector(2, 2, -2)

#Operaciones de Vectores
Vector4=Vector1+Vector2
Vector5 = Vector4+Vector3
Vector6=Vector1-Vector2
Vector7 = Vector6 - Vector3
Norma1=Vector1.Norma(Vector0)
Norma2=Vector2.Norma(Vector0)
Norma3=Vector3.Norma(Vector0)
Vector8=Vector1.ProductoPunto(Vector2,Vector3)
#Vector9=Vector8.ProductoPunto(Vector3)
PCV1V2=Vector1.ProductoCruz(Vector2)
Vectoraceleracion = Vector5.Aceleracion(m)
#Imprimir
print("V1+V2+V3:", Vector5)
print("V1-V2-V3:", Vector7)
print("Norma V1:", round(Norma1,2))
print("Norma V2:", round(Norma2,2))
print("Norma V3:", round(Norma3,2))
print("V1*V2*V3:",Vector8 )
print("V1xV2:", PCV1V2)
print("Aceleracion",Vectoraceleracion  )