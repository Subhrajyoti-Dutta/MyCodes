import numpy as np
x1,y1,z1=tuple(map(float,(input("Enter point 1 (without brackets): ")).split(",")))
x2,y2,z2=tuple(map(float,(input("Enter point 2 (without brackets): ")).split(",")))

print("\n")

rat=((input("Enter the ratio: ")))
ratio=tuple(map(int,rat.split(":")))
print(ratio)

dist=((x1-x2)**2+(y1-y2)**2+(z1-z2)**2)**0.5

print("distance between the points are: ",dist)

def sec(a1,a2,ratio):
	rat1,rat2=ratio
	return np.divide((rat1*a2+rat2*a1),(rat1+rat2),dtype="float32")

print("The desired point is: (",
sec(x1,x2,ratio),",",
sec(y1,y2,ratio),",",
sec(z1,z2,ratio),")")