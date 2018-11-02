#Find the maximum difference between two elements
#such that the elements are in ascending order.

def find_max_diff(a):
    min_so_far = a[0]
    max_diff = 0
    for ele in a[1:]:
        if ele <= min_so_far:
            min_so_far = ele
        elif ele-min_so_far > max_diff:
            max_diff = ele-min_so_far
    print(max_diff)

#calculating using Maximum Sum subarray - The maximum sum subarray value is the largest difference that is possible
def find_max_diff1(a):
    l = len(a)
    diff = []
    #Create a differance array
    for i in range(l-1):
        diff.append(a[i+1]-a[i])
    a = diff
    #Calculate the max_sum_sub_array of diff array.
    curr_max = a[0]
    max_so_far = a[0]
    for i in range(1, len(a)):
        curr_max = max(a[i], curr_max + a[i])
        max_so_far = max(max_so_far, curr_max)
    # print(left,right)
    return max_so_far

find_max_diff([4,3,10,2,9,1,6])
find_max_diff([3,1,4,7,5,100,10])
print(find_max_diff1([4,3,10,2,9,1,6]))
