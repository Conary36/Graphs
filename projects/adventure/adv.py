from room import Room
from player import Player
from world import World

import random
from ast import literal_eval



# Load world
world = World()

# You may uncomment the smaller graphs for development and testing purposes.
map_file = "maps/test_line.txt"
map_file = "maps/test_cross.txt"
map_file = "maps/test_loop.txt"
map_file = "maps/test_loop_fork.txt"
map_file = "maps/main_maze.txt"

# Loads the map into a dictionary
room_graph = literal_eval(open(map_file, "r").read())
world.load_graph(room_graph)

# Print an ASCII map
world.print_rooms()

player = Player(world.starting_room)


# Fill this out with directions to walk
# def dft(self, room):
#     """
#     Print each vertex in depth-first order
#     beginning from starting_vertex.
#     """
#     visited = set()
#     stack = Stack()
#     stack.push(room)
#     while stack.size() > 0:
#         curr_room = stack.pop()
#         if curr_room not in visited:
#             visited.add(curr_room)
#             # print(curr_node)
#             # find the neighbors
#             for neighbor in self.get_neighbors(curr_room):
#                 # iterate over neighbors and add to call queue
#                 stack.push(neighbor)
def dfs_walk(room, visited, path, dir):
    # print(room.id, dir)
    for direction in room.get_exits():
        neighbor_room = room.get_room_in_direction(direction)
        if neighbor_room not in visited:
            visited.add(neighbor_room)
            path.append(direction)
            dfs_walk(neighbor_room, visited, path, direction)
    if dir == 'n':
        path.append('s')
    if dir == 's':
        path.append('n')
    if dir == 'w':
        path.append('e')
    if dir == 'e':
        path.append('w')

# traversal_path = ['n', 'n']
traversal_path = []

dfs_walk(world.starting_room, {world.starting_room}, traversal_path, 'p')
# print(traversal_path)

# TRAVERSAL TEST
visited_rooms = set()
player.current_room = world.starting_room
visited_rooms.add(player.current_room)

for move in traversal_path:
    player.travel(move)
    visited_rooms.add(player.current_room)

if len(visited_rooms) == len(room_graph):
    print(f"TESTS PASSED: {len(traversal_path)} moves, {len(visited_rooms)} rooms visited")
else:
    print("TESTS FAILED: INCOMPLETE TRAVERSAL")
    print(f"{len(room_graph) - len(visited_rooms)} unvisited rooms")

# ######
# UNCOMMENT TO WALK AROUND
# ######
player.current_room.print_room_description(player)
while True:
    cmds = input("-> ").lower().split(" ")
    if cmds[0] in ["n", "s", "e", "w"]:
        player.travel(cmds[0], True)
    elif cmds[0] == "q":
        break
    else:
        print("I did not understand that command.")
