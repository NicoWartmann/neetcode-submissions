class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        for char in s:
            if char == '(' or char == '{' or char == '[':
                stack.append(char)
            elif char == ')':
                if stack == [] or stack.pop() != '(': 
                    return False
            elif char == '}':
                if stack == [] or stack.pop() != '{': 
                    return False
            elif char == ']':
                if stack == [] or stack.pop() != '[': 
                    return False

    
        return not bool(stack)