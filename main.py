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
            init_wallet['USD'] -= VAL
            init_wallet['KZT'] += amount * VAL
        else:
            print("You do not have enough money")
    else:
        if init_wallet['KZT'] >= amount:
            init_wallet['KZT'] -= VAL
            init_wallet['USD'] += amount / VAL
        else:
            print("You do not have enough money")

while True:
    print("1. Check your balance")
    print("2. Add money")
    print("3. Subtract money")
    print("4. Transfer money")
    print("5. Exit")
    choice = input()
    if choice == '1':
        print(f'KZT: {init_wallet["KZT"]}')
        print(f'USD: {init_wallet["USD"]}')
    elif choice == '2':
        money = float(input('Enter amount of money to add'))
        currency = input("Enter currency of money")
        if currency == "KZT":
            add_money(money,True)
        else:
            add_money(money,False)
    elif choice == '3':
        money = float(input('Enter amount of money to subtract'))
        currency = input("Enter currency of money")
        if currency == "KZT":
            get_money(money,True)
        else:
            get_money(money,False)
    elif choice == '4':
        money = float(input('Enter amount of money to transfer'))
        curr1 = input("Enter from what currency to transfer")
        curr2 = input("Enter to what currency to transfer")
        transfer(money,curr1,curr2)
    else:
        break
