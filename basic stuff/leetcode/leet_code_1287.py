class Solution(object):
    def findSpecialInteger(self, arr):
        min_to_solution = len(arr) / 4
        prev = None
        current = None
        num_seen = 0
        for i in range(0, len(arr)):
            prev = current
            current = arr[i]
            if (prev == current):
                num_seen += 1
            else:
                num_seen = 1
            if num_seen > min_to_solution:
                return arr[i]