# PalindromicSubstrings ii

class Solution(object):
    def minCut(self, s):
      palindrome = [[False for x in range(len(s))] for y in range(len(s))]

      for i in range(0, len(s)):
        palindrome[i][i] = True
      for i in range(0, len(s) - 1):
        if s[i] == s[i + 1]:
          palindrome[i][i + 1] = True
      for curr_len in range(3, len(s)):
        for i in range(0, len(s) - curr_len + 1):
          j = i + curr_len - 1
          if s[i] == s[j] and palindrome[i+1][j-1] == True:
            palindrome[i][j] = True

      cuts = [float('inf') for x in range(len(s))]

      for i in range(0, len(s)):
        temp = float('inf')
        if palindrome[0][i] == True:
          cuts[i] = 0
        else:
          for j in range(0, i):
            if palindrome[j+1][i] and temp > cuts[j] + 1:
              temp = cuts[j] + 1
            cuts[i] = temp
      return cuts[len(s) - 1] 


s = Solution()
print(s.minCut('banana'))
