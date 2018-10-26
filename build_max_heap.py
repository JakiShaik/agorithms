def build_max_heap(a):
    def max_heapify(a,i):
        left = 2*i+1
        right = 2*i+2
        largest = i
        if (left<len(a) and a[left]>a[i]):
            largest = left
        elif (right < len(a) and a[right]>a[largest]):
            largest = right
        if largest != i:
            a[i],a[largest] = a[largest],a[i]
            max_heapify(a,largest)
    heap_size = len(a)
    for i in range(heap_size//2,-1,-1):
        max_heapify(a,i)
    return a
print(build_max_heap([9,6,5,0,8,2,13]))
