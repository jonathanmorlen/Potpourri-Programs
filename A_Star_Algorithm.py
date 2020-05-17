def aStar(maze, start, end):
    # initialize A*
    openSet = set()
    closedSet = set()
    start.cost = 0
    openSet.add(start)

    # perform search
    while openSet:
        # visit node
        currentNode = min(openSet, key=lambda x: x.cost)
        openSet.remove(currentNode)
        closedSet.add(currentNode)

        # check for end
        if currentNode == end:
            path = []
            current = currentNode
            while current is not None:
                path.append((current.x, current.y))
                current = current.parent
            return path[::-1]

        # generate set of surrounding nodes reachable with legal moves
        surroundingNodes = maze.getSurroundingNodes(currentNode)
        for node in surroundingNodes:
            if node in closedSet or openSet:
                continue

            node.parent = currentNode
            node.distanceFromStart = currentNode.distanceFromStart + 1
            node.distanceFromEnd = ((node.x - end.x) ** 2) + ((node.y - end.y) ** 2)
            node.cost = node.distanceFromStart + node.distanceFromEnd

            openSet.add(node)


class Maze:
    def __init__(self, maze_string, start, end):
        self.width = len(maze_string[0])
        self.height = len(maze_string)
        self.nodes = []

        for y in range(self.height):
            nodeRow = []
            for x in range(self.width):
                # create node
                node = Node(x, y)
                node.value = maze_string[y][x]
                node.distanceFromEnd = 0
                node.distanceFromStart = 0
                node.cost = 0

                # rebuild maze as 2D list of nodes
                nodeRow.append(node)
            self.nodes.append(nodeRow)

    def getNode(self, x, y):
        # check if accessing nonexistent node
        if (x < 0) or (x >= self.width):
            return None
        if (y < 0) or (y >= self.height):
            return None
        if self.nodes[y][x].value == 1:
            return None
        return self.nodes[y][x]

    def getSurroundingNodes(self, node):
        x = node.x
        y = node.y

        # find the surrounding nodes and form a set with them
        left = self.getNode(x - 1, y)
        up = self.getNode(x, y - 1)
        right = self.getNode(x + 1, y)
        down = self.getNode(x, y + 1)
        surrounding = {left, up, right, down}

        # if any nodes accessed are nonexistent, remove them
        if None in surrounding:
            surrounding.remove(None)
        return surrounding

    # for debugging and printing
    def __str__(self):
        maze = ""
        for y in range(self.height):
            row = ""
            for x in range(self.width):
                row = row + str(self.nodes[y][x]) + " "
            maze = maze + row + '\n'
        return maze


class Node:
    def __init__(self, x, y):
        # coordinates of node in maze
        self.x = x
        self.y = y

        # whether node is a 1 or 0
        self.value = None

        # if a wall has been removed to reach this node
        self.removed = False

        # cost of node
        self.distanceFromStart = 0
        self.distanceFromEnd = 0
        self.cost = 0

        # parent of node in path
        self.parent = None

    # for debugging and printing
    def __str__(self):
        return str(self.value)

    # for debugging
    def __repr__(self):
        return str((self.x, self.y))

    # for usage in sets
    def __eq__(self, other):
        return (self.x == other.x) and (self.y == other.y)

    # for usage in sets
    def __hash__(self):
        return hash((self.x, self.y))


def solveMaze(maze_string, start, end):
    if not (0 <= start[0] <= len(maze_string[0])):
        raise ValueError("Out of bounds x coordinate for start (x, y)")
    if not (0 <= start[1] <= len(maze_string)):
        raise ValueError("Out of bounds y coordinate for start (x, y)")
    if not (0 <= end[0] <= len(maze_string[0])):
        raise ValueError("Out of bounds x coordinate for end (x, y)")
    if not (0 <= end[1] <= len(maze_string)):
        raise ValueError("Out of bounds y coordinate for end (x, y)")

    # create maze of nodes instead of 1's and 0's
    maze = Maze(maze_string)
    start = maze.nodes[start[1]][start[0]]
    end = maze.nodes[end[1]][end[0]]

    # Display path and path length
    path = aStar(maze, start, end)
    for coordinates in path:
        maze_string[coordinates[1]][coordinates[0]] = 'x'
    solved_maze_string = ""
    for y in range(len(maze_string)):
        row = ""
        for x in range(len(maze_string[0])):
            row = row + str(maze_string[y][x]) + " "
        solved_maze_string = solved_maze_string + row + '\n'
    print(solved_maze_string)
    print(path)
    print("path length: " + str(len(path)) + '\n')


if __name__ == '__main__':
    # construct new maze here, travel from top left to bottom right
    # 1's are unable to be traveled, 0's are able to be traveled
    maze_map1 = [[0, 1, 1, 0],
                 [0, 0, 0, 1],
                 [1, 1, 0, 0],
                 [1, 1, 1, 0]]

    maze_map2 = [[0, 0, 0, 0, 0, 0],
                 [1, 1, 1, 1, 1, 0],
                 [0, 0, 0, 0, 0, 0],
                 [0, 1, 1, 1, 1, 1],
                 [0, 1, 1, 1, 1, 1],
                 [0, 0, 0, 0, 0, 0]]

    maze_map3 = [[0, 0, 1, 0, 0, 0],
                 [1, 0, 1, 0, 1, 0],
                 [0, 0, 0, 0, 1, 0]]

    maze_map4 = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

    # Run A* on mazes from start (x, y) to end (x, y)
    solveMaze(maze_map1, (0, 0), (3, 3))
    solveMaze(maze_map2, (0, 0), (5, 5))
    solveMaze(maze_map3, (0, 0), (5, 2))
    solveMaze(maze_map4, (0, 0), (9, 9))
