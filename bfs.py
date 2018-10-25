def printLevel(tree,level):
    if tree == []:
        return
    if level == 1:
        print(tree[1])
    else:
        printLevel(tree[0],level-1)
        printLevel(tree[2],level-1)
def bfs(tree,level):
    for i in range(1,level+1):
        printLevel(tree,i)
bfs([[[[], 1, []], 2, [[], 3, []]], 4, [[[], 5, []], 6, [[], 7, [[], 9, []]]]],4)
