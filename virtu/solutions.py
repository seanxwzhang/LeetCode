# 1.Return the integer that corresponds to the minimum number of steps required to change X to a Fibonacci number。每次变化可以加1或者减1。

def question1(x):
    def find_fibonacci_upper_bound(x):
        assert x > 0, "x has to be greater than 0"
        nums = [0, 1]
        while nums[-1] < x:
            nums.append(nums[-1] + nums[-2])
        return nums[-2], nums[-1]
    if x <= 0:
        return abs(x)
    else:
        bound1, bound2 = find_fibonacci_upper_bound(x)
        print(bound1)
        print(bound2)
        return min(abs(x - bound1), abs(bound2 - x))

print(question1(10))
