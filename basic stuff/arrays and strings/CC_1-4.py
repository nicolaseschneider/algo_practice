# given a string write a function to check if it is a permutation of a palindrome
# input: tact Coa
# output: True (tacocat, atcocta)

from collections import defaultdict

# what is a palindrome?
# there must be an even amount of every letter if the length of string is even
# all but one character of the string must be even if length is odd.
# CRUSHED IT BABY YEEEE

# im going to assume a few things about input for simplicity's sake
# 1. White space does not matter. we can reformat the string if we need to remove all spaces using split and join
# # or iterating and simply ignoring whitespace characters
# 2. the string is currently all lowercase. Easy enough to format in python also
# # .lowercase is a thing for a reason.
def perm_palindrome(str):
  even = len(str) % 2 == 0

  counter = defaultdict(lambda: 0, {})
  for ch in str:
    counter[ch] += 1

  if even:
    for _, num in counter.iteritems():
      if num % 2 != 0:
        return False
  else:
    odd_count = 0
    for _, num in counter.iteritems():
      if num % 2 != 0:
        odd_count += 1
        if odd_count > 1:
          return False
    return True

# time complexity
# O(2n) or O(n) where n is the length of the string
# we iterate over the string twice
# space complexity
# O(1) we again are creating a dictionary. But that dictionary has a max number of key value pairs
# which is the number of existing characters in ASCII
# so memory pointers are limited to a couple hundred, which is constant
print(perm_palindrome('taacooocata'));
