"""
Date: 2021 03 04
Problems: CV + Code + Machine Learning
Result: Fail
"""


class Problem1:
    """
    Simulation addition by linked lists.
    Given two singularly linked lists representing two integers.
    Return a list represents the summation of these two integers.
    Requirement: Not permitted to use two arrays to store integer digits.

    Input
    123: 1 -> 2 -> 3 -> null
    58: 5 -> 8 -> null
    Return
    181: 1 -> 8 -> 1 -> null

    Ask the interviewer and acquire notes below.
    There is no zero-starting case, like 0123, 0057, 00002, and 00087.
    Do not need to consider empty lists.
    """

    class Node:
        def __init__(self, val):
            self.val = val  # 0 - 9
            self.next = None

    def solution(self, a, b):
        """
        1 - Brute-Force
        Traverse a and b, and use two variables x and y to store two integers.
        Let z = x + y.
        Create a new list c, representing z.

        x and y can be very large, refused by the interviewer.

        2 - List Operation
        O(M + N)
        O(M + N)
        Add x and y digit by digit from the start is not simple.
        We can not align two lists and we need an array to store carries(d1 + d2 >= 10).
        If we are given doubly linked list, the situation will become friendly.
        Ask the interviewer whether we can change the original lists.

        - Reverse two lists at first.
        - Add them digit by digit from the end to the beginning while generating a new list c.
        - Notice carries.
        - Reverse c and return.
        """

        def reverse_list(head):
            p1 = None
            p2 = head
            while p2 is not None:
                t = p2
                p2 = p2.next
                t.next = p1
                p1 = t
            return p1

        a_r = reverse_list(a)
        b_r = reverse_list(b)
        flag_carry = False

        # sentinel
        dummy = self.Node(None)
        p = dummy

        # traverse a and b
        while a_r is not None and b_r is not None:
            v = a_r.val + b_r.val
            # notice the carry
            if flag_carry:
                v += 1
            # update the flag
            flag_carry = v >= 10
            # create new node, notice the module operation
            n = self.Node(v % 10)
            # link the new list
            p.next = n
            # move the pointer
            p = n
            # iterate
            a_r = a_r.next
            b_r = b_r.next

        # traverse the remaining of a list
        if a_r is not None or b_r is not None:
            rem = a_r if a_r is not None else b_r
            while rem is not None:
                v = rem.val
                if flag_carry:
                    v += 1
                flag_carry = v >= 10
                n = self.Node(v % 10)
                p.next = n
                p = n
                rem = rem.next

        # a_r and b_r are both None
        # notice there may exist a carry
        if flag_carry:
            n = self.Node(1)
            p.next = n
            p = n

        # end the new list with None
        p.next = None
        return reverse_list(dummy.next)


class Problem2:
    """
    2D matrix robot traversal with restrictions.
    Given an m * n matrix grid, and robot moving start and end [x0, y0] -> [x1, y1].
    grid[i][j] = "" shows this grid is empty and the robot can pass it.
    grid[i][j] = "*" shows this grid is leaking water and the robot can not pass it.
    When the robot moves a step, the leaking water also spreads to four directions by one grid as shown below.
                 *
         *      ***
    *   ***    *****
         *      ***
                 *
    If the robot can reach [x1, y1], return the length of path, else return -1.

    Ask the interviewer and acquire notes below.
    No special operations on overlapped leaking.
    No considerations on corner cases, like empty matrix, invalid coordinates, etc.
    """

    def solution(self, grid, m, n, x0, y0, x1, y1):
        """
        Intuition - BFS
        O((MN) ** 2)
        O((MN) ** 2)
        Finding whether there exists a path or the shortest unweighted path, try BFS.
        Since we are trying to find the shortest path and the leaking will expand,
        there is no need to consider repeatedly visiting a grid.

        Hint 1
        Use another queue to represent leakage, do not search the whole matrix at each iteration.
        O(MN)
        O(MN) - auxiliary matrices visit and leakage

        # Initialization
        q_l = deque()
        for i in range(m):
            for j in range(n):
                if check_leak(grid, i, j):
                    q_l.append([i, j])

        # BFS
        while q:
            *** BFS for Path ***

            for _ in range(len(q_l)):
                i = q_l.popleft[0]
                j = q_l.popleft[1]

                # left
                if not check_exceed(i - 1, j, m, n) and not check_leak(leakage, i - 1, j):
                    leakage[i - 1][j] = "*"
                    q_l.append([i - 1, j])
                # right
                if not check_exceed(i + 1, j, m, n) and not check_leak(leakage, i + 1, j):
                    leakage[i + 1][j] = "*"
                    q_l.append([i + 1, j])
                # top
                if not check_exceed(i, j - 1, m, n) and not check_leak(leakage, i, j - 1):
                    leakage[i][j - 1] = "*"
                    q_l.append([i, j - 1])
                # bottom
                if not check_exceed(i, j + 1, m, n) and not check_leak(leakage, i, j + 1):
                    leakage[i][j + 1] = "*"
                    q_l.append([i, j + 1])
        """

        def check_exceed(x, y, m, n):
            if x < 0 or x >= m:
                return False
            if y < 0 or y >= n:
                return False
            return True

        def check_leak(leakage, x, y):
            return leakage[x][y] == "*"

        # BFS initialization (queue + visit + path_len)
        from collections import deque
        q = deque()
        q.append([x0, y0])

        path_len = 1

        # without visit matrix, BFS will be stuck in an infinite loop
        visit = [[False] * n for _ in range(m)]
        visit[x0][y0] = True

        # leakage matrix
        leakage = grid[:][:]

        # BFS
        while q:
            # iterate path level by level
            for _ in range(len(q)):
                coordinates = q.popleft()
                if coordinates == [x1, y1]:
                    return path_len

                x = coordinates[0]
                y = coordinates[1]

                # left
                if not check_exceed(x - 1, y, m, n) and not check_leak(leakage, x - 1, y):
                    if not visit[x - 1][y]:
                        visit[x - 1][y] = True
                        q.append([x - 1, y])
                # right
                if not check_exceed(x + 1, y, m, n) and not check_leak(leakage, x + 1, y):
                    if not visit[x + 1][y]:
                        visit[x + 1][y] = True
                        q.append([x + 1, y])
                # top
                if not check_exceed(x, y - 1, m, n) and not check_leak(leakage, x, y - 1):
                    if not visit[x][y - 1]:
                        visit[x][y - 1] = True
                        q.append([x, y - 1])
                # bottom
                if not check_exceed(x, y + 1, m, n) and not check_leak(leakage, x, y + 1):
                    if not visit[x][y + 1]:
                        visit[x][y + 1] = True
                        q.append([x, y + 1])

            path_len += 1

            # iterate leakage
            temp = leakage[:][:]

            for i in range(m):
                for j in range(n):
                    if check_leak(leakage, i, j):
                        # left
                        if not check_exceed(i - 1, j, m, n):
                            temp[i - 1][j] = "*"
                        # right
                        if not check_exceed(i + 1, j, m, n):
                            temp[i + 1][j] = "*"
                        # top
                        if not check_exceed(i, j - 1, m, n):
                            temp[i][j - 1] = "*"
                        # bottom
                        if not check_exceed(i, j + 1, m, n):
                            temp[i][j + 1] = "*"
            leakage = temp[:][:]
        return -1
