class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        return_stack = [-1] * (len(temperatures))
        idx_stack = [0]
        curr = 1
        

        while (curr < len(temperatures)):
            print(f"curr: {curr}, idx_stack: {idx_stack}, return_stack: {return_stack})")

            i = -1
            while len(idx_stack) > 0 and (temperatures[curr] > temperatures[idx_stack[i]]) :
                print(f"curr: {temperatures[curr]}, {temperatures[idx_stack[i]]})")

                old_idx = idx_stack.pop()
                return_stack[old_idx] = curr - old_idx
            
            idx_stack.append(curr)
            curr+=1

        while len(idx_stack) > 0:
                old_idx = idx_stack.pop()
                return_stack[old_idx] = 0
        
            
            
        return return_stack
                