# One away
# there are 3 types of edits that can be performed on strings:
# insertion
# deletion
# replacement
# given 2 strings check if they are one edit or 0 edits away

# ex:
# # pale, ple => true
# # pales, pale => true
# # pale, bale => true
# # pale, bake => false

# checking characters. There needs to be a character difference of just one
from collections import defaultdict

def one_edit(str1, str2):
  num_dif = 0
  for i in range(0, len(str1)):
    if str1[i] != str2[i]:
      num_dif += 1
      if num_dif > 1:
        return False
  return True

def one_insert(shorter, longer):
  j = 0
  for i in range(0, len(shorter)):
    if shorter[i] != longer[j]:
      j += 1
      if j - 1 != i or shorter[i] != longer[j]:
        return False
    j += 1
  return True
  

def one_away(str1, str2):
  if len(str1) == len(str2):
    return one_edit(str1, str2)
  elif len(str1) - len(str2) == -1:
    return one_insert(str1, str2)
  elif len(str1) - len(str2) == 1:
    return one_insert(str2, str1)
  else:
    return False

# Time Complexity:
# O(n)
# iterate over the string one time
# Space Complexity:
# O(1) we only ever store indexes and number of differences. Num diff will never grow beyond 2;

# this exercise is great in understanding to break up the problem into smaller sub problems
# you have three checks. Is it easier to write functions for each check?
# yes. Do you need to call the all checks on each string? No
# we know that replacement will only work on strings with equal length
# insertion and deletion will only work on a length diff of 1
# deletion and insertion are the same thing, just seap the argument order for deletion



  

  # return True

print(one_away('pale','ple')) # True
print(one_away('pale', 'bale')) # True
print(one_away('pales', 'pale')) # True
print(one_away('pale', 'alpe')) # False
print(one_away('bob','doob')) # False
