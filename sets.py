def union(set1, set2):
    return [ i for i in set1 for j in set2 if j not in set1 ]

def intersection(set1, set2):
    return [ i for i in set1 if i in set2 ]

def set_diff(set1, set2):
    return

print '[1,2,3] U [2,3,4]:', union([1,2,3], [2,3,4])
print '[1,2,3] \ [2,3,4]:', intersection([1,2,3], [2,3,4])
