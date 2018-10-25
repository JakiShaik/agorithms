#Brute Force

def max_sub(arr):
    l = len(arr)
    max_i = 0
    max_j=0
    sum_arr=[]
    for i in range(l):
        for j in range(i,l):
            sum_arr.append((sum(arr[i:j+1]),i,j))
    #print(sum_arr)
    #print(max(sum_arr))
    return arr[max(sum_arr)[1]:max(sum_arr)[2]+1]


#Kadane's algorithm
def max_sub_1(a):
    curr_max = a[0]
    max_so_far = a[0]
    left = 0
    right = 0
    if max(arr) < 0:
        return [max(arr)]
    if min(arr)>=0:
        return arr
    for i in range(1,len(a)):
        if a[i] > curr_max+a[i]:
            left = i
        curr_max = max(a[i],curr_max+a[i])
        if curr_max > max_so_far:
            right = i
        max_so_far = max(max_so_far,curr_max)
    #print(left,right)
    return a[left:right+1]


print(max_sub([1,-3,2,1,-1]))
print(max_sub([-1,-2,-3,-4]))
print(max_sub([1,2,3,4,5]))
print(max_sub([-2,-3,4,-1,-2,1,5,-3]))
arr = [-2,-3,4,-1,-2,1,5,-3]
print('arr is '+str(arr))
print(max_sub_1(arr))
arr = [1,-3,2,1,-1]
print('arr is '+str(arr))
print(max_sub_1(arr))
arr = [-1,-2,-3,-4]
print('arr is '+str(arr))
print(max_sub_1(arr))
arr = [1,2,3,4,5]
print('arr is '+str(arr))
print(max_sub_1(arr))
