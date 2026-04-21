class Solution:
    
    ops = {
        "+": lambda a, b: a + b,
        "-": lambda a, b: a - b,
        "*": lambda a, b: a * b,
        "/": lambda a, b: int(a / b) if b else 0
    }


    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        result = 0
        for token in tokens:
            if token not in self.ops:
                stack.append(int(token))
            else:
                b = stack.pop()
                a = stack.pop()
                result = self.ops[token](int(a), int(b))
                stack.append(result)

        return stack[0]