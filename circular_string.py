def circ(source, target):
    d_target = { ch:target.count(ch) for ch in set(target)}
    work_str = source * 2
    match_dicts = {}
    for i in range(len(source)-1):
        d_source = {}

        for j in range(i, i+len(source)-1):

            if work_str[j] in set(target):

                if d_source.get(work_str[j], 0):
                    d_source[work_str[j]] += 1
                else: 
                    d_source[work_str[j]] = 1

                if d_target == d_source:
                    match_dicts[work_str[i:j+1]] = j - i + 1

    if match_dicts:
        print(match_dicts)
        return match_dicts[min(match_dicts, key=match_dicts.get)]                
    else:
        return -1



print(circ('hackerrank', 'krr'))