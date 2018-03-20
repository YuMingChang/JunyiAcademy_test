#exclude = lambda n:len([i for i in range(1, n+1) if i%15 == 0 elif not i%3==0 elif not i%5==0 else None])
def exclude(n):
    l = list()
    for i in range(1, n+1):
        if not i%15 or (i%3 and i%5):
            l.append(i)
    
    return len(l)

print(exclude(15))

