class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = sorted(zip(position, speed))
        ans = len(cars)

        print(cars)

        def time(c, t):
            return (t - c[0]) / c[1]

        ans = 1
        m = time(cars[-1], target)
        for i in range(len(cars) - 2, -1, -1):
            if time(cars[i], target) > m:
                ans += 1
                m = time(cars[i], target)
        return ans

        


            