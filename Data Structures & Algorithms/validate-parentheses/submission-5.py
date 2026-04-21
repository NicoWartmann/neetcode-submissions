class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        closeToOpen = { ')' : '(', ']' : '[', '}' : '{' }

        for char in s:
            if char not in closeToOpen:
                stack.append(char)
            elif not stack or stack.pop() != closeToOpen[char]: 
                return False
                
        return not bool(stack)