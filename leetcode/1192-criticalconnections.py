# O(E + E*N) time, where E is num edges and N is num nodes. E to build the graph, E edges to delete, each DFS visits N nodes.
# O(E*N) space, E*N to store the graph + E maximum critical nodes + N maximum recursive calls on the stack.
def criticalConnections(n, connections):
   # No nodes are technically critical if there are 2 or less nodes.
    if n <= 2:
        return []

    # Build the graph
    graph = defaultdict(list)
    for u, v in connections:
        graph[u].append(v)
        graph[v].append(u)

    critical = []
    for edge in connections:
        root = 0

        visited = set()
        dfs(root, root, edge, visited, graph)
        if len(visited) != n:
            critical.append(edge)
    return critical

def dfs(root, parent, removed, visited, graph):
    visited.add(root)
    for child in graph[root]:
        if child not in visited and child != parent:
            if ([root, child] != removed) and ([child, root] != removed):
                dfs(child, root, removed, visited, graph)

# Rank each node visited by DFS in increasing order. If a node
# encounters a child with a rank thats between 0 and the parent it's in a cycle.
# Discard each edge thats inside a cycle. The edges that are left are critical edges.
# See https://leetcode.com/problems/critical-connections-in-a-network/discuss/382638/DFS-detailed-explanation-O(orEor)-solution
# Also see: Tarjan's Algorithm
# O(E + V) time, DFS takes E+V time
# O(E + V) space, Graph takes E, rank takes E, connections takex E
def criticalConnections(n, connections):
    def makeGraph(connections):
        graph = collections.defaultdict(list)
        for conn in connections:
            graph[conn[0]].append(conn[1])
            graph[conn[1]].append(conn[0])
        return graph

    graph = makeGraph(connections)
    connections = set(map(tuple, (map(sorted, connections))))
    rank = [-2] * n

    def dfs(node, depth):
        if rank[node] >= 0:
            # visiting (0<=rank<n), or visited (rank=n)
            return rank[node]
        rank[node] = depth
        min_back_depth = n
        for neighbor in graph[node]:
            if rank[neighbor] == depth - 1:
                continue  # don't immmediately go back to parent. that's why i didn't choose -1 as the special value, in case depth==0.
            back_depth = dfs(neighbor, depth + 1)
            if back_depth <= depth:
                connections.discard(tuple(sorted((node, neighbor))))
            min_back_depth = min(min_back_depth, back_depth)
        rank[node] = n  # this line is not necessary. see the "brain teaser" section below
        return min_back_depth
        
    dfs(0, 0)  # since this is a connected graph, we don't have to loop over all nodes.
    return list(connections)