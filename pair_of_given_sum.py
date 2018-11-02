from collections import defaultdict
#using Hash table

#Time complexity - O(n), Space complexity - O(n)
def find_pair(arr,x):
    ele_dict = defaultdict(int)
    res = []
    for ele in arr:
        ele_dict[ele] = 1
    for ele in arr:
        if abs(x-ele) and ele_dict[abs(x-ele)] == 1:
            res.append((ele,abs(x-ele)))
            ele_dict[ele] = 0
    return res

print(find_pair([1,3,2,4,6,5],9))
