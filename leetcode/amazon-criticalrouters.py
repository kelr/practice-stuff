from collections import defaultdict

# Create a dict of nodes that map to their neighbor nodes.
# If a node has only 1 neighbor, that neighbor is a critical node.
# For each critical node, if it iself has only 1 other neighbor then it is a critical node.
# O(E + N) time where E is number of edges and N is number of nodes
# O(EN) space, each node can be connected to every other node.
# This answer is wrong. Test case: [[0,1],[1,2],[2,0],[1,3],[3,4],[4,5],[5,3]]
# There is a possible critical node from nodes that dont only have 1 neighbor.
def numCritical(numNodes, numEdges, edges):
    # No nodes are technically critical if there are 2 or less nodes.
    if numNodes <= 2:
        return []

    nodeMap = defaultdict(list)
    for edge in edges:
        nodeMap[edge[0]].append(edge[1])
        nodeMap[edge[1]].append(edge[0])

    # If a node has only 1 neighbor, that neighbor is a critical node
    critical = []
    for node in nodeMap:
        if len(nodeMap[node]) == 1:
            newCritical = nodeMap[node][0]
            critical.append(newCritical)

            nodeMap[node].remove(newCritical)
            nodeMap[newCritical].remove(node)

    keepChecking = True
    # For each critical node, if it itself has only 1 other neighbor that node is a critical node.
    while keepChecking:
        keepChecking = False
        for node in critical:
            if len(nodeMap[node]) == 1:
                keepChecking = True
                newCritical = nodeMap[node][0]
                critical.append(newCritical)

                nodeMap[node].remove(newCritical)
                nodeMap[newCritical].remove(node)

    return critical



numNodes = 7
numEdges = 7
edges = [[0, 1], [0, 2], [1, 3], [2, 3], [2, 5], [5, 6], [3, 4]]

#print(numCritical(numNodes, numEdges, edges))

# O(E + N^2) time, where E is num edges and N is num nodes. E to build the graph, N^2 since there are N DFS of N each.
# O(E*N) space, E*N to store the graph + N-2 maximum critical nodes + N-1 maximum recursive calls on the stack.
def numCriticalDFS(numNodes, numEdges, edges):
    # No nodes are technically critical if there are 2 or less nodes.
    if numNodes <= 2:
        return []

    # Build the graph
    graph = defaultdict(list)
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)

    # Remove each node from the graph. DFS on the graph, if the number of nodes visited is not numNodes-1, that node was critical.
    critical = []
    for node in graph:
        root = 0
        if root == node:
            root = 1
        
        visited = set()
        dfs(root, root, node, visited, graph)
        if len(visited) != numNodes - 1:
            critical.append(node)
    return critical

def dfs(root, parent, removed, visited, graph):
    visited.add(root)
    for child in graph[root]:
        if child not in visited and child != parent and child != removed:
            dfs(child, root, removed, visited, graph)

numNodes = 6
numEdges = 7
#edges = [[0, 1], [0, 2], [1, 3], [2, 3], [2, 5], [5, 6], [3, 4]]
edges = [[0,1],[1,2],[2,0],[1,3],[3,4],[4,5],[5,3]]

print(numCriticalDFS(numNodes, numEdges, edges))