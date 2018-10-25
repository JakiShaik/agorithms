from collections import defaultdict
def check(s):
    open,close = [],[]
    for char in s:
        if char == '(':
            open.append(char)
        elif char == ')':
            if len(open) > 0:
                open.pop()
            else:
                close.append(char)
    return len(close)+len(open)
if __name__ == '__main__':
    s = input()
    print(check(s))

    
