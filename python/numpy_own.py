def toposort(Alist):
    (indegree,toposortlist) =({},[])
    for u in Alist.keys():
        indegree[u] = 0
    for u in Alist.keys():
        for v in Alist[u]:
            indegree[v] += 1

    zerodegreeq = Queue()
    for u in Alist.keys():
        if indegree[u] == 0:
            zerodegreeq.addq(u)

    while (not zerodegreeq.isempty()):
        j = zerodegreeq.delq()
        toposortlist.append(j)
        indegree[j] -= 1
        for k in Alist[j]:
            indegree[k] -= 1
            if indegree[k] == 0:
                zerodegreeq.addq(k)
    return toposortlist

def longestpath(L,Alist):
    steps = {}
    for u in Alist.keys():
        steps[u] = 0

    for i in L:
        for j in Alist[i]:
            steps[j] = max(steps[i] + 1, steps[j])

    maxm = 0
    for i in step:
        if (step[i] > maxm):
            maxm = step[i]

    return maxm+1


d = {
    0:[],
    1:[],
    2:[5],
    3:[0],
    4:[0],
    5:[1,3],
    6:[5],
    7:[1,3,4,6]
}   

print(longestpath(toposort(d),d))