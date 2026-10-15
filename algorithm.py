a = int(input("Enter a: "))
b = int(input("Enter b: "))
c = int(input("Enter c: "))

# compare and swap
if a > b:
    a, b = b, a

if a > c:
    a, c = c, a

if b > c:
    b, c = c, b

print("Sorted:", a, b, c)