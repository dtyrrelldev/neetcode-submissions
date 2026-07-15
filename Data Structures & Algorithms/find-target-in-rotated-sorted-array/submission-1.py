class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1

        while (l < r):
            mid = (l + r) // 2

            if (nums[mid] > nums[r]):
                l = mid + 1
            else: 
                r = mid
        
        
        # search right half:
        right = self.bin_search(nums, target, l, len(nums) - 1)
        # search left half
        left = self.bin_search(nums, target, 0, l - 1)
        num = max(right, left)
    
        if num != -1:
            return num

        return -1

    def bin_search(self, nums: List[int], target: int, start: int, end:int) -> int:
        l = start
        r = end

        while (l <= r):
            mid = (l + r) // 2 
            if (nums[mid] == target):
                return mid
            elif (nums[mid] > target):
                r = mid - 1
            else:
                l = mid + 1
        
        return -1


