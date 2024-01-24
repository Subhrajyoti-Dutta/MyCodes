import numpy as np
import fractions
import tool
a=[
    [3,0,2],
    [2,0,-2],
    [0,1,1]
]

np_a=np.array(a)

inv_np_a = np.linalg.inv(np_a)

det_np_a = round(np.linalg.det(np_a),5)

print("Warning: All elements should be int")
ans=input("Do you want det and answer together? [y,n]: ")
if ans=="y" or ans=="Y":
    print("1/|A| = 1/",det_np_a,"\n",det_np_a*inv_np_a)

else:
    foo2 = lambda x : fractions.Fraction(int(x),int(det_np_a))
    ans = tool.map_numpy(foo2,det_np_a*inv_np_a)
    ans2 = tool.map_numpy(tool.frac,ans)
    print(ans2)