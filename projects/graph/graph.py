"""
Simple graph implementation
"""
from util import Stack, Queue  # These may come in handy


class Graph:
    """Represent a graph as a dictionary of vertices mapping labels to edges."""

    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex_id):
        """
        Add a vertex to the graph.
        """
        self.vertices[vertex_id] = set()

    def add_edge(self, v1, v2):
        """
        Add a directed edge to the graph.
        """
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)
            # If not, raise an error
        else:
            raise IndexError('nonexistent vertex')

    def get_neighbors(self, vertex_id):
        """
        Get all neighbors (edges) of a vertex.
        """
        return self.vertices[vertex_id]

    def bft(self, starting_vertex):
        """
        Print each vertex in breadth-first order
        beginning from starting_vertex.
        """
        visited = set()
        queue = Queue()
        queue.enqueue(starting_vertex)
        while queue.size() > 0:
            curr_node = queue.dequeue()
            if curr_node not in visited:
                visited.add(curr_node)
                print(curr_node)
                # find the neighbors
                for neighbor in self.get_neighbors(curr_node):
                    # iterate over neighbors and add to call queue
                    queue.enqueue(neighbor)

    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        visited = set()
        stack = Stack()
        stack.push(starting_vertex)
        while stack.size() > 0:
            curr_node = stack.pop()
            if curr_node not in visited:
                visited.add(curr_node)
                print(curr_node)
                # find the neighbors
                for neighbor in self.get_neighbors(curr_node):
                    # iterate over neighbors and add to call queue
                    stack.push(neighbor)

    def dft_recursive(self, vertex, visited=set()):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.

        This should be done using recursion.

        Need a base case
        Needs to call itself
        """
        if vertex not in visited:
            print(vertex)
            visited.add(vertex)

            neighbors = self.get_neighbors(vertex)
            if len(neighbors) == 0:
                return
            else:
                for neighbor in neighbors:
                    self.dft_recursive(neighbor, visited)

    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.

        Enqueue PATH"[]" to starting node, instead of just starting node
        """
        queue = Queue()
        visited = set()
        # path to starting vertex is enqueue
        queue.enqueue([starting_vertex])
        # loop while que is not empty
        while queue.size() > 0:
            # dequeue our current path
            current_path = queue.dequeue()
            # current node is always last in that path
            current_node = current_path[-1]
            # check if we have found our target node
            if current_node == destination_vertex:
                # then we are done! return
                return current_path
            # check if we've yet visited
            if current_node not in visited:
                ## if not, we go to the node
                ### mark as visited == add to visited set
                visited.add(current_node)
                ### get the neighbors
                neighbors = self.get_neighbors(current_node)
                ### iterate over the neighbors, enqueue the path to them
                for neighbor in neighbors:
                    # create copy of current path and add to new path to node
                    # new_path = list(current_path)
                    # new_path.append(neighbor)
                    # queue.append(new_path)
                    path_copy = current_path + [neighbor]
                    # enqueue that copy
                    queue.enqueue(path_copy)

    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.

        Will not be the shortest path
        """
        stack = Stack()
        visited = set()
        # path to starting vertex is enqueue
        stack.push([starting_vertex])
        # loop while que is not empty
        while stack.size() > 0:
            # dequeue our current path
            current_path = stack.pop()
            # current node is always last in that path
            current_node = current_path[-1]
            # check if we have found our target node
            if current_node == destination_vertex:
                # then we are done! return
                return current_path
            # check if we've yet visited
            if current_node not in visited:
                ## if not, we go to the node
                ### mark as visited == add to visited set
                visited.add(current_node)
                ### get the neighbors
                neighbors = self.get_neighbors(current_node)
                ### iterate over the neighbors, enqueue the path to them
                for neighbor in neighbors:
                    # create copy of current path and add to new path to node
                    path_copy = current_path + [neighbor]
                    # enqueue that copy
                    stack.push(path_copy)

    def dfs_recursive(self, starting_vertex, destination_vertex, path=[], visited=set()):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.

        This should be done using recursion.
        """
        if len(path) == 0:
            path.append(starting_vertex)

        if starting_vertex == destination_vertex:
            return path
        if starting_vertex not in visited:
            visited.add(starting_vertex)

            neighbors = self.get_neighbors(starting_vertex)

            for neighbor in neighbors:
                path_copy = path + [neighbor]

                result = self.dfs_recursive(neighbor, destination_vertex, path_copy)
                if result is not None:
                    return result


if __name__ == '__main__':
    graph = Graph()  # Instantiate your graph
    # https://github.com/LambdaSchool/Graphs/blob/master/objectives/breadth-first-search/img/bfs-visit-order.png
    graph.add_vertex(1)
    graph.add_vertex(2)
    graph.add_vertex(3)
    graph.add_vertex(4)
    graph.add_vertex(5)
    graph.add_vertex(6)
    graph.add_vertex(7)
    graph.add_edge(5, 3)
    graph.add_edge(6, 3)
    graph.add_edge(7, 1)
    graph.add_edge(4, 7)
    graph.add_edge(1, 2)
    graph.add_edge(7, 6)
    graph.add_edge(2, 4)
    graph.add_edge(3, 5)
    graph.add_edge(2, 3)
    graph.add_edge(4, 6)

    '''
    Should print:
        {1: {2}, 2: {3, 4}, 3: {5}, 4: {6, 7}, 5: {3}, 6: {3}, 7: {1, 6}}
    '''
    print(graph.vertices)

    '''
    Valid BFT paths:
        1, 2, 3, 4, 5, 6, 7
        1, 2, 3, 4, 5, 7, 6
        1, 2, 3, 4, 6, 7, 5
        1, 2, 3, 4, 6, 5, 7
        1, 2, 3, 4, 7, 6, 5
        1, 2, 3, 4, 7, 5, 6
        1, 2, 4, 3, 5, 6, 7
        1, 2, 4, 3, 5, 7, 6
        1, 2, 4, 3, 6, 7, 5
        1, 2, 4, 3, 6, 5, 7
        1, 2, 4, 3, 7, 6, 5
        1, 2, 4, 3, 7, 5, 6
    '''
    graph.bft(1)

    '''
    Valid DFT paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    graph.dft(1)
    graph.dft_recursive(1)

    '''
    Valid BFS path:
        [1, 2, 4, 6]
    '''
    print(graph.bfs(1, 6))

    '''
    Valid DFS paths:
        [1, 2, 4, 6]
        [1, 2, 4, 7, 6]
    '''
    print(graph.dfs(1, 6))
    print(graph.dfs_recursive(1, 6))
