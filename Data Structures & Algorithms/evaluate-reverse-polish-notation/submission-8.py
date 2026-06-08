class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for char in tokens:
            if (char == '+'):
                result = stack.pop() + stack.pop()
                stack.append(result)
            elif (char == '*'):
                result = stack.pop() * stack.pop()
                stack.append(result)
            elif (char == '-'):
                first = stack.pop() 
                result = stack.pop() - first
                stack.append(result)
            elif (char == '/'):
                first = stack.pop()
                result = int(stack.pop() / first)
                stack.append(result)
            else:
                stack.append(int(char))
            
        return stack[0]
        