class Solution:
    def trap(self, height: List[int]) -> int:
        # build prefix array:
        prefix = []
        suffix = []
        pre = -1

        for num in height:
            if(num > pre):
                prefix.append(num)
                pre = num
            else:
                prefix.append(pre)
        print(prefix)

        # build suffix array:
        suff = -1
        for num in reversed(height):
            if (num > suff):
                suffix.append(num)
                suff = num 
            else:
                suffix.append(suff)
        
        suffix.reverse()
        print(suffix)

        # then iterate thru heights w formula and prefix/suffix arrays, use formula to find water trapped:
        area = 0

        for i in range(len(height) - 1):
            area += min(prefix[i], suffix[i]) - height[i]


        return area