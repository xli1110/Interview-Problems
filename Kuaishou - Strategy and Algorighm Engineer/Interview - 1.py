"""
Date: 2021 04 14
Problems: CV + Machine Learning + Code
Result:
        Interesting interviewer.
"""


class Problem1:
    """
    GBDT vs XGBoost

    Performance Evaluation

    Feature Concatenation
    """


class Problem2:
    """
    Leetcode 78
    Subsets
    """

    def __init__(self):
        self.path = []
        self.res = []

    def DFS(self, arr):
        if not arr:
            self.res.append(self.path[:])
            return

        self.res.append(self.path[:])

        for i in range(len(arr)):
            self.path.append(arr[i])
            self.DFS(arr[i + 1:])
            self.path.pop()


if __name__ == "__main__":
    sol = Problem2()

    arr = [1, 2, 3]
    sol.DFS(arr)
    print(sol.res)
