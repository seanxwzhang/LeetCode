def get_host(line):
    return line.split(',')[0]

def paginate(num, results):
    memo, cur, res, visited, i, total, sentry, flag = set(), [], [], {i: False for i in xrange(len(results))}, 0, 0, float('inf'), True
    while total < len(results) and i < len(results):
        if visited[i]:
            i += 1
        elif flag and get_host(results[i]) in memo:
            sentry = min(sentry, i)
            i += 1
        else:
            cur.append(results[i])
            visited[i] = True
            memo.add(get_host(results[i]))
            total += 1
            if len(cur) == num or total == len(results):
                res.append('\n'.join(cur) + '\n')
                cur = []
                memo = set()
                i = min(i+1, sentry)
            else:
                i += 1
        if i >= len(results):
            i = sentry
            flag = False
    return res