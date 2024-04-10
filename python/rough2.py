a = """    def prims(a_list):
        inf = 1 + max([d for u in a_list.keys()
                for (v, d) in a_list[u]])

    visited = {}; distance = {}; nbr = {}

    for v in a_list.keys():
        visited[v] = False
        distance[v] = inf
        nbr[v] = -1

    visited[1] = True

    for (v,d) in a_list[1]:
        distance[v] = d
        nbr[v] = 1

    for i in range(1, len(a_list.keys())):
        next_d = min([distance[v] for v in a_list.keys()
                      if not visited[v]])
        next_vlist = [v for v in a_list.keys()
                      if (not visited[v] and distance[v] == next_d)]

        next_v = min(next_vlist)

        visited[next_v] = True

        for (v,d) in a_list[next_v]:
            if not visited[v]:
                if d <= distance[v]:
                    distance[v] = d
                    nbr[v] = next_v

    connected = True
    TE = []

    for u in nbr.keys():
        if u != 1:
            if nbr[u] == -1:
                connected = False
                break
            else:
                TE.append((nbr[u], u))

    if not connected:
        print("The given graph is not connected.")
    else:
        print("The edges of the MST are:")

        for e in TE:
            print(e)

        cost = sum([d for u in a_list.keys()
                    for (v,d) in a_list[u]
                    if v == nbr[u]])

        print("Minimum Cost is ", cost)"""

print("\n".join(map(lambda x : x[4:],a.split("\n"))))