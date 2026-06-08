class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for char in tokens:
            print(char, stack)
            if char.isnumeric() or char[1:].isnumeric():
                stack.append(int(char))
            elif (char == '+'):
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
            
        return stack[0]
        