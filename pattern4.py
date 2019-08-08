def pattern(n):
    for i in range (1,6):
        for j in range (5,i-1,-1):
            print ("*",end=" ")
        print ("\r")
n=5
pattern(n)
