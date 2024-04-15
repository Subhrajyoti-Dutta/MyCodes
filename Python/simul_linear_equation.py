import numpy as np
import fractions
import tool

foo = lambda x : round(x)

#works only when coeff are int

coeff=[
    [0,1,1],
    [0,1,-1],
    [1,1,1]
]

const=[
    [-1],
    [-5],
    [0]
]

np_coeff=np.array(coeff)
np_const=np.array(const)

det_np_coeff=foo(np.linalg.det(np_coeff))                                   #calculated the determinant of original matrix

inv_np_coeff=np.linalg.inv(np_coeff)                                        #calculated the inverse
res=np.matmul(inv_np_coeff,np_const)                                        #multiplied the inverse and constants

res2 = tool.map_numpy(foo,res)                                              #removed fractional part

ans=input("Do you want det and answer together? [y,n]: ")
if ans=="y" or ans=="Y":
    res3 = det_np_coeff*res2                                                #multiplied with det so that it removes decimals
    print("1/|A| = 1/",det_np_coeff,"\n",res3)

else:
    foo2 = lambda x : fractions.Fraction(x,det_np_coeff)
    res3 = tool.map_numpy(foo2,det_np_coeff*res2)                           #converted the values to fraction
    res4 = tool.map_numpy(tool.frac,res3)                                   #converted the values to string of fraction

    print(res4)