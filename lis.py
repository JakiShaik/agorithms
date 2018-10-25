from collections import defaultdict

def solution(back,max_pos):
    res = [max_pos]
    pos = max_pos
    while back[pos] in back:
        pos = back[pos]
        res = [pos]+res
    return res

def lis(lst):
    len_dict = defaultdict(int)
    back = defaultdict(int)
    max_pos = -1
    back[lst[0]] = -99999999
    for i,ele in enumerate(lst):
        len_dict[ele] = 1
        for key in len_dict.keys():
            if ele > key and 1+len_dict[key] > len_dict[ele]:
                len_dict[ele] = 1+len_dict[key]
                back[ele] = key
                max_pos = ele
    #print(len_dict)
    #print(max_pos)
    #print(back)
    return max(len_dict.values()), solution(back,max_pos)
if __name__ == '__main__':
    s = [int(i) for i in input().split()]
    print(lis(s))
        
    
    
