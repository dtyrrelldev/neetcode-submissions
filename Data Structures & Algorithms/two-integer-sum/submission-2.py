class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_dict = {}

        for num in range(len(nums)):
            diff = target - nums[num]
            x = target - diff
            if (x in nums_dict):
                return [nums_dict[x], num]

            else:
                nums_dict[diff] = num
            

        