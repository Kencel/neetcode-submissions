class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        ptr = len(digits) - 1
        while ptr >= 0:
            if digits[ptr] == 9:
                digits[ptr] = 0
                ptr -= 1
            else:
                digits[ptr] += 1
                return digits
        return [1] + [0] * len(digits)

