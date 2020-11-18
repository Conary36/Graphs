# Write a function that takes a 2D binary array and returns the number of 1 islands. An island consists of 1s that are connected to the north, south, east or west. For example:
islands = [[0, 1, 0, 1, 0],
           [1, 1, 0, 1, 1],
           [0, 0, 1, 0, 0],
           [1, 0, 1, 0, 0],
           [1, 1, 0, 0, 0]]


# get neighbors goes here
def getNeighbors(row, col, matrix):
    # check north, east, south, west
    # neighbors are like.. index - 1[same place], index[-1 place], index[+1 place], index + 1[same place]
    # What about the edges of the matrix?
    # check if these are 1s

    neighbors = []

    if col >= 1:
        west_neighbor = matrix[row][col - 1]
        if west_neighbor == 1:
            neighbors.append((row, col - 1))

    if col <= len(matrix) - 2:
        east_neighbor = matrix[row][col + 1]
        if east_neighbor == 1:
            neighbors.append((row, col + 1))

    if row <= len(matrix) - 2:
        south_neighbor = matrix[row + 1][col]
        if south_neighbor == 1:
            neighbors.append((row + 1, col))

    if row >= 1:
        north_neighbor = matrix[row - 1][col]
        if north_neighbor == 1:
            neighbors.append((row - 1, col))

    return neighbors


# traversal goes here
def dft_recursive(row, col, visited, matrix):
    if (row, col) not in visited:
        visited.add((row, col))

        neighbors = getNeighbors(row, col, matrix)

        for neighbor in neighbors:
            dft_recursive(neighbor[0], neighbor[1], visited, matrix)


# count number of connected components
def count_islands(matrix):
    visited = set()
    # If 0 continue, If 1: hold place, traverse and add each to visited, at end back

    number_of_connected_components = 0

    # Iterate over matrix
    for row in range(len(matrix)):
        for col in range(len(matrix)):
            node = matrix[row][col]
            # If 0 continue
            if node == 0:
                continue
            # If 1: hold place, traverse and add each to visited, at end go back
            elif node == 1:
                if (row, col) not in visited:
                    number_of_connected_components += 1
                    dft_recursive(row, col, visited, matrix)

    return number_of_connected_components


print(count_islands(islands))  # returns 4
