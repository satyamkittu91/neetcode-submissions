class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 != 0:
            return False

        stack = []
        bracket_map = {
            ')' : '(', ']' : '[', '}' : '{'
        }
        for bracket in s:
            if bracket in bracket_map:
                top_element = stack.pop() if stack else '#'

                if bracket_map[bracket] != top_element:
                    return False
            
            else:
                stack.append(bracket)

        return len(stack) == 0