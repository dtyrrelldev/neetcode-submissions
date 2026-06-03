class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        s_nums = nums

        triplets = []
        # print(s_nums)

        for i in range(len(s_nums)):
            l = i + 1
            r = len(s_nums) - 1

            if i > 0 and s_nums[i] == s_nums[i - 1]: # skips using the same i num twice
                continue

            while (l < r and l != r):
                current_sum = s_nums[l] + s_nums[r] + s_nums[i]

                # print("i: " , s_nums[i], s_nums[l], s_nums[r],  "current sum:", current_sum)

                if (current_sum == 0):
                    triplets.append([s_nums[i], s_nums[l], s_nums[r]])
                    l += 1
                    r -= 1
                    while l < r and s_nums[l] == s_nums[l - 1]: # avoids same l values
                        l += 1
                    # print("added!")
                elif (current_sum < 0):
                    l += 1
                else:
                    r -= 1
        
        return triplets

    
