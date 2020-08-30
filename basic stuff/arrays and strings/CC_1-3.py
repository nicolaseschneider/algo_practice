# URLify
# write a method that replaces all spaces in a string with %20
# assume that the string has sufficient space at the end to hold the additional characters and that you are given the true length of the string

# input: "Mr John Smith        ", 13
# output: "Mr%20John%20Smith"

def urlify(str, length):
  sliced = str[:length]
  return '%20'.join(sliced.split())


print(urlify("Mr John Smith        ", 13))

# not sure if i understand this question correctly? like if there are extra spaces in the middle do I include them?