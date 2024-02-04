def recursion(i):
    print(i)
    if i <= 1:
        return
    else:
        recursion(i-1)


recursion(5)
