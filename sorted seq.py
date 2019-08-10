seq=input("input some coma separated words")
seq1=seq.split(',')
seq1.sort()
for word in seq1:
    print(word,end=',')
