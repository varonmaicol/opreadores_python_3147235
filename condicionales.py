'''
es una expresion que al ser evaluada 
da como resultado un valor verdadero o falso
Por tanto, en una condicional deben haber 
operaciones relacionales o logicos  
'''

#Ejemplo condicional 
a = 3 
b = 2
c = 1 
d = 4 
resultado = ((a + b )* c) ** 2 < 4 and (b + d) / 2 > 3
print (resultado)

resultado = not (a ** 2 - b > c ** 2 ) and ((a * 3 + c )/ 2 < d )or True
print (resultado) 

#Ejemplo condicional 
x = 5
y = 10 
z = 5 
resultado = (x == z + (8/z)) and not ((y + 3 ) * (4 / (z + 1 ))) == z 
print (resultado)

#Ejemplo condicional  
a = 6 
b = 3 
c = 7 
d = 4
e = 5 
resultado = not ( a + b > c / d ) or e * 2 != d + c and not (a < b ) 
print (resultado)
