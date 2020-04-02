import random as r
num= r.randint(0,10)
for x in range(num): print(" "*(num-x)+ ""+'* '*x)

for x in range(num): print(" "*x +""+ '* '*(num-x))
