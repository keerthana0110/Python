from collections import Counter
d1={'a':100,'b':200}
d2={'a':44,'b':53}
d=Counter(d1)+Counter(d2)
print(d)
