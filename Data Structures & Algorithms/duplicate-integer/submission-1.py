class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dict = {}
        for i in range(len(nums)):
            if nums[i] in dict.values():
                return True   
            dict[i] = nums[i]
            print(dict)
        
        return False

        