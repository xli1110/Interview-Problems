"""
Date: 2021 03 12
Problems: CV + Code + Machine Learning
Result: Fail, the interviewer is a shabi from price decision group.
"""

import random


class Problem1:
    """
    Machine Learning

    1 - Tree Model
    principles, three types, cutting branches, parameters

    2 - LGBM
    principles

    3 - Pick the most familiar model.(Linear Regression)
    principles, gradient descend

    4 - Bayesian NN
    project

    5 - Performance Evaluation
    precision/recall/accuracy
    F-score/AUC/ROC
    """


class Problem2:
    """
    Median of Two Arrays

    Do not use stack/heap/sort.

    Do not have ideas. The interviewer asked to write a quick sort.
    """

    def solution(self, arr):
        def quick_sort(arr):
            """
            Remain the original array.
            Space complexity is too high.
            O(NlogN)
            O(N) - Seems huge, at each recursion we allocate three arrays,
                   but actually their total size is N, partitioning N elements.
            """
            if len(arr) <= 1:
                return arr
            L = []
            E = []
            G = []

            pivot = arr[0]
            for i in range(1, len(arr)):
                if arr[i] < pivot:
                    L.append(arr[i])
                elif arr[i] == pivot:
                    E.append(arr[i])
                else:
                    G.append(arr[i])
            return quick_sort(L) + E + quick_sort(G)

        def partition(arr, low, high):
            pivot = arr[high]
            i_less = low

            for i in range(low, high):
                if arr[i] <= pivot:  # leq
                    arr[i_less], arr[i] = arr[i], arr[i_less]  # in-place swap
                    i_less += 1

            arr[i_less], arr[high] = arr[high], arr[i_less]
            i_pivot = i_less
            return i_pivot

        def qs(arr, low, high):
            """
            In-place swap.
            The original array will be changed.
            O(NlogN)
            O(1)
            """
            # if high - low <= 1:  # WRONG!
            if high - low < 1:  # Note: high - low < 1 <==> len(arr) <= 1
                return

            i_pivot = partition(arr, low, high)

            qs(arr, low, i_pivot - 1)
            qs(arr, i_pivot + 1, high)

        # return quick_sort(arr)
        return qs(arr, 0, len(arr) - 1)


if __name__ == "__main__":
    sol = Problem2()
    arr = [random.randint(0, 9) for _ in range(5)]
    arr = [8, 1, 8, 9, 0]
    # arr = [3, 4, 0, 6, 3]

    print(arr)
    sol.solution(arr)
    print(arr)
