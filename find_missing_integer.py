from collections import defaultdict
#O(n) solution
def find_missing(arr):
    if max(arr) < 0 or arr == []:
        return 1
    ind_dict= defaultdict(int)
    for i in range(1,len(arr)+1):
        ind_dict[i] = 0
    for ele in arr:
        if ele in ind_dict:
            ind_dict[ele] = 1
    for key in ind_dict:
        if ind_dict[key] == 0:
            return key



# Looks like O(n^2) but the system has accepted with 48ms 
def find_missing1(arr):
    if max(arr) < 0:
        return 1
    for i,_ in enumerate(arr):
        if i+1 not in arr:
            return i+1
    return max(arr)+1
