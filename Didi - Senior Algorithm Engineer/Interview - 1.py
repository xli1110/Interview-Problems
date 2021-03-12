"""
Date: 2021 03 12
Problems: CV + Code
Result:
"""


class Problem1:
    """
    Two-sum on two BSTs.
    Given two BSTs whose values are positive integers, with roots b1 and b2 respectively, and a integer target.
    Return two values whose summation equals to the target from two trees.
    """

    class Node:
        def __init__(self, val):
            self.val = val
            self.left = None
            self.right = None

    def solution(self, b_1, b_2, target_value):
        """
        O(N)
        O(1)

        Hint 1 - Recurse twice, have not used BST properties. Can be applied on any binary trees.
        Answer: Probably apply binary search. Do not have any ideas yet.

        Hint 2 - At line \alpha, if tree values and the target data type can be double,
                 how to return the summation that is closest to the target?
        Answer: Due to double precision problem, double x == double y sux.
                Brute-force method, O(N ** 2), O(N).

                Pseudo Code:
                arr_v = []
                arr_node = []
                Traverse b_1 with node_1:
                    node_set = [node_1, b_2]
                    v_min = target - node_1.val - b_2.val
                    Traverse b_2 with node_2:
                        if target - node_1.val - node_2.val < v_min:
                            node_set[1] = node_2
                    arr_node.append(node_set)
                return arr_node[arr_v.index(min(arr_v))]
        """
        if b_1 is None or b_2 is None:
            raise Exception("At least one of the given BSTs is empty.")

        def DFS(node):
            if node is None:
                return

            DFS(node.left)
            value_set.add(node.val)
            DFS(node.right)

        def DFS_search(node, target, s):
            if node is None:
                return
            if res:  # already found the answer, return to root
                return

            DFS(node.left)
            if target - node.val in s:  # \alpha
                res.append(node.val)
                res.append(target - node.val)
                return
            DFS(node.right)

        value_set = set()
        res = []
        DFS(b_1)
        DFS_search(b_2, target_value, value_set)
        return res


class Problem2:
    """
    Smallest matrix.
    Given a matrix(M \times N) with positive integer elements, and a positive integer target,
    how to find the smallest submatrix whose elements' summation is closest to the target?
    """

    def mat_sum(self, start_i, start_j, end_i, end_j, pre_sum_mat):
        """
        Calculate the matrix summation.
        Notice index exceeding.
        """
        if start_i == 0 and start_j == 0:
            # x x 0 0 0
            # x x 0 0 0
            # x x 0 0 0
            # x x 0 0 0
            # 0 0 0 0 0
            return pre_sum_mat[end_i][end_j]
        if start_i == 0 and start_j != 0:
            # 0 x x x 0
            # 0 x x x 0
            # 0 x x x 0
            # 0 0 0 0 0
            # 0 0 0 0 0
            return pre_sum_mat[end_i][end_j] - pre_sum_mat[end_i][start_j - 1]
        if start_i != 0 and start_j == 0:
            # 0 0 0 0 0
            # x x x x x
            # x x x x x
            # x x x x x
            # 0 0 0 0 0
            return pre_sum_mat[end_i][end_j] - pre_sum_mat[start_i - 1][end_j]

        # start_i != 0 and start_j != 0
        # 0 0 0 0 0
        # 0 0 x x 0
        # 0 0 x x 0
        # 0 0 x x 0
        # 0 0 x x 0
        return pre_sum_mat[end_i][end_j] - pre_sum_mat[end_i][start_j - 1] - pre_sum_mat[start_i - 1][end_j] \
               + pre_sum_mat[start_i - 1][start_j - 1]

    def solution(self, mat, target, M, N):
        """
        O(M ** 2 * N ** 2)
        O(MN)
        Two dimensional optimization.
        1 - For a submatrix with size i * j, search the start position where difference is minimized.
        2 - For all submatrices, search which produces the smallest difference.

        Hint 1 - How to calculate the summation of a submatrix?
        Answer: Implement pre sum matrix, where pre_sum_mat[i][j] = sum(matrix start at [0][0], end at [i][j]).

        Hint 2 - O(M ** 2 * NlogN), Fix start, then binary search end on the pre_sum matrix.
        Answer: TBD.
        """
        if not mat:
            raise Exception("The matrix is empty.")

        # Pre Summation Matrix
        # pre_sum_mat[i][j] = sum(mat start at [0][0], end at [i][j])
        pre_sum_mat = [[0] * N for _ in range(M)]

        # initialization
        pre_sum_mat[0][0] = mat[0][0]
        for i in range(1, M):
            pre_sum_mat[i][0] = pre_sum_mat[i - 1][0] + mat[i][0]
        for j in range(1, N):
            pre_sum_mat[0][j] = pre_sum_mat[0][j - 1] + mat[0][j]

        # loop
        for i in range(1, M):
            for j in range(1, N):
                pre_sum_mat[i][j] = pre_sum_mat[i - 1][j] + pre_sum_mat[i][j - 1] + mat[i][j] \
                                    - pre_sum_mat[i - 1][j - 1]

        # Optimization 1
        # diff_mat[i][j] = [submat_start_row, submat_start_col, diff_val]
        # the closest submatrix with size i * j starts at position [submat_start_row][submat_start_col]
        diff_mat = [[] * N for _ in range(M)]

        # generate diff_mat
        for i in range(M):  # submatrix size i * j
            for j in range(N):
                # record closest submat's start position
                # search the position where submatrix with size i * j is closest to the target
                min_diff = abs(self.mat_sum(0, 0, i, j, pre_sum_mat) - target)
                min_start_i = 0
                min_start_j = 0
                for start_i in range(1, M):  # submatrix start position [start_i][start_j]
                    for start_j in range(1, N):
                        # check exceed
                        if start_i + i <= M - 1 and start_j + j <= N - 1:
                            # update position
                            temp_diff = abs(self.mat_sum(0, 0, i, j, pre_sum_mat) - target)
                            if temp_diff < min_diff:
                                min_start_i = start_i
                                min_start_j = start_j

                if min_diff == 0:
                    return [min_start_i, min_start_j, min_start_i + i, min_start_j + j]

                diff_mat[i][j] = [min_start_i, min_start_j, min_diff]

        # Optimization 2
        # Search final result. Which submatrix produces the closest diff?
        # The start position of submatrix has already been stored.
        close_i_start = diff_mat[0][0][0]
        close_j_start = diff_mat[0][0][1]
        close_i_end = diff_mat[0][0][0] + 0
        close_j_end = diff_mat[0][0][1] + 0
        close_diff = diff_mat[0][0][2]
        for i in range(1, M):
            for j in range(1, N):
                if diff_mat[i][j][2] < close_diff:
                    close_i_start = diff_mat[i][j][0]
                    close_j_start = diff_mat[i][j][1]
                    close_i_end = diff_mat[i][j][0] + i
                    close_j_end = diff_mat[i][j][1] + j
                    close_diff = diff_mat[i][j][2]
        return [close_i_start, close_j_start, close_i_end, close_j_end]
