def reverseString(string):
  end = len(string) - 1
  start = 0
  split = list(string)
  while start < end:
    temp = split[start]
    split[start] = split[end]
    split[end] = temp
    start += 1
    end -= 1

  return ''.join(split)