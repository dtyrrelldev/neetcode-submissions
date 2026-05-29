class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        
        hash = {}

        for num in nums:
            if (num - 1) in nums:
               continue

            else:
                hash[num] = [num]
                orig = num
                next = False
                
                while not next:
                    if (num + 1) in nums:
                        hash[orig].append(num + 1)
                        num += 1
                    else:
                        next = True

        longest = 0;
        for key in hash.keys():
            if (len(hash[key]) > longest):
                longest = len(hash[key])
        
        return longest