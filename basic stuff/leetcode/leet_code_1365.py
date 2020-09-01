class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        res_dict = {}
        sorted_nums = sorted(nums)
        for i, n in enumerate(sorted_nums):
          if n not in res_dict:
            res_dict[n] = i
        res = []
        for n in nums:
          res.append(res_dict[n])
        return res


# Input: nums = [8,1,2,2,3]
# Output: [4,0,1,1,3]
s = Solution()
ns = [8,1,2,2,3]
print(s.smallerNumbersThanCurrent(ns))
print(ns)