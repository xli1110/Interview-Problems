"""
Date: 2021 02 25
Problems: Code + CV
Result: Pass
"""

"""
Problem 1
Two-sum on BSTs.
Given two BSTs whose values are positive integers, with roots b1 and b2 respectively, and a integer target.
Return two values whose summation equals to the target from two trees.
"""


class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def solution(b_1, b_2, target_value):
    """
    O(N)
    O(1)

    1 - Recurse twice, have not used BST properties. Can be applied on any binary trees.
    Answer: Probably apply binary search. Do not have any ideas till now.

    2 - At line \alpha, if tree values and the target data type can be double,
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
