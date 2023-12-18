def counter(start=0):
    def step():
        nonlocal start
        start += 1
        return start
    
    return step


c1 = counter(1)
c1()
c1()
print(c1())