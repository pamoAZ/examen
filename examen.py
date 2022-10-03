from math import sqrt
import matplotlib.pyplot as plt
import numpy as np 
from mpl_toolkits.mplot3d import Axes3D
#Bloque donde se ingresan los datos 
v_1x =float(input("ingrese la componente del vector1 en x: "))
v_1y =float(input("ingrese la componente del vector1 en y: "))
v_1z =float(input("ingrese la componente del vector1 en z: "))
v_2x =float(input("ingrese la componente del vector2 en x: "))
v_2y =float(input("ingrese la componente del vector2 en y: "))
v_2z =float(input("ingrese la componente del vector2 en z: "))
v_3x =float(input("ingrese la componente del vector3 en x: "))
v_3y =float(input("ingrese la componente del vector3 en y: "))
v_3z =float(input("ingrese la componente del vector3 en z: "))
m=int(input("ingrese la masa"))
#se llenan los vectores 
#Vectores 
Vector0=Vector()
Vector1=Vector(v_1x, v_1y, v_1z)
Vector2=Vector(v_2x, v_2y, v_2z)
Vector3=Vector(v_3x, v_3y, v_3z)

#clase principal donde se tratan los datos, se define el objeto vector y sus metodos
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
    def ProductoPunto2(self, otro):
        pp = self.x*otro.x+self.y*otro.y+self.z*otro.z
        return(pp)
    def __str__(self):
        cadena = "("+str(self.x)+" , "+str(self.y)+" , "+str(self.z)+")"
        return(cadena)
    def Aceleracion(self, m):
        return(Vector(self.x/m, self.y/m, self.z/m))
    
    

#Operaciones de Vectores
Vector4=Vector1+Vector2
Vector5 = Vector4+Vector3
Vector6=Vector1-Vector2
Vector7 = Vector6 - Vector3
Norma1=Vector1.Norma(Vector0)
Norma2=Vector2.Norma(Vector0)
Norma3=Vector3.Norma(Vector0)
Vector8=Vector1.ProductoPunto(Vector2,Vector3)
PCV1V2r=Vector2.ProductoCruz(Vector3)
PCV1V2=Vector1.ProductoPunto2(PCV1V2r)
Vectoraceleracion = Vector5.Aceleracion(m)


#calculos de las cordenadas de posicion en funcion del tiempo 
#pasados un 60 segundos sigiendo la fomula del MRUA X_f = (at^2)/2
cordenadax = float(((Vectoraceleracion.x * (60)**2)/2))
cordenaday = float(((Vectoraceleracion.y * (60)**2)/2))
cordenadaz = float(((Vectoraceleracion.z * (60)**2)/2))

#mensaje de consola
print("cordenadas posicionales luego de 60 seguntos")
print(cordenadax,cordenaday,cordenadaz)
print("La suma de los vectores es ")
print("V1+V2+V3:", Vector5)
print("La resta de los vectores es ")
print("V1-V2-V3:", Vector7)
print(" la norma de cada vector es ")
print("Norma V1:", round(Norma1,2))
print("Norma V2:", round(Norma2,2))
print("Norma V3:", round(Norma3,2))
print("producto punto")
print("V1*V2*V3:",Vector8 )
print("producto vectorial")
print("V1*(V2XV3):", PCV1V2)
print("Vector aceleracion es ")
print("Aceleracion",Vectoraceleracion  )

#metodo que grafica 
def trazado_vectores_3d(ax,vectores,cordenadax,cordenaday,cordenadaz,**kwords):
        x_cor,y_cor,z_cor = zip(*vectores)
        ax.scatter(x_cor,y_cor,z_cor,**kwords)
        for v in vectores:
            x,y,z = v
            ax.plot([0,cordenadax],[0,cordenaday],[0,cordenadaz], color = "gray",linestyle="dotted",marker = ".")
        
subplot3d = plt.subplot(111,projection="3d")
trazado_vectores_3d(subplot3d,[r],cordenadax,cordenaday,cordenadaz,color=["r"])
subplot3d.set_zlim([0,cordenadaz])
plt.title("Grafica de la trayectoria de la particula")
plt.xlabel("X(s)", size = 10)
plt.ylabel("Y(s)", size = 8)
plt.show()

