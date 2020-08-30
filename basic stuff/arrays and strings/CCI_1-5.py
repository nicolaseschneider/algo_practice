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


def one_insert(shorter, longer):
  we()

def one_away(str1, str2):
  if len(str1) == len(str2):
    return one_edit(str1, str2)
  elif len(str1) - len(str2) == -1:
    return one_insert(str1, str2)
  elif len(str1) - len(str2) == 1:
    return one_insert(str2, str1)
  else:
    return False


  

  # return True

print(one_away('pale','ple')) # True
print(one_away('pale', 'bale')) # True
print(one_away('pales', 'pale')) # True
print(one_away('pale', 'alpe')) # False
print(one_away('bob','doob')) # False
