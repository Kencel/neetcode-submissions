class Solution:
    def isHappy(self, n: int) -> bool:
        s = set()
        curr = n
        while curr != 1:
            temp = 0
            while curr != 0:
                temp += (curr % 10) ** 2
                curr //= 10
            if temp in s:
                return False
            s.add(temp)
            curr = temp
        return True
