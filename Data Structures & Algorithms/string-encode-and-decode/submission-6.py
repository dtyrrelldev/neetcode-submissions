class Solution:

    def encode(self, strs: List[str]) -> str:
        new_str = ""
        if not strs:
            return ""
        else:   
            for word in strs:
                new_str += (str(len(word)) + "#" + word)
        print(new_str)
        return new_str   


    def decode(self, s: str) -> List[str]:
        new_list = []
       
        if not str:
            return []
        else:
            res = []
            i = 0
            
            while i < len(s):
                j = i
                while (s[j] != '#'):
                    j+= 1
                length = int(s[i:j]) # computing the NUMBER  
                i = j + 1
                j = i + length
                new_list.append(s[i:j]) # adding the actual next WORD to the list
                i = j
                print(new_list)

            return new_list
                
                    



