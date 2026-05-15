class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        some_dict = defaultdict(int)

        # iterate thru nums, increment frequency
        for num in nums:
                some_dict[num] += 1

        max_nums = []

        # retrieve the number with max frequency using max()
        for i in range(k):
            max_num = max(some_dict, key=some_dict.get)
            max_nums.append(max_num)
            del some_dict[max_num]

        print(some_dict)

        return max_nums
