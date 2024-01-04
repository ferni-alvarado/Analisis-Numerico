def horn(a, x):
    n = len(a)
    b = a[0]
    for idx in range(1,n):
        b = a[idx] + x*b 
    
    return b

p = horn([1, -5, 6, 2], 2)
print(p)
