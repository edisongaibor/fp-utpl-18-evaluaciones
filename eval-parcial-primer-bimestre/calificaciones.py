calificacion1=0
calificacion2=0
calificacion3=0
calificacion4=0
promedio=0

print("Ingrese el nombre y apellidos del estudainte")
nombre=input()
print("Ingrese la primera calificacion")
calificacion1=input()
print("Ingrese la segunda calificacion")
calificacion2=input()
print("Ingrese la tercera calificacion")
calificacion3=input()
print("Ingrese la cuarta calificacion")
calificacion4=input()

promedio=(calificacion1+calificacion2+calificacion3+calificacion4)/4

if(promedio>=90 && promedio<100):
	puntuacion="A"
if(promedio>=80 && promedio<=89):
	puntuacion="B"
if(promedio>=70 && promedio<=79):
	puntuacion="C"
if(promedio>=0 && promedio<=69):
	puntuacion+"D"

print("El estudaiente:"+nombre)
print("COn el promedio de calificaciones:"+promedio)
print("Tiene una puntuacion de:"+puntuacion)