class Solution:
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        stack = []  # res = sum(stack)
        num = 0
        sign = '+'  # default
        s += '+'  # add a char to force it processing the last number
        for char in s:
            if '0' <= char <= '9':  # digit
                num = num * 10 + ord(char) - ord('0')
            else:  # finish scanning a number
                if char != ' ':
                    if sign == '+':  # last sign
                        stack.append(num)
                    elif sign == '-':
                        stack.append(-num)
                    elif sign == '*':
                        last = stack.pop()
                        stack.append(last*num)
                    elif sign == '/':
                        # 3//2 = 1, -3//2 = -2
                        # 14-3//2 != 14+(-3//2)
                        last = stack.pop()
                        if last < 0:
                            stack.append(-(-last//num))
                        else:
                            stack.append(last//num)

                    # reset
                    sign = char
                    num = 0

        return sum(stack)