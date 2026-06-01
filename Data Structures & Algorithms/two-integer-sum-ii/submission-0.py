class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l = 0
        r = len(numbers) - 1

        while (l < r and l != r):
            le = numbers[l]
            ri = numbers[r]
            if (le + ri == target):
                return [l + 1, r + 1]
            else:
                if (le + ri > target):
                    r -= 1
                else:
                    l += 1
        