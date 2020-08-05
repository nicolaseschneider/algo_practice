# // Given a string print all subsets (not permutations)
# Eg. String "abc" should output
# empty string
# a
# b
# c
# ab
# bc
# ac
# abc

class Solution (object):
  def subsets(self, string):
    solution = []
    self.helper(string, solution,[], 0)
    return solution

  def helper(self, string, solution, currSubset, currIndex):
    solution.append(''.join(currSubset))
    # join is a string method in python
    for idx in range(currIndex, len(string)):
      currSubset.append(string[idx])
      self.helper(string, solution, currSubset, idx + 1)
      currSubset.pop()


res = Solution()

print(res.subsets('abc'))
