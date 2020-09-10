class Solution(object):
    def findPoisonedDuration(self, timeSeries, duration):
        n = len(timeSeries)
        if n == 0:
            return 0

        total_poison = 0
        prev = None
        for i in range(n - 1):
            total_poison += min(timeSeries[i + 1] - timeSeries[i], duration)
        return total_poison + duration