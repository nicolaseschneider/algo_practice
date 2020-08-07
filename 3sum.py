class Solution(object):
    def threeSum(self, nums):
        res = []
        nums.sort()
        for i in range(len(nums) - 2):
            if (i == 0 or nums[i] > nums[i - 1]):
                start = i + 1
                end = len(nums) - 1
                while start < end:
                    if nums[start] + nums[end] + nums[i] == 0:
                        res.append([nums[start], nums[end], nums[i]])
                    if nums[start] + nums[end] + nums[i] < 0:
                        curr_start = start
                        while (nums[start] == nums[curr_start] and start < end):
                            start += 1
                    else:
                        curr_end = end
                        while (nums[end] == nums[curr_end] and end > start):
                            end -= 1
                            
        return res


res = Solution()

print(res.threeSum([-1, -1, 0, 1, 2, -4]))