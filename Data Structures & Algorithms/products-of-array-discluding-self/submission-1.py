class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pre = 1
        new_nums = [1] * len(nums)
        
        for i in range(len(nums)):
           new_nums[i] = pre
           pre *= nums[i]

        print(new_nums)

        post = 1
        for i in range(len(nums) - 1, -1, -1):
            new_nums[i] *= post
            post *= nums[i]
            
        return new_nums