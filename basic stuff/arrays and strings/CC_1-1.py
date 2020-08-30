# is Unique implement an algorithm to determing if a string has all unique chars

# what if you cannot use additional data structures?
from sets import Set
def isUnique(str):
  set = Set([])
  for ch in str:
    if ch in set:
      return False
    else:
      set.add(ch)
  return True
# n = length of string
# time complexity is O(n)
# one interation over string
# space is O(1)
# Every character within string is added to a Set
# But the set size will never exceed length 128 - 256 
# 


print(isUnique('hello')) # False
print(isUnique('world')) # True

def isUniqueHard(str):
  for i in range(0, len(str)):
    for j in range(i + 1, len(str)):
      if str[i] == str[j]:
        return False
  return True
# n = length of string
# time complexity is O(n^2)
# we have a nested loop, 
# space is O(1)
# we arent storing anything
print(isUniqueHard('hello')) # False
print(isUniqueHard('world')) # True
print(isUniqueHard('abcdefaaa')) # False

def isUniqueFaster(str):
  sort = sorted(str)
  sortedStr = ''.join(sort)
  for i in range(0, len(str) - 1):
    if sortedStr[i] == sortedStr[i + 1]:
      return False
  return True
# n = length of string
# time complexity is O(n log n)
# we sort the string. Then we can only just compare whats in front of us.
# space is O(1)
# we arent storing anything

print(isUniqueFaster('hello')) # False
print(isUniqueFaster('world')) # True
print(isUniqueFaster('abcdefaaa')) # False


  