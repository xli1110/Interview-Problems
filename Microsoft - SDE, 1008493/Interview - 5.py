"""
Date: 2021 04 13
Problems: CV + Machine Learning + Code + Trick
Result: Pass
"""


class Problem1:
    """
    Overfitting

    Tree

    Big Data Tools
    """


class Problem2:
    """
    Reverse the BFS traversal of a complete binary tree.
    Example:
    input: [4,2,7,1,3,6,9]
    output:[4,7,2,9,6,3,1]
    """

    def reverse_arr(self, arr):
        return arr[::-1]

    def reverse_BFS(self, arr):
        level = 1
        i = 0
        while i <= len(arr) - 1:
            num_nodes = 2 ** (level - 1)

            arr[i:i + num_nodes] = self.reverse_arr(arr[i:i + num_nodes])

            i += num_nodes
            level += 1


class Problem3:
    """
    Similar to Leetcode 560.
    Given an array and a target, check whether there is a sub-array whose summation equals to the target.
    Require linear time complexity.
    Example:
    input:A=[2,1,3,4,7]
    T=5 => return false
    T=8 => return true

    I - Are these elements non-negative?
    Int - You can solve in this case.

    I solved it with two pointers, but I have no time to think about negative elements.
    """

    def check_sum(self, arr, tar):
        if not arr:
            raise Exception("Empty Array")

        low = 0
        high = 0
        temp = arr[0]  # current summation

        while high <= len(arr) - 1:
            if temp == tar:
                return True
            elif temp < tar:
                if high != len(arr) - 1:
                    high += 1
                    temp += arr[high]
                else:
                    return False
            else:
                temp -= arr[low]
                low += 1
        return False


class Problem4:
    """
    Given a bottle of blue ink and a bottle of red ink.
    Drip a drop from the red bottle into the blue bottle.
    Then, drip a drop from the blue bottle into the red bottle.
    Which is more in terms of red ink in the blue bottle and bule ink in the red bottle?

    Write a concrete example.

    Init
    B = 10b
    R = 10r

    Step 1
    drop = r, size = 1
    R = 9r
    B = 10b + r

    Step 2
    drop = 10/11b + 1/11r, size = 1
    R = 9r + 1/11r + 10/11b
    B = 10b - 10/11b + 10/11r

    10/11b in R and 10/11r in B

    Thus, they have the same volume.
    """
