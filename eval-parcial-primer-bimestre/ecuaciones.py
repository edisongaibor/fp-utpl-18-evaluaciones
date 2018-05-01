a=0
b=0
x=0
y=0
c=0
d=0
e=0
f=0
print("Ingrese el valor de a")
a=input()
print("Ingrese el valor de x")
x=input()
print("Ingrese el valor de b")
b=input()
print("Ingrese el valor de y")
y=input()
print("Ingrese el valor de d")
d=input()
print("Ingrese el valor de e")
e=input()

c=a*x+b*y
f=d*x+e*y

x=(c*e-b*f)/(a*e-b*d)
y=(c*e-b*f)/(a*e-b*d)

print("El valor de x es de:"+x)
print("El valor de y es de:"+y)


