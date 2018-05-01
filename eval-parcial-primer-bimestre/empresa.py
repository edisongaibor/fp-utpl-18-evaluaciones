sueldo=360.40
ventas=0
porcentaje=0
totalsueldo=0
print("Ingrese el valor de ventas del empleado")
ventas=input()

if(ventas<=500):
	porcentaje=500*0.05
if(ventas>500 && ventas<=1000):
	porcentaje=1000*0.08
if(ventas>1000 && ventas<=5000):
	porcentaje=5000*0.10
if(ventas>5000):
	porcentaje=5000*0.15

totalsueldo=sueldo+porcentaje

print("El valor total del empleado es de:"+totalsueldo)