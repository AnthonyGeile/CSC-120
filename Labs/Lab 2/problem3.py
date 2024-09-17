def merg_dicts(d1, d2):
    merged = {}
    for i in d1.items():
        if i in merged:
            merged[i[0]] += i[1]
        else:
            merged[i[0]] = i[1]
    for i in d2.items():
        if i in merged.items():
            merged[i[0]] += i[1]
        else:
            merged[i[0]] = i[1]
    return merged

print(merg_dicts({'t':4, 'x':2, 'z':5}, {'b':3, 'x':1, 't':2, 'c':9}))