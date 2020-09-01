# min path sum

class Solution(object):
  def minPathSum(self, grid):
    if not grid:
      return
    i_max = len(grid) - 1
    j_max = len(grid[0]) - 1
    for i in range(0, len(grid)):
      for j in  range(0, len(grid[0])):
        if i == 0 and j != 0:
          grid[i][j] = grid[i][j] + grid[i][j - 1]
        elif j == 0 and i != 0:
          grid[i][j] = grid[i][j] + grid[i - 1][j]
        elif j != 0 and i != 0:
          grid[i][j] = grid[i][j] + min(grid[i - 1][j], grid[i][j - 1])
    return grid[i_max][j_max]

s = Solution()
grid = [
  [1, 3, 1],
  [1, 5, 1],
  [4, 2, 1],
]
print(s.minPathSum(grid)) # 5