import math

f = lambda x: x**3 - 4*x -9

a = 2
b = 3

round_lim = 2

fa = round(f(a),round_lim+1)
fb = round(f(b),round_lim+1)

print(f"x0 = {a}")
print(f"f0 = {fa}\n")
print(f"x1 = {b}")
print(f"f1 = {fb}\n")

for i in range(2,15):
    c = round((a*fb - b*fa)/(fb-fa),3)
    print(f"x{i} = {c}")
    a, b = b, c
    fa, fb = fb, round(f(b),round_lim+1)
    print(f"f{i} = {fb}\n")
    if fb == 0 or a==b: 
        break