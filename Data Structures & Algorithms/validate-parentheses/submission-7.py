class Solution:
    def isValid(self, s: str) -> bool:

        stack = []

        for char in s:
            print(stack)
            if (char in '({['):
                stack.append(char)
            else:
                if (len(stack) == 0):
                    return False
                matched_char = stack.pop()
                print(f"char: {char}, matched char: {matched_char}")
                if (char == ')' and matched_char != '('):
                    return False
                elif (char == '}' and matched_char != '{'):
                    return False
                elif (char == ']' and matched_char != '['):
                    return False
        
        if (len(stack) != 0):
            return False

        return True


        