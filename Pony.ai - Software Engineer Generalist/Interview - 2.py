"""
Date: 2021 03 04
Problems: CV + Machine Learning + Code
Result: Pass
"""


class Problem1:
    """
    Given a positive integer array with length N.
    Define an operation: add 1 to any element from this array.
    How many are the duplicate elements in the array after at most k operations?
    """

    def solution(self, arr, k):
        """
        1 - Special Case: Maximum Element M

        - Intuition:
        arr = [1, 4, 2, 3, 2]
        M = max(arr)
        temp = [M - x for x in arr]
        if k > sum(temp):
            We can add 1 to every element until reaching M.
            # duplicates = len(arr)
        else:
            ?

        - Case at ?:
        k <= sum(temp), not every element can be added to M.
        Sort the arr at first, then try to add elements so that their values are equal to M.
        Add from arr[-2] to arr[0], since arr[-2] is closest to arr[-1], then arr[-3], etc.
        Return # duplicates under the restriction of k.

        2 - Common Case: Traverse the Array
        O(N ** 2)
        O(1)
        Traverse the array from end to start, and compute # duplicates for every element.
        Since array elements are positive and the operation is adding one,
        elements equal to arr[i] can only be selected from arr[0] to arr[i - 1] in a SORTED array.
        Hint - Not necessary to store every result with an array res = [], use a variable temp.
               Space: O(N) -> O(1)

        3 - Binary Search
        Search # duplicates.
        low = 1
        high = len(arr)
        Do not have any ideas right now.
        """

        if len(arr) <= 1:
            return len(arr)

        """
        1 - Special Case
        """
        # arr.sort()
        # M = arr[-1]
        # i = len(arr) - 2
        #
        # while i >= 0:
        #     if k <= 0:
        #         return len(arr) - i - 1
        #
        #     num_opt = M - arr[i]
        #     if num_opt <= k:
        #         k -= num_opt
        #         i -= 1
        #     else:
        #         return len(arr) - i - 1
        #
        # # Case: k > sum(temp)
        # return len(arr)

        """
        2 - Common Case
        """

        def num_duplicate(i, k):
            M = arr[i]
            i = len(arr) - 2

            while i >= 0:
                if k <= 0:
                    return len(arr) - i - 1

                num_opt = M - arr[i]
                if num_opt <= k:
                    k -= num_opt
                    i -= 1
                else:
                    return len(arr) - i - 1
            return len(arr)

        arr.sort()
        i = len(arr) - 1
        temp = num_duplicate(i, k)

        while i >= 1:  # as maximum element case above, compute each element
            if temp == len(arr):
                return temp

            current_value = num_duplicate(i, k)
            if current_value > temp:
                temp = current_value

            i -= 1
        return temp
