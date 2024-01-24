import numpy as np


pt1=np.array(list(map(float,(input("Enter point 1 (without brackets): ")).split(","))))
pt2=np.array(list(map(float,(input("Enter point 2 (without brackets): ")).split(","))))

dpt=np.subtract(pt2,pt1)

sqr=np.power(dpt,2)
add=np.sum(sqr)
sqrrt=np.power(add,0.5)
print(sqrrt)

ans=(input("Enter Continue with ratio [Y/N]: "))
if (ans=="Y" or ans=="y"):
    rat=(input("Enter the ratio: ")).split(":")
    ratio=int(rat[0])/(int(rat[0])+int(rat[1]))
    a=tuple(pt1+dpt*ratio)

    print("The Desired point is: ",a)