from collections import deque

def vow_check(ch): 
  return ch.lower() in 'aeiou'


def reverse_vowels(str):
  split = list(str)
  vow_list = deque()
  for ch in split:
    if vow_check(ch):
      vow_list.appendleft(ch)
  
  for idx, ch in enumerate(split):
    if vow_check(ch):
      split[idx] = vow_list.popleft()
  
  return ''.join(split)

print(reverse_vowels('hello'))