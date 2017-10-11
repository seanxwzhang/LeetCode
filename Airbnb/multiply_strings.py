# 但是string里面的数可以为负

# leetcode 43题，多了个负数的情况（https://leetcode.com/problems/multiply-strings/?tab=Description）

def multiply(num1, num2):
    sign = 1
    if num1[0] == '-':
        sign *= -1
        num1 = num1[1:]
    if num2[0] == '-':
        sign *= -1
        num2 = num2[1:]
    res = [0] * (len(num1) + len(num2))
    for i, vi in enumerate(num1):
        for j, vj in enumerate(num2):
            mul = int(vi) * int(vj)
            res[i+j+1] += mul % 10
            res[i+j] += mul / 10
    for i in xrange(len(res) - 1, 0, -1):
        res[i - 1] += res[i] / 10
        res[i] %= 10
    ans = ''.join(map(str, res)).lstrip('0')
    return str(sign*int(ans)) if ans else '0'

print(multiply('123', '-8212342451234219'))
