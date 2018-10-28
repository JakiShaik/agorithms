def find_match(str1,str2):
    size1 = len(str1)
    size2 = len(str2)
    for i in range(size1-size2+1):
        for j in range(size2):
            if str1[i+j] != str2[j]:
                break
        if j == size2-1:
            print('pattern found at '+str(i))


find_match("abcdkhjdhjabckjdabcc","abc")
