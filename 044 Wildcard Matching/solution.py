from collections import defaultdict

class Solution:
    def isMatch_DFS(self, s: str, p: str) -> bool:
        if len(s) == 0 and len(p) == 0:
            return True
        elif len(p) == 0 and len(s) != 0:
            return False
        elif len(s) == 0:
            return len(set(p)) == 1 and list(set(p))[0] == '*'
        else:
            if p[0] == '*':
                if p[-1] == '?':  # optimization, delay loop stack creation
                    return self.isMatch(s[:-1], p[:-1])
                elif p[-1] != '*':
                    return self.isMatch(s[:-1], p[:-1]) if p[-1] == s[-1] else False
                for i in range(len(s) + 1):
                    if self.isMatch(s[i:], p[1:]):
                        return True
                return False
            elif p[0] == '?':
                return self.isMatch(s[1:], p[1:])
            else:
                return self.isMatch(s[1:], p[1:]) if p[0] == s[0] else False
    
    def isMatch_DP(self, s: str, p: str) -> bool:
        # dp[i][j] = isMatch(s[:i+1], p[:j+1])
        dp = [[False] * (len(p) + 1) for i in range(len(s) + 1)]
        dp[0][0] = True  # '' can match ''
        for j in range(1, len(p) + 1):
            dp[0][j] = dp[0][j - 1] if p[j - 1] == '*' else False
        for i in range(1, len(s) + 1):
            for j in range(1, len(p) + 1):
                if p[j - 1] == '*':
                    dp[i][j] = dp[i-1][j-1] or dp[i - 1][j] or dp[i][j-1]
                elif p[j - 1] == '?' or s[i-1] == p[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
        return dp[len(s)][len(p)]
    
    
    def isMatch(self, s: str, p: str) -> bool:
        nexts = 1
        s_len = len(s)
        end_bit = 1<<s_len
        d = defaultdict(int)
        for i,c in enumerate(s):
            d[c] += 1<<i
        for c in p:
            if c == '*':
                lowest_bit = (nexts & (-nexts)).bit_length() - 1
                nexts = (1<<(s_len+1)) - (1<<lowest_bit)
            elif c == '?':
                nexts <<= 1
            else:
                nexts &= d[c]
                nexts <<= 1
            if nexts == 0:
                return False
        return nexts & end_bit == end_bit
        
                
                    