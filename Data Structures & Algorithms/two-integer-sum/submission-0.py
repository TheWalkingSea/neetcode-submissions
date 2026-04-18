class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ans: dict[int, int] = {}

        for i in range(len(nums)):
            if (nums[i] in ans):
                return [ans[nums[i]], i]
            ans[target - nums[i]] = i