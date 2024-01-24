import math

f = lambda x: x**3 - 12
df = lambda x: 3*x**2

a1 = 2
a2 = 3

round_lim = 5

fa1 = round(f(a1),round_lim)
fa2 = round(f(a2),round_lim)

print(f"a1 = {a1}")
print(f"fa1 = {fa1}\n")
print(f"a2 = {a2}")
print(f"fa2 = {fa2}\n")

a = (a1 + a2) / 2
fa = round(f(a),round_lim)
dfa = round(df(a),round_lim)

print(f"x0 = {a}")
print(f"f0 = {fa}")
print(f"df0 = {dfa}\n")

for i in range(1,15):
    c = round(a - fa / df(a),round_lim)
    print(f"x{i} = {c}")
    fc = round(f(c),round_lim)
    dfc = round(df(c),round_lim)
    # fa, fb = fb, round(f(b),round_lim+1)
    print(f"f(x{i}) = {fc}")
    print(f"df(x{i}) = {dfc}\n")
    if fc == 0 or a==c: 
        break
    a, fa, dfa = c, fc, dfc