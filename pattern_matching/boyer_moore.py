from collections import defaultdict

#O(m)
def fill_hash_table(pat):
    pat_dict = defaultdict(int)
    for i,char in enumerate(pat):
        pat_dict[char] = i
    return pat_dict

def search(txt,pat):
    l_txt = len(txt)
    l_pat = len(pat)
    
    pat_dict = fill_hash_table(pat)
    
    s = 0

    while (s <= l_txt-l_pat):
        j = l_pat-1 #Starting from the end of the pattern
        while (j>=0 and txt[s+j] == pat[j]):
            j -=1
        if j<0:
            print("Pattern match found at "+str(s))
            s = s+l_pat-pat_dict[txt[s+l_pat]] if s+l_pat<l_txt else 1
        else:
            s = s + max(1,j-pat_dict[txt[s+j]])
        
        
        
search('which-finally-halts.--at-that-point','at-that')
