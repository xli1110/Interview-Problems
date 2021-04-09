"""
Date: 2021 03 19
Problems: CV + Machine Learning + Code
Result: Fail
"""


class Problem1:
    """
    Machine Learning

    1 - Tree
    classification
    regression

    2 - Ensemble Learning
    loss function(exponential loss, MSE)
    GBDT(residual and negative gradient)

    3 - Pick the most familiar model.(Linear Regression)
    When is MSE the best depending on labels' distribution?
    """


class Problem2:
    """
    Binary Search
    LeetCode - 35
    Interviewed at 9 p.m. Friday.
    Tired AF, then wrote code below with linear iteration not logarithmic.
    """

    def insert_target(self, x, t):
        if not x:
            return 0

        low = 0
        high = len(x) - 1

        while low < high:
            mid = (low + high) >> 1
            if x[mid] == t:
                return mid
            elif x[mid] < t:
                high -= 1  # I suck
            else:
                low += 1  # same as above

        if x[low] > t:
            return low
        else:
            return low + 1
