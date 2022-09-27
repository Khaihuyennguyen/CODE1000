class Solution(object):
    def isAddictiveNumber(self, num: str) -> bool:
        res = []
        if len(num) <= 2:
            return False
        
        def get_all_nums(first, second, index):
            s = str(first) + str(second)
            while len(s) < len(num):
                