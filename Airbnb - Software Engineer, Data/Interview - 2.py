"""
Date: 2021 04 20
Problems: Two Coding Problems, 45 Minutes for Each
Result: P1 - Suck in the m_tree function, did not complete.
        P2 - Talk with the interviewer over 30 minutes, and draw the final conclusion.
             However, do not have enough time to complete it.
             Talk with the interviewer about the rest part.
             Nice interviewer, helpful reminds and discussion.
"""


class Node:
    def __init__(self):
        self.val = ""
        self.children = []


class Problem1:
    """
    Print N-ary Tree
    Input = [s1, s2, s3, ..., sN]
    Tree nodes in the same level should be printed in the lexical order from top to bottom.

    Example
    "/*
    input:

    /bin/usr/bash
    /var/test/.ssh
    /var/log/wifi.log
    /opt
    /xyz

    char range: `[a-zA-Z0-9./]`

    output:

    /
    +-- bin
    |   +-- usr
    |       +-- bash
    +-- opt
    +-- var
    |   +-- log
    |   |   +-- wifi.log
    |   +-- test
    |       +-- .ssh
    +-- xyz

    * the indent should be 4 blanks
    * new node starts with `+-- `
    * the siblings are linked by '|'
    */
    """

    def m_node(self, s):
        n = Node()
        n.val = s
        return n

    def m_tree(self, root, arr):
        """
        Two Pointers
        Similar to generate N linked lists with the same root.
        """
        n1 = root
        for x in arr:
            node_exist = False

            for child in n1.children:  # avoid adding one node twice
                if child.val == x:
                    n1 = child
                    node_exist = True
                    break

            if not node_exist:
                n2 = Node()
                n2.val = x
                n1.children.append(n2)
                n1 = n2

    def DFS_print(self, node, depth):
        if depth == 0:
            print("/")
        elif depth == 1:
            print("+-- " + node.val)
        else:
            print("|" + "    " * (depth - 1) + "+-- " + node.val)

        for child in node.children:
            self.DFS_print(child, depth + 1)


class Problem2:
    """
    2D Matrix Path with Restrictions
    Given a 2D (X * Y) matrix with N bombs located at (xi, yi).
    start = [0][0]
    end = [X - 1][Y - 1]
    Find the shortest path from start to end which has the maximum d_shortest,
    where d_shortest denotes the shortest Manhattan distance between the bomb and the path.

    Example:
    N = 2
    (1, 2), (2, 3)
    output: 9(shortest path length), 2(shortest distance)

           0     1     2     3     4     5
        +-----+-----+-----+-----+-----+-----+
        |     |     |     |     |     |     |
    0   |start|     |     |     |     |     |
        |  |  |     |     |     |     |     |
        +--+--+-----+-----+-----+-----+-----+
        |  |  |     | xxx |     |     |     |
    1   |  +  |     |xxxxx|     |     |     |
        |  |  |     | xxx |     |     |     |
        +--+--+-----+-----+-----+-----+-----+
        |  |  |     |     | xxx |     |     |
    2   |  v--+-->  |     |xxxxx|     |     |
        |     |  |  |     | xxx |     |     |
        +-----+--+--+-----+-----+-----+-----+
        |     |  |  |     |     |     |     |
    3   |     |  v--+-->  |     |     |     |
        |     |     |  |  |     |     |     |
        +-----+-----+--+--+-----+-----+-----+
        |     |     |  |  |     |     |     |
    4   |     |     |  v--+--> -+--> -+>end |
        |     |     |     |     |     |     |
        +-----+-----+-----+-----+-----+-----+

    I - BFS, find all paths and calculate the shortest distance.
    Int - Let 0 < X, Y, N, <= 1000. Is your algorithm acceptable?
    I - (X * Y) ** 2.
    Int - Sure?
    I - Wrong, should be exponential complexity, like 4 ** (X + Y).
    Int - Yes, how to optimize it?

    Think.

    I - No ideas, any remind?
    Int - How to calculate one point's shortest distance to the bombs?
    I - Generate one matrix for one bomb, denoting this distance, O(XYN). s1, get mat[][].
        When traversing, at each point, we check N matrices and find the shortest distance, O(N). s2
    Int - Can we only use ONE auxiliary matrix?
    I - Yes, we traverse all bombs and update the distance matrix if we find a smaller value at s1.
        Then s2's complexity will be O(1).

    Think.
    I - Reminds please.
    Int - What if we know 2 is the shortest distance, and let you find the path?
    I - We traverse mat and block points whose value < 2.
    Int - Right, so what if we do not know 2?
    I - We can try from the maximal distance to 0, if we find the path, then we break and return.
    Int Right, complexity?
    I - O(XY * (X + Y)), cubic complexity.
    Int - Right, try to implement your ideas.
    """


    def check_exceed(self,x, y, X, Y):
        if 0 <= x < X and 0 <= y < Y:
            return True
        else:
            return False

    def BFS(self,x, y, X, Y, mat):
        dist = 0
        q = deque()
        q.append([x, y])
        while q:
            while _ in range(len(q)):
                point = q.popleft()
                i = point[0]
                j = point[1]
                mat[i][j] = min(dist, mat[i][j])
                if check_exceed(i - 1, j, X, Y):
                    q.append([i - 1, j])
                if check_exceed(i - 1, j, X, Y):
                    q.append([i + 1, j])
                if check_exceed(i, j - 1, X, Y):
                    q.append([i, j - 1])
                if check_exceed(i, j + 1, X, Y):
                    q.append([i, j + 1])
            dist += 1
        return mat

    def generate_mat(arr, X, Y):
        mat = [[9999] * Y for _ in range(X)]

        for b in arr:
            BFS(b[0], b[1], X, Y, mat)

        return mat

    def find_shortest_dist(self,mat, X, Y):
        dist = set()
        for i in range(X):
            for j in range(Y):
                if mat[i][j] not in dist:
                    dist.add(mat[i][j])

        dist = list(dist).sort()

        i = len(dist) - 1

        while i >= 0:
            shortest_dist = dist[i]

            """
            Time out at this point.
            The interviewer ask me to explain the rest part.
            """

            # check availability
            # set shorters None
            for arr in temp:
                for ele in temp:
                    if
                        None

                BFS(temp)
                break
                short_dist

            i -= 1




if __name__ == "__main__":
    # Problem 1

    s_list = [
        "/bin/usr/bash",
        "/var/test/.ssh",
        "/var/log/wifi.log",
        "/opt",
        "/xyz"
    ]
    p1 = Problem1()

    # make the root
    root = Node()
    root.val = "/"

    # make the tree
    for s in s_list:
        p1.m_tree(root, s.split("/")[1:])

    p1.DFS_print(root, 0)
