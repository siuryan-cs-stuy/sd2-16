def union(set1, set2):
    return [ i for i in set1 ] + [ j for j in set2 if j not in set1 ]

def intersection(set1, set2):
    return [ i for i in set1 if i in set2 ]

def set_diff(set1, set2):
    return [ i for i in set1 if i not in set2 ]

def sym_diff(set1, set2):
    return set_diff(union(set1, set2), intersection(set1, set2))

def cart_prod(set1, set2):
    return [ [i, j] for i in set1 for j in set2 ]

print '[1,2,3] U [2,3,4]:', union([1,2,3], [2,3,4])
print '[1,2,3] I [2,3,4]:', intersection([1,2,3], [2,3,4])
print '[1,2,3] \ [2,3,4]:', set_diff([1,2,3], [2,3,4])
print '[2,3,4] \ [1,2,3]:', set_diff([2,3,4], [1,2,3])
print '[1,2,3] D [2,3,4]:', sym_diff([1,2,3], [2,3,4])
print '[1,2] x [red, white]:', cart_prod([1,2], ['red', 'white'])
