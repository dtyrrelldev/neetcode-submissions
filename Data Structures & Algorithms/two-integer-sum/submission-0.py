class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_dict = {}

        for num in range(len(nums)):
            diff = target - nums[num]
            x = target - diff
            if (x in nums_dict):
                if num < nums_dict[x]:
                    return [num, nums_dict[x]]
                else:
                    return [nums_dict[x], num]

            else:
                nums_dict[diff] = num
            print(nums_dict)
            

        