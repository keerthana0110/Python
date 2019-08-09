def no_notes(a):
    N=[500,200,100,50,20,10]
    x=0
    for i in range(6):
        n=N[i]
        x+=int(a/n)
        a=int(a%n)
    if a>0:
        x=-1
    return x
print(no_notes(600))
print(no_notes(1000))
        
