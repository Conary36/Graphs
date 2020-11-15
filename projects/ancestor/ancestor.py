def earliest_ancestor(ancestors, starting_node):
    '''
   Write a function that, given the dataset and the ID of an individual in the dataset, returns their earliest known
   ancestor – the one at the farthest distance from the input individual.If there is more than one ancestor tied
  for "earliest", return the one with the lowest numeric ID.If the input individual has no parents, the function
  should return -1.
  '''

    visited = []
    for i in get_parents(ancestors,starting_node):
        visited.append(i)
    while len(visited) > 0:
        node = visited.pop(0)
        for i in get_parents(ancestors,node):
            visited.append(i)
        if len(visited) == 0:
            return node

    return -1


def get_parents(dataset, children):
    parents = [node[0] for node in dataset if node[1] == children]
    parents.sort(reverse= True)
    return parents


'''
DFS(graph):
    for v of graph.verts:
        v.color = white
        v.parent = null

    for v of graph.verts:
        if v.color == white:
            DFS_visit(v)

DFS_visit(v):
    v.color = gray

    for neighbor of v.adjacent_nodes:
        if neighbor.color == white:
            neighbor.parent = v
            DFS_visit(neighbor)

    v.color = black


'''
