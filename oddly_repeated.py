
def find_odd(a):
    res = a[0]
    for ele in a[1:]:
        res = res ^ ele
    return res

print(find_odd([3,2,2,1,1,3,2]))