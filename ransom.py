from collections import defaultdict

class Solution (object) :
    def ransom (self, magazine, note):
        characters = defaultdict(int)
        for i in magazine:
            characters[i] += 1
        
        for i in note:
            if characters[i] <= 0:
                return False
            characters[i] -= 1
        return True
        
print(Solution().ransom(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k'], "bed"))
print(Solution().ransom(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k'], "zzzz"))