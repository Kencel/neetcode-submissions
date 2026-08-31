from collections import Counter
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        c = Counter(nums)
        ans = set()
        l = 0
        r = len(nums) - 1
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                target = -(nums[i] + nums[j])
                temp = Counter((nums[i], nums[j], target))
                for number in temp:
                    if temp[number] > c[number]:
                        break
                else:
                    ans.add(tuple(sorted((nums[i], nums[j], target))))

        return [list(i) for i in ans]
                


                