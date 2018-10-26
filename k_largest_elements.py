#O(logn)
def max_heapify(a,i):
    left = 2*i+1
    right = 2*i+2
    largest = i
    if (left<len(a) and a[left]>a[i]):
        largest = left
    if (right < len(a) and a[right]>a[largest]):
        largest = right
    if largest != i:
        a[i],a[largest] = a[largest],a[i]
        max_heapify(a,largest)

#O(n)
def build_max_heap(a):
    heap_size = len(a)
    for i in range(heap_size//2,-1,-1):
        #print('i is '+str(i)+' a[i] is '+str(a[i]))
        max_heapify(a,i)
    return a

#O(1)
def max_extract(a):
    if len(a) < 1:
        return "Heap underflow"
    max = a[0]
    a[0],a[len(a)-1] = a[len(a)-1],a[0]
    a.pop()
    #print('a after popping is '+str(a))
    return max

#O(n+klogn)
def k_largest(a,k):
    a = build_max_heap(a)
    print(a)
    res = []
    for _ in range(k):
        res.append(max_extract(a))
        max_heapify(a,0)
    return res

#print('############')
print(k_largest([9,6,5,0,8,2,13],4))
#print(build_max_heap([5,8,9,0,6,2]))    
