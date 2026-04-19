class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if (len(nums) < 2):
            return -1
        
        nums.sort()
        ans = []
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue

            target = -nums[i]
            l = i + 1
            r = len(nums) - 1

            while l < r:
                lv = nums[l]
                rv = nums[r]
                if ((lv + rv) == target):
                    ans.append([-target, lv, rv])
                    while l < r and nums[l] == nums[l+1]:
                        l += 1
                    while l < r and nums[r] == nums[r-1]:
                        r -= 1
                    l += 1
                    r -= 1
                elif ((lv + rv) > target):
                    r -= 1
                else:
                    l += 1
        return ans
        


