# water land。 比如terrian是[3,2,1,2] print出来就是
# *

# * *   *

# * * * *

# * * * *

# 然后给你一个dumpPoint，一个waterAmount，比如dumpPoint 1, waterAmount 2，因为有重力，所以是从index 2开始加水
# *

# * * w *
# * * * *

# * * * *

# terrian两边是最高，模拟，先向左找到非递增的最低点，如果该点和dumpPoint一样高，往右继续找非递增的最低点，如果一样高就放到dumpPoint，不一样的话放置在非递增的最低点
def getWaterLevel(terrian, dumpPoint, waterAmount):
    waterLevel = [0 for _ in terrian]
    assert(dumpPoint < len(terrian))
    for _ in xrange(waterAmount):
        point = dumpPoint
        for i in xrange(dumpPoint - 1, -1, -1):
            if terrian[i] + waterLevel[i] > terrian[i+1] + waterLevel[i+1]:
                break
            elif terrian[i] + waterLevel[i] < terrian[point] + waterLevel[point]:
                point = i
        for i in xrange(dumpPoint + 1, len(terrian)):
            if terrian[i] + waterLevel[i] > terrian[i-1] + waterLevel[i-1]:
                break
            elif terrian[i] + waterLevel[i] < terrian[point] + waterLevel[point]:
                point = i
        waterLevel[point] += 1
    print(waterLevel)
    printWater(terrian, waterLevel)
        
def printWater(terrian, water):
    assert(len(terrian) == len(water))
    top = max([t + w for t in terrian for w in water])
    for level in xrange(top, -1, -1):
        string = ''
        for i in xrange(len(terrian)):
            if terrian[i] + water[i] == level:
                if water[i] > 0:
                    string += 'w'
                    water[i] -= 1
                else:
                    string += '*'
                    terrian[i] -= 1
            else:
                string += ' '
        print(string)

getWaterLevel([3,2,1,3], 1, 7)