#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 上周五第二轮电面，问经历问project，为什么想做software为什么想去uber等等，题是写一个ratelimiter作为另一个函数的wrapper，输入ip地址，若一定时间内访问次数到达limit则throwexception，否则call此函数，面经里有过这道题，有一种叫什么bucket的算法，但之前没看到，说了用hashmap+ queue，感觉效率应该很低但没想到更好的办法，另外关于time的api不太熟练稍微耽误了点时间，用的codepair有ide，要编译通过而且可以console debug


import time;

class rateLimiter(object):

    def __init__(self):
        self.tokenPersecond = 1 # you can only call the function with same ip once per second
        self.bucketSize = 5 # provide throttling, has to be greater than 0
        self.dict = {} # stores the tocken in each bucket as well as the last check time

    def checkIP(self, ip):
        if ip not in self.dict:
            self.dict[ip] = [0, time.time()]
            return True
        timePassed = time.time() - self.dict[ip][1]
        self.dict[ip][1] = time.time()
        self.dict[ip][0] += self.tokenPersecond * timePassed
        if self.dict[ip][0] > self.bucketSize: # throttling
            self.dict[ip][0] = self.bucketSize
        if self.dict[ip][0] > 1.0:
            self.dict[ip][0] -= 1.0
            return True
        return False

if __name__ == "__main__":
    r = rateLimiter()
    IPcases = "1.0.0.0"
    timeInterval = [0.5, 0.1, 0.4, 0.2]
    for i in xrange(4):
        print(r.checkIP(IPcases))
        time.sleep(timeInterval[i])

        

        
