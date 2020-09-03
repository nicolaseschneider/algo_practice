class Solution(object):
    def numIdenticalPairs(self, nums):
        prev_seen = {}
        good_pairs = 0
        for num in nums:
            if num in prev_seen:
                good_pairs += prev_seen[num]
                prev_seen[num] += 1
            else:
                prev_seen[num] = 1
        return good_pairs