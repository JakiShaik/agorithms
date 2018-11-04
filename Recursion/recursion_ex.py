def a(n):
    if n > 0:
        print(n)
        return a(n-1)
    print('Finished')

a(3)
        
