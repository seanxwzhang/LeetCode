# 给出一个ipv4的range，找出最少的cidr可以覆盖这个range内的所有ip。

# 参考：
# 背景介绍https://en.wikipedia.org/wiki/Classless_Inter-Domain_Routing
# 这个是个online转化工具http://www.ipaddressguide.com/cidr
# 大概的思路是group as much IPs as you can.
# 描述起来还真的麻烦呢，建议跑几个case，就理解了
from math import *

def ipToNum(ip):
    val = 0
    for x in ip.split('.'):
        val = (val << 8) + int(x)
    return val

def numToIp(num):
    res, i = ['0'] * 4, 3
    while num:
        res[i] = str(num % (1 << 8))
        num /= (1 << 8)
        i -= 1
    return '.'.join(res)

def ip2cidr(start, end):
    if not start or not end or start.count('.') != 3 or start.count('.') != 3:
        return None
    start, end = ipToNum(start), ipToNum(end)
    if start > end:
        return None
    res = []
    while start <= end:
        firstOne = start & (-start)
        maxMask = 32 - int(log(firstOne, 2))
        maxDiff = 32 - int(log(end - start + 1, 2))
        maxMask = max(maxMask, maxDiff)
        ip = numToIp(start)
        res += ip + '/' + str(maxMask),
        start += (1 << (32 - maxMask))
    return res

print(ip2cidr('192.168.0.44', '192.169.3.12'))