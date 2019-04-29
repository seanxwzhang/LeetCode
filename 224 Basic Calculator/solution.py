class Solution:
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        stack = []
        num, res, sign = 0,0,1
        s += '+'
        for c in s:
            if c.isdigit():
                num = num * 10 + ord(c) - ord('0')
            else:
                if c != ' ':
                    if c in '+-':
                        res += sign * num
                        sign = 1 if c == '+' else -1
                        num = 0

                    elif c == '(':
                        stack.append(res)
                        stack.append(sign)
                        sign, res, num = 1, 0, 0
                    elif c == ')':
                        res += sign * num
                        res *= stack.pop()
                        res += stack.pop()
                        sign, num = 1, 0
        return res
        