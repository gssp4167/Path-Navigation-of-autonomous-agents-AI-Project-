from pyswip import Prolog
prolog = Prolog()
prolog.consult("code.pl")
edge=list(prolog.query("edge(P1,P2,P3)"))
heuristic_list=list(prolog.query("h(P1,P2)"))


def aStarAlgo(start_node, stop_node):
    open_set = set(start_node)
    closed_set = set()
    g = {}
    cost = 0
    parents = {}
    g[start_node] = 0
    parents[start_node] = start_node

    while len(open_set) > 0:
        n = None
        for v in open_set:
            if n == None or g[v] + heuristic(v) < g[n] + heuristic(n):
                n = v

        if n == stop_node or Graph_nodes[n] == None:
            pass
        else:
            for (m, weight) in get_neighbors(n):
                if m not in open_set and m not in closed_set:
                    open_set.add(m)
                    parents[m] = n
                    g[m] = g[n] + weight


                else:
                    if g[m] > g[n] + weight:
                        g[m] = g[n] + weight
                        parents[m] = n

                        if m in closed_set:
                            closed_set.remove(m)
                            open_set.add(m)

        if n == None:
            print('Path does not exist!')
            return None

        if n == stop_node:
            path = []

            while parents[n] != n:
                path.append(n)
                n = parents[n]

            path.append(start_node)

            path.reverse()

            print(f'Your minimum cost path is : {path}')
            return path
        open_set.remove(n)
        closed_set.add(n)

    print('Path does not exist!')
    return None


def get_neighbors(v):
    if v in Graph_nodes:
        return Graph_nodes[v]
    else:
        return None

def heuristic(n):
    H_dist = {}
    for i in range(len(heuristic_list)):
        k=list(heuristic_list[i].values())
        H_dist[k[0]]=k[1]
    # print(H_dist)
    return H_dist[n]

Graph_nodes={
    'A':[],
    'B':[],
    'C':[],
    'D':[],
    'E':[],
    'F':[],
    'G':[],
    'H':[],
    'I':[],
    'L':[],
    'M':[],
    'N':[],
    'O':[],
    'P':[],
    'R':[],
    'S':[],
    'T':[],
    'U':[],
    'V':[],
    'Z':[]
}

g2 = list(Graph_nodes.keys())
c2 = []
for i in range(len(edge)):
    c2 = tuple(edge[i].values())
    for j in range(len(g2)):
        if(c2[0]==g2[j]):
            Graph_nodes[g2[j]].append((c2[1], c2[2]))




sum=0
print("\n")
print("Welcome to Romania\n")
Source=input("Enter the first alphabet in capital of your source: ")
Destination=input("Enter the first alphabet in capital of your destination: ")
if Source in Graph_nodes and Destination in Graph_nodes:
     path=aStarAlgo(Source,Destination)
else:
    print("Entered Source or Destination doesn't exist please check!")
# print(edge)
# print(Graph_nodes)
# print(heuristic_list)
# print(heuristic('A'))