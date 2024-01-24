import math

f = lambda x: x*math.exp(x)-1

a = 0
b = 1

round_lim = 3

fa = round(f(a),round_lim)
fb = round(f(b),round_lim)

assert a < b
increasing = (fa < fb)
print(f"x0 = {a}")
print(f"f0 = {fa}\n")
print(f"x1 = {b}")
print(f"f1 = {fb}\n")

for i in range(2,15):
    c = round((a+b)/2,round_lim)
    fc = f(c)
    if fc > 0:
        if increasing:
            b = c
        else:
            a = c
    else:
        if increasing:
            a = c
        else:
            b = c
    print(f"x{i} = {c}")
    fa, fb = fb, round(fc,round_lim)
    print(f"f{i} = {fb}\n")
    if fb == 0 or a==b: 
        break