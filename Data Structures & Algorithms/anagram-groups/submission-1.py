class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        some_dict = defaultdict(list)
    
        # we are going to use a alphabet vector as a key for each
        for word in strs:
            count = [0] * 26
            for char in word:
                count[ord(char) - ord('a')] += 1
            some_dict[tuple(count)].append(word)

        print(some_dict)
        return list(some_dict.values())
            
            

        