# Task 1

a = int(input())
b = int(input())

print((a ** 2 + b ** 2) ** 0.5)

# Task 2

num = input()
print(num[1])

# Task 3

a = int(input())

try:
    print(int(a / (a % 2)) + 1)
except:
    print(a + 2)

# Task 4

num = int(input())

res = 9 * 60 + num * 45 + num // 2 * 5 + (num - 1) // 2 * 15

print(res // 60, res - res // 60 * 60)

# Task 5

a = int(input())
b = int(input())

if a > b:
    print(1)
elif a < b:
    print(2)
else:
    print(0)

# Task 6

a = input()
b = input()
c = input()

print(max(a,b,c))

# Task 7

x1 = input()
y1 = input()
x2 = input()
y2 = input()

if x1 == x2 or y1 == y2:
    print("YES")
else:
    print("NO")

# Task 8

a = int(input())
b = int(input())
c = int(input())

if a + b > c and a + c > b and c + b > a:
    print("YES")
else:
    print("NO")

# Task 9

a = input()
b = input()
c = input()
res = 0

if a == b and a != c:
    print(2)
elif a == c and a != b:
    print(2)
elif b == c and b != a:
    print(2)
elif a == b == c:
    print(3)
else:
    print(0)

# Task 10

a = input()
b = input()
c = input()

if a >= b:
    a,b = b,a
if a >= c:
    a,c = c,a
if b >= c:
    b,c = c,b

print(a,b,c)
