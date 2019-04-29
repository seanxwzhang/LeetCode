from typing import Tuple

class Solution:
    def parseExp(self, s: str, i: int, prev_op: str) -> Tuple[int, int]:
        stack, prev = [], 0
        while i < len(s):
            char = s[i]
            if char == "(":
                prev, j = self.parseExp(s, i + 1, "+")
                i = j + 1
            elif char.isdigit():
                j = i + 1
                while j < len(s) and s[j].isdigit():
                    j += 1
                prev = int(s[i:j])
                i = j
            else:
                if char != ' ':
                    if prev_op == '+':
                        stack.append(prev)
                    elif prev_op == '-':
                        stack.append(-prev)
                    elif prev_op == '*':
                        last = stack.pop()
                        stack.append(last*prev)
                    elif prev_op == '/':
                        last = stack.pop()
                        stack.append(int(last/prev))
                    if char == ")":
                        return sum(stack), i
                    else:
                        prev_op = char
                        prev = 0
                i += 1
        return sum(stack), i
        
    def calculate(self, s: str) -> int:
        res, _ = self.parseExp(s + "+", 0, "+")
        return res