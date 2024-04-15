import numpy as np
import fractions

def map_numpy(func,np_array):
    func_vec=_func_vec_numpy(func)
    res=func_vec(np_array)
    return res

def _func_vec_numpy(func):
    return np.vectorize(func)

def frac(x):
    if x.numerator == 0:
        return"0"
    return f"{x.numerator}/{x.denominator}"


if __name__=="__main__":
    arr=[[1,2,3,4],[5,6,7,8]]
    a=np.array(arr)
    pi=3.1415926
    foo = lambda x : pi**x

    b=map_numpy(foo,a)

    print(foo(a))