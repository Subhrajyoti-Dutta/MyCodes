import numpy as np
a = np.array([
    ['#','*','*','*','*'],
    ['#','#','*','*','*'],
    ['#','#','*','#','*'],
    ['#','#','#','#','*'],
    ['#','#','#','#','#']
])


# print((a == '#').sum(axis = 0))

# for i in range(5):
#     print('#'*i + "*"*(5-i))

a = """#####
.####
.####
.####
.#.#.
.#...
....."""
b = [a[i::6] for i in range(5)]
d = dict()
for i in range(6):
    d['#' + '#'*i + "."*(5-i) + '.'] = i

# print(d)
e=[]
for i in range(5):
    e.append(d[b[i]])
print(e)