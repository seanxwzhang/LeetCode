class Solution(object):
    def fullJustify(self, words, maxWidth):
        """
        :type words: List[str]
        :type maxWidth: int
        :rtype: List[str]
        """
        letters, cur, res = 0, [], []
        for w in words:
            if letters + len(w) + len(cur) > maxWidth:
                for i in xrange(maxWidth - letters):
                    cur[i % (len(cur) - 1 or 1)] += ' '
                res.append(''.join(cur))
                letters, cur = 0, []
            cur.append(w)
            letters += len(w)
        return res + [' '.join(cur).ljust(maxWidth)]
