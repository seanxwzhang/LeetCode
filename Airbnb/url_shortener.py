# （https://instant.1point3acres.com/thread/196339）

# 看描述好像是url里的id如果有某些位置大小写换了会导致原来的url decode有问题，需要重写encode方法，回溯改某些位的大小写判断

class decodeURL(object):
    def decode(self, url):
        dUrl = "kljJJ324hijkS_"
        if url == dUrl:
            return 848662
        return -1

    def decodeFind(self, url):
        return self.helper(url, 0)

    def helper(self, url, index):
        if index == len(url):
            return self.decode(url)
        elif url[index].isalpha():
            up = self.helper(url[:index] + url[index].upper() + url[index+1:], index +1)
            low = self.helper(url[:index] + url[index].lower() + url[index+1:], index +1)
            return up or low
        elif url[index] in ('_'):
            exist = self.helper(url, index + 1)
            not_exist = self.helper(url[:index] + url[index+1:], index+1)
            return exist or not_exist
        return self.helper(url, index + 1)
