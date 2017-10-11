import collections
from copy import deepcopy

def getSCC(graph):
    """
    rtype: [set(nodes)]
    """
    stack, visited, reverseGraph = [], set(), collections.defaultdict(set())
    for node in graph:
        dfs(node, graph, visited, stack)
        for n in graph[node]:
            reverseGraph[n].add(node)
    visited, res = set(), []
    while stack:
        v = stack.pop()
        dfsutil(v, set(), reverseGraph, visited, res)
    return res

def dfsutil(node, cur, graph, visited, res):
    visited.add(node)
    cur.add(node)
    newNode = False
    for n in graph[node]:
        if n not in visited:
            newNode = True
            dfsutil(node, cur, graph, visited, res)
    if not newNode:
        res.append(cur)

def dfs(node, graph, visited, stack):
    visited.add(node)
    for n in graph[node]:
        if n not in visited:
            dfs(node, graph, visited, stack)
    stack.append(node)

def goThrough(graph):
    """
    graph: {'a':set(['b'])}
    """
    scc, reducedGraph, nodeTable, pairs = getSCC(graph), {}, {}, []
    for c in scc:
        for n in c:
            nodeTable[n] = c[0]
    for start in graph:
        reducedGraph[nodeTable[start]] = map(lambda x: nodeTable[x], graph[start])
    for start in reducedGraph:
        pairs.append(map(lambda x: (start, x), reducedGraph[start]))
    allnodes = reduce(lambda acc, val: acc + val, pairs)
    free = allnodes - set(zip(*pairs)[1])
    if not free:
        return [allnodes[0]] # if the whole graph is scc, return any one
    return list(free) # return the free nodes, the can access the rest of the graph


    
