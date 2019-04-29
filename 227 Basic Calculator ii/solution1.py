class Solution:
    def calculate(self, s: str) -> int:
        s = "+" + s.replace(" ", "") + "+"
        i, total, prev = 0, 0, 0
        while i < len(s):
            if s[i] in ["+", "-"]:
                total += prev
                j = i + 1
                if j >= len(s):
                    break
                while s[j].isdigit():
                    j += 1
                prev = int(s[(i + 1):j]) * (1 if s[i] == "+" else -1)
                i = j
            else:
                j = i + 1
                while s[j].isdigit():
                    j += 1
                num = int(s[i + 1:j])
                if s[i] == "*":
                    prev = int(prev * num)
                else:
                    prev = int(prev / num)
                i = j
        return int(total)
                
            
            