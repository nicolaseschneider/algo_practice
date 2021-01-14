# // https://leetcode.com/problems/house-robber/

class Solution:
  def rob(self, nums):
    table = [float('-inf')]* len(nums);
    table[0] = nums[0]
    for i in range(0, len(table)):
      if i + 1 < len(table):
        table[i + 1] = max(table[i] - nums[i] + nums[i + 1], table[i + 1])
      if i + 2 < len(table):
        table[i + 2] = max(table[i] + nums[i + 2], table[i + 2])
    return table[-1]
# print(rob([4,3,1,3])) // 4 + 3 = 7
s = Solution()
print(s.rob([2,7,9,3,1])) # 12
print(s.rob([4,3,1,3])) # 7