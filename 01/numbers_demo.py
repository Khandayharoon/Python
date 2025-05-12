import math
from decimal import Decimal

import random
x=3
y=4
z=5
print("checking compersion", x<y<z)
print("sum" ,x+y)
print("Multiple" , x*y*z)
print("Divide", y%x)
print("modulus", y/x)

print("Decimal", Decimal('1.2')+Decimal('2.5') )
print(math.floor(4.56))
print(math.floor(-4.56))
print(math.trunc(4.234))
print(math.trunc(-4.234))

print( 3==3)
print (3!=4)
randomNumber = random.randint(1,13)
print(randomNumber)

listOne = ["Harry", "Jhon" , "alex", "Lena","Johana"]
print(random.choice(listOne))
biar = int('101000000',2)
print(biar)
