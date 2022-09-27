import itertools 
class Solution(object):
    def isAddictiveNumber(self, num: str) -> bool:
        def valid(a, b, s):
            if a != str(int(a)) or b != str(int(b)): return   
            if not s: return True
            c = str(int(a) + int(b))
            return s.startswith(c) and valid(b,c,s[len(c):])
        return any(valid(num[:i], num[i:j], num[j:]) for i,j in itertools.combinations(range(1, len(num)),2))

print(Solution().isAddictiveNumber("112358"))