"""
Date: 2021 04 06
Problems: QA + Code
Result: Fail
"""


class Problem1:
    """
    1 - Difference between tuple and list in python.

    2 - Can we hash a list?

    3 - Conditions of a hash key.

    4 - Iterator vs Generator.

    5 - Front end?

    6 - How to test a log-in page?
    """


class Problem2:
    """
    Leetcode 3
    Longest Sub-String
    """

    def sub_string(self, s):
        if not s:
            return 0

        d = {s[0]: 0}
        res = [1] * len(s)

        for i in range(1, len(s)):
            if s[i] in d:
                if i - d[s[i]] <= res[i - 1]:
                    res[i] = i - d[s[i]]
                else:
                    res[i] = res[i - 1] + 1
            else:
                res[i] = res[i - 1] + 1
            d[s[i]] = i
        return max(res)
