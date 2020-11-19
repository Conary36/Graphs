import random

from collections import deque


class Queue():
    def __init__(self):
        self.queue = deque()

    def enqueue(self, value):
        self.queue.append(value)

    def dequeue(self):
        if self.size() > 0:
            return self.queue.popleft()
        else:
            return None

    def size(self):
        return len(self.queue)


class User:
    def __init__(self, name):
        self.name = name


class SocialGraph:
    def __init__(self):
        self.last_id = 0
        self.users = {}
        self.friendships = {}

    def add_friendship(self, user_id, friend_id):
        """
        Creates a bi-directional friendship
        """
        if user_id == friend_id:
            print("WARNING: You cannot be friends with yourself")
        elif friend_id in self.friendships[user_id] or user_id in self.friendships[friend_id]:
            print("WARNING: Friendship already exists")
        else:
            self.friendships[user_id].add(friend_id)
            self.friendships[friend_id].add(user_id)

    def add_user(self, name):
        """
        Create a new user with a sequential integer ID
        """
        self.last_id += 1  # automatically increment the ID to assign the new user
        self.users[self.last_id] = User(name)
        self.friendships[self.last_id] = set()

    def fisher_yates_shuffle(self, l):
        for i in range(0, len(l)):
            random_index = random.randint(i, len(l) - 1)
            l[random_index], l[i] = l[i], l[random_index]

    def get_friends(self, current_friend):
        return self.friendships[current_friend]

    def populate_graph(self, num_users, avg_friendships):
        """
        Takes a number of users and an average number of friendships
        as arguments

        Creates that number of users and a randomly distributed friendships
        between those users.

        The number of users must be greater than the average number of friendships.
        """
        # Reset graph
        self.last_id = 0
        self.users = {}
        self.friendships = {}
        # !!!! IMPLEMENT ME

        # Add users
        for user in range(num_users):
            self.add_user(user)
        # Create friendships
        friendship_combos = []
        total_friendships = avg_friendships * num_users

        for user_id in range(1, num_users + 1):
            for friend_id in range(user_id + 1, num_users + 1):
                friendship_combos.append((user_id, friend_id))

        self.fisher_yates_shuffle(friendship_combos)
        friendships_to_make = friendship_combos[:(total_friendships // 2)]
        for friendship in friendships_to_make:
            self.add_friendship(friendship[0], friendship[1])

    def get_all_social_paths(self, user_id):
        """
        Takes a user's user_id as an argument

        Returns a dictionary containing every user in that user's
        extended network with the shortest friendship path between them.

        The key is the friend's ID and the value is the path.

        ### Chose BFT as my search method
        """
        q = Queue()
        # key: user_id, value: path
        visited = {}  # Note that this is a dictionary, not a set
        q.enqueue([user_id])  # enqueue path

        while q.size() > 0:
            # get the next person
            current_path = q.dequeue()
            current_person = current_path[-1]
            # check if person was visited yet
            if current_person not in visited:
                ## If not mark as visited.
                # key: user_id, value: path
                visited[current_person] = current_path
                ## get their friends
                friends = self.get_friends(current_person)

                ## enqueue over them
                for friend in friends:
                    friend_path = list(current_path)  # Also can be written friend_path = [*current_path]
                    friend_path.append(friend)
                    q.enqueue(friend_path)

        return visited


if __name__ == '__main__':
    sg = SocialGraph()
    sg.populate_graph(10, 2)
    print(sg.friendships)
    connections = sg.get_all_social_paths(1)
    print(connections)
