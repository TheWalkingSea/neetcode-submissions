class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        d = {0: 0, 1: 0, 2: 0}
        for num in nums:
            d[num] += 1

        i = 0
        for color in range(0, 3):
            for _ in range(d[color]):
                nums[i] = color
                i += 1

        return nums