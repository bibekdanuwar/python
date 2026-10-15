x = int(input("please enter 1st number "))
y = int(input("please enter 2nd number "))
bigger = 0
smaller = 0
total = 0
if x > y:
    bigger = x
    smaller = y
else:
    bigger = y
    smaller = x
    
while smaller <= bigger:
    total += smaller
    smaller += 1

print(total)