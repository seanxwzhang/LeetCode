# john’s travel city: a1 a2 c2 h8 j9
# tom’s travel city: b1 a1 c3 z5
# kate travel city: a2 a1 h8 x8

# 给你一个人john, 以及他的一堆朋友，让你计算出来和他travel的city相似度大于75%的所有朋友，并且根据这个相似度对朋友排序

class Solution(object):
    def getBuddies(self, john, friends):
        if not john:
            return friends
        johnCities = set(john)
        buddies = map(lambda friend: (len(johnCities & set(friend))/len(johnCities), friend), friends)
        buddies = filter(lambda tuple: tuple[0] > 0.75, buddies)
        return [x[1] for x in sorted(buddies, key=lambda tuple: tuple[0], reverse=True)]

        