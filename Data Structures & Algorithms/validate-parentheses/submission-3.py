class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        closeToOpen = { ")" : "(", "]" : "[", "}" : "{" }

        for char in s:
            if char == '(' or char == '{' or char == '[':
                stack.append(char)
            elif stack == [] or stack.pop() != closeToOpen[char]: 
                return False

    
        return not bool(stack)