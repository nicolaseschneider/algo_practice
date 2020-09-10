class Solution(object):
    def sumZero(self, n):
        result = []
        if n % 2 != 0:
            result.append(0)
        i = -1
        while len(result) < n:
            result.append(i)
            result.append(abs(i))
            i -= 1
        return result