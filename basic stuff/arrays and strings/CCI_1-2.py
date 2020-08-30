# check Permutation 
# given 2 strings, write a method to decide if one is a permutation of the others

from collections import defaultdict

# modifying original string
def isPerm(str1, str2):
  sort1 = sorted(str1)
  sorted_str_1 = ''.join(sort1)
  sort2 = sorted(str2)
  sorted_str_2 = ''.join(sort2)
  return sorted_str_1 == sorted_str_2

# time complexity.
# O(n log n). n is the length of the longest string
# 2 strings, sort them, check equality. done
# space complexity
# O(1)
# mutating strings uses no additional space (?)
def is_perm(str1, str2):
  count1 = defaultdict(lambda: 0, {})
  count2 = defaultdict(lambda: 0, {})
  for ch1 in str1:
    count1[ch1] += 1
  for ch2 in str2:
    count2[ch2] += 1

  for character in str1:
    if count1[character] != count2[character]:
      return False
  return True

# time complexity
# O(n) (or 3n) n is the longest string
# space complexity
# O(1)
# while we are making a dictionary entry for every character pointing to a number
# that dictionary will NEVER have more entries than 256. if this is O(2n) because 2 dictionaries.
# memory pointer wise tho. These dictionaries will never have keys with len greater than 1. I stand by O(1)

print(isPerm('dingo','oingd')) # True
print(isPerm('aa', 'a')) # False

print(is_perm('dingo','oingd')) # True
print(is_perm('aa', 'a')) # False