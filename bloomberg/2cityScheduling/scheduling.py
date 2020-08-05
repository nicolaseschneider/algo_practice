# leetcode #1029

class Solution (object):
  def compare(self, cost1, cost2):
    if cost2[1] - cost2[0] < cost1[1] - cost1[0]:
      return -1
    elif cost2[1] - cost2[0] > cost1[1] - cost1[0]:
      return 1
    else:
      return 0
  def scheduling(self, costs):
    cityATotal = 0
    cityBTotal = 0
    sortedByMargin = sorted(costs, cmp=self.compare)
    for idx, cost in enumerate(sortedByMargin):
      if idx < len(costs) / 2:
        cityATotal += cost[0]
      else:
        cityBTotal += cost[1]
    return cityATotal + cityBTotal

sol = Solution()

print(sol.scheduling([[10, 20],
  [30, 200],
  [400, 50],
  [30, 20]])) # 110


print(sol.scheduling([
  [20, 60],
  [10, 50],
  [30, 300],
  [40, 200],
])) # should return 180