"""
Date: 2021 04 07
Problems: CV + Machine Learning + Code
Result: Fail, they said they need one more experienced.
"""


class Problem1:
    """
    Leetcode 394
    Decode String
    """

    def decode(self, s):
        stack = []
        dic = {"1", "2", "3", "4", "5", "6", "7", "8", "9", "0"}
        res = ""
        num_left = 0
        num_right = 0
        for i in range(len(s)):
            if s[i] == "]":
                num_right += 1
                t = ""
                while stack[-1] != "[":
                    t = stack.pop() + t
                stack.pop()  # "["

                num = ""
                while stack and stack[-1] in dic:
                    num = stack.pop() + num

                if num_left == num_right:
                    res += t * int(num)
                else:
                    stack.append(t * int(num))

            elif s[i] == "[":
                num_left += 1
                stack.append(s[i])
            elif s[i] in dic:
                stack.append(s[i])
            else:  # letter
                if num_left != 0:
                    stack.append(s[i])
                else:
                    res += s[i]
        return res


if __name__ == "__main__":
    sol = Problem1()

    s = "3[a10[c]]"

    print(sol.decode(s))
