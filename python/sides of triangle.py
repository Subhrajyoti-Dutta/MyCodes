
A=tuple(map(float,(input("Enter point 1 (without brackets): ")).split(",")))
B=tuple(map(float,(input("Enter point 2 (without brackets): ")).split(",")))
C=tuple(map(float,(input("Enter point 3 (without brackets): ")).split(",")))

print("\n")

def distance(a,b):
    return ((a[0]-b[0])**2 + (a[1]-b[1])**2 + (a[2]-b[2])**2)**0.5


dist1=distance(A,B)
dist2=distance(B,C)
dist3=distance(A,C)


print(f"The Distance between A{A} and B{B} is: {dist1}")
print(f"The Distance between B{B} and C{C} is: {dist2}")
print(f"The Distance between C{C} and A{A} is: {dist3}")
