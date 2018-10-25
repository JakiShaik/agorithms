import sys

list1 = input().split(' ')
#print(list1)
input_list = list(map(int,list1))
#input_list = []
#input_list.append(list1)

print(input_list)

def calculate_inv(tupleA,tupleB):
    leftArr, lef_inv = tupleA
    rightArr, rig_inv = tupleB
    #print('leftArr is '+str(leftArr))
    #print('rightArr is '+str(rightArr))
    res = []
    count = lef_inv+rig_inv
    ll = len(leftArr)
    lr = len(rightArr)
    i,j = 0,0
    while i < ll and j < lr:
        #print(rightArr[j])
        if leftArr[i] <= rightArr[j]:
            res.append(leftArr[i])
            i +=1
        else:
            res.append(rightArr[j])
            j +=1
            count += len(leftArr)-i
    res.extend(leftArr[i:])
    res.extend(rightArr[j:])
    return res,count
def num_inversions(arr):
    length = len(arr)
    #print(length)
    if length <= 1:
        return arr,0
    return calculate_inv(num_inversions(arr[:length//2]),num_inversions(arr[length//2:]))


sor,count = num_inversions(input_list)

print(sor)
print(count)

