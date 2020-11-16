import queue
# // https://www.hackerrank.com/challenges/tree-huffman-decoding/problem

# // You are given pointer to the root of the Huffman tree and a binary coded string to decode. You need to print the decoded string.

# // Function Description

# // Complete the function decode_huff in the editor below. It must return the decoded string.

# // decode_huff has the following parameters:

# // root: a reference to the root node of the Huffman tree
# // s: a Huffman encoded string




"""class Node:
    def __init__(self, freq,data):
        self.freq= freq
        self.data=data
        self.left = None
        self.right = None
"""        

1010
'bb';
# Enter your code here. Read input from STDIN. Print output to STDOUT
def decodeHuff(root, s):
    current = root
    result = []

    for char in s:
        #traverse the tree
        if char is '1':
            current = current.right
        else:
            current = current.left
        #if we are at a character node, reset traversal and append current character to result
        if current.left is None and current.right is None:
            result.append(current.data)
            current = root
    print(''.join(result))
    return ''.join(result)


  # the string will contain only 1 or 0;
  # 0 means go left. 1 means go right;
  # if you hit a node with a value, return that value.
	#Enter Your Code Here