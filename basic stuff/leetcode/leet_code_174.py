# Dungeon Game

class Solution(object):
    def calculateMinimumHP(self, dungeon):
        height, width = len(dungeon), len(dungeon[0])
        m, n = height-1, width-1
        dp = dungeon
        dp[m][n] = max(1, 1-dp[m][n])

        for row in range(m, -1, -1):
            # bottom rows
            dp[r][n] = max(1, dp[row + 1][n]-dp[row][n])
        for c in range(n-1,-1,-1):
            dp[m][c] = max(1, dp[m][c+1] - dp[m][c])
        for r in range(m-1, -1, -1):
            for c in range(n-1, -1, -1):
                dp[r][c] = max(1,min(dp[r+1][c],dp[r][c+1]) - dp[r][c])
        return dp[0][0]