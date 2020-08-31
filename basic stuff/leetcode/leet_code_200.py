from sets import Set
class Solution(object):


  def coord_key(self, x, y):
    return ('(%s,%s)' %(x, y))

  def discover_island(self, grid, x, y, coords):
    coordinates = self.coord_key(x, y)
    if coordinates not in coords and grid[x][y] == '1':
      coords.add(coordinates)
      if x > 0:
        self.discover_island(grid, x - 1, y, coords)
      if y > 0:
        self.discover_island(grid, x, y - 1, coords)
      if x < len(grid) - 1:
        self.discover_island(grid, x + 1, y, coords)
      if y < len(grid[x]) - 1:
        self.discover_island(grid, x, y + 1, coords)
    return

  def numIslands(self, grid):
    island_count = 0
    coord_set = Set([])

    for x in range(0, len(grid)):
      # row logic
      for y in range(0, len(grid[x])):
        key = self.coord_key(x,y)
        if grid[x][y] == '1' and key not in coord_set:
          self.discover_island(grid, x, y, coord_set)
          island_count += 1

    return island_count

class Mutating_Solution(object):

  def discover_island(self, grid, x, y):
      if grid[x][y] == '1':
          grid[x][y] = '0'
          if x > 0:
              self.discover_island(grid, x - 1, y)
          if y > 0:
              self.discover_island(grid, x, y - 1)
          if x < len(grid) - 1:
              self.discover_island(grid, x + 1, y)
          if y < len(grid[x]) - 1:
              self.discover_island(grid, x, y + 1)
      return

  def numIslands(self, grid):
      island_count = 0

      for x in range(0, len(grid)):
      # row logic
          for y in range(0, len(grid[x])):
              if grid[x][y] == '1':
                  self.discover_island(grid, x, y )
                  island_count += 1

      return island_count



grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]



sol = Solution()
print(sol.numIslands(grid)) # 3