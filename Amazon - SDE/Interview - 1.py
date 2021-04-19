"""
Date: 2021 04 19
Problems: Online Assignment
Result: Pass All 12 Test Cases(the first method exceeds time limit for case 8)
        Pass All 12 Test Cases
"""
import heapq


class Problem1:
    """
    Amazon Fulfillment Builder
    Similar to leetcode 1046.

    Complete the 'combineParts' function below.

    The function is expected to return an INTEGER.
    The function accepts INTEGER_ARRAY parts as parameter.
    """

    def combineParts_0(self, parts):
        """
        This is trash.
        O(N * N * logN)
        """
        # Write your code here
        if len(parts) == 1:
            return 0

        parts.sort()

        time = parts[0] + parts[1]

        parts = parts[2:] + [time]

        return self.combineParts_0(parts) + time

    def combineParts(self, parts):
        """
        O(NlogN)
        """
        # Write your code here
        heapq.heapify(parts)

        time = 0

        while len(parts) > 1:
            x1 = heapq.heappop(parts)
            x2 = heapq.heappop(parts)
            t = x1 + x2

            time += t
            heapq.heappush(parts, t)

        return time


class Problem2:
    """
    Prime Air Route

    Compute max route pairs that are less than the given maxTravelDist.
    """

    def routePairs(self, maxTravelDist, forwardRouteList, returnRouteList):
        # Write your code here
        res = []
        max_route = 0

        for x1 in forwardRouteList:
            for x2 in returnRouteList:
                if x1[1] + x2[1] == max_route:
                    res.append([x1[0], x2[0]])  # add a new pair
                if x1[1] + x2[1] > max_route and x1[1] + x2[1] <= maxTravelDist:
                    max_route = x1[1] + x2[1]
                    res = []  # clear the old array
                    res.append([x1[0], x2[0]])

        return res
