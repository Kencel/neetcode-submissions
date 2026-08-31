class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        a = 0
        b = 0
        ptr = 0
        for i in range(len(num1) - 1, -1, -1):
            a += (ord(num1[i]) - 48) * 10 ** ptr
            ptr += 1
        ptr = 0
        for i in range(len(num2) - 1, -1, -1):
            b += (ord(num2[i]) - 48) * 10 ** ptr
            ptr += 1
        return str(a * b)