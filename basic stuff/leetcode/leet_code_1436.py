# given an array of paths [citya, cityb] return the destination city
from sets import Set
class Solution(object):
    def destCity(self, paths):
        not_dest = {}
        possible_dest = {}
        for path in paths:
            not_dest.add(path[0])
            possible_dest.add(path[1])
        for dest in possible_dest:
            if dest not in not_dest:
                return dest