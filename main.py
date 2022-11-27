# Task 1
a = int(input())
b = int(input())

if a % 2 == 1:
    for i in range(a+1,b + 1,2):
        print(i, end=" ")
else:
    for i in range(a,b + 1,2):
        print(i, end=" ")
# Task 2

a = int(input())

for i in range(2,a+1):
    if a % i == 0:
        print(i)
        break

# Task 3

a = int(input())

for i in range(1, a+1):
    if a % i == 0:
        print(i, end=" ")

# Task 4

num = int(input())
res = 0

for i in range(num):
    res += int(input())

print(res)

# Task 5

a = input()
res = 0

for i, num in enumerate(a):
    res += int(num) * 2 ** (len(a) - 1 - i)

print(res)

# Task 6

def power(a, b):
    res = 1
    for i in range(b):
        res *= a
    return res

a = int(input())
b = int(input())

print(power(a,b))

# # Task 7

def election(x, y, z):
    if x == y:
        return x
    return z

x,y,z = input().split()

print(election(x,y,z))

# Task 8

VAL = 470
init_wallet = {'USD': 0.0,
               'KZT': 0.0}
def add_money(amount: float, currency_kzt: bool):
    if currency_kzt:
        init_wallet['KZT'] += amount
    else:
        init_wallet['USD'] += amount

def get_money(amount: float, currency_kzt: bool):
    if currency_kzt:
        if init_wallet['KZT'] >= amount:
            init_wallet['KZT'] -= amount
        else:
            print("You do not have enough money")
    else:
        if init_wallet['USD'] >= amount:
            init_wallet['USD'] -= amount
        else:
            print("You do not have enough money")
def transfer(amount, currency1, currency2):
    if currency1 == "USD" and currency2 == "KZT":
        if init_wallet['USD'] >= amount:
            init_wallet['USD'] -= amount * VAL
            init_wallet['KZT'] += amount * VAL
        else:
            print("You do not have enough money")
    else:
        if init_wallet['KZT'] >= amount:
            init_wallet['KZT'] -= amount * VAL
            init_wallet['USD'] += amount * VAL
        else:
            print("You do not have enough money")

