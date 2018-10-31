def find_r(a,ele,l_ind,r_ind):
    if l_ind > r_ind:
        return None
    mid = l_ind + (r_ind-l_ind) //2
    if ele == a[mid]:
        return mid
    if ele < a[mid]:
        r_ind = mid-1
        return find_r(a,ele,l_ind,r_ind)
    elif ele > a[mid]:
        l_ind = mid+1
        return find_r(a,ele,l_ind,r_ind)


#Non-recursive algo
def find(a,target):
    l_index = 0
    r_index = len(a)-1
    
    while (l_index <= r_index):
        m_index = l_index + (r_index-l_index)//2
        if target == a[m_index]:
            return m_index
        if target < a[m_index]:
            r_index = m_index-1
        elif target > a[m_index]:
            l_index = m_index+1
    return None



print('Searching for 1 in [1,2,3,4,5,6] '+str(find([1,2,3,4,5,6],1)))
print('Searching for 6 in [1,2,3,4,5,6] '+str(find([1,2,3,4,5,6],6)))
print('Searching for 7 in [1,2,3,4,5,6] '+str(find([1,2,3,4,5,6],7)))
print('#########')
print('[Recursive] Searching for 1 in [1,2,3,4,5,6] '+str(find_r([1,2,3,4,5,6],1,0,5)))
print('[Recursive] Searching for 6 in [1,2,3,4,5,6] '+str(find_r([1,2,3,4,5,6],6,0,5)))
print('[Recursive] Searching for 7 in [1,2,3,4,5,6] '+str(find_r([1,2,3,4,5,6],7,0,5)))
