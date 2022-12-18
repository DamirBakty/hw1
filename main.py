from dataclasses import dataclass, field
from enum import Enum
import copy

db = []
class Account(Enum):
    KZT = 'KZT'
    RUB = 'RUB'
    USD = 'USD'
    prices = {
         "KZT": 1,
         "USD": 470,
         "RUB": 7
         }


@dataclass(frozen=True)
class BankAccount:
    name: str
    surname: str
    wallet: dict = field(default_factory=dict)

    def add_money(self, amount: float, currency: str):
        if currency == Account.KZT.value:
            self.wallet[Account.KZT.value] = self.wallet[Account.KZT.value] + amount if Account.KZT.value in self.wallet else amount
            return
        if currency == Account.RUB.value:
            self.wallet[Account.RUB.value] = self.wallet[Account.RUB.value] + amount if Account.RUB.value in self.wallet else amount
            return
        if currency == Account.USD.value:
            self.wallet[Account.USD.value] = self.wallet[Account.USD.value] + amount if Account.USD.value in self.wallet else amount
            return

    def subtract_money(self, amount: float, currency: str):
        if currency == Account.KZT.value:
            if not self.wallet[Account.KZT.value] or self.wallet[Account.KZT.value] < amount:
                print("You do not have enough money!")
                return
            self.wallet[Account.KZT.value] -= amount
            return
        if currency == Account.RUB.value:
            if not self.wallet[Account.RUB.value] or self.wallet[Account.RUB.value] < amount:
                print("You do not have enough money!")
                return
            self.wallet[Account.RUB.value] -= amount
            return
        if currency == Account.USD.value:
            if not self.wallet[Account.USD.value] or self.wallet[Account.USD.value] < amount:
                print("You do not have enough money!")
                return
            self.wallet[Account.USD.value] -= amount
            return

    def transfer(self, amount: float, currency1: str, currency2: str):
        if self.wallet[currency1] < amount\
                or currency1 not in self.wallet:
            print("You do not have enough money!")
            return
        self.wallet[currency1] -= amount
        self.wallet[currency2] = self.wallet[currency2] + amount * (Account.prices.value[currency1] / Account.prices.value[currency2])\
                                 if currency2 in self.wallet else amount * (Account.prices.value[currency1] / Account.prices.value[currency2])


    def __str__(self):
        return f"Name: {self.name},\n" \
               f"Surname: {self.surname},\n" \
               f"Money: {self.wallet}"



while True:
    print("1. Create bank account")
    print("2. Choose bank account")
    print("0. Exit")
    choice = input()
    if choice == "1":
        name = input("Enter your name: ")
        surname = input("Enter your surname: ")
        account = BankAccount(name=name, surname=surname)
        db.append(copy.deepcopy(account))
    if choice == "2":
        name = input("Enter your name: ")
        surname = input("Enter your surname: ")
        for acc in db:
            if acc.name == name and acc.surname == surname:
                account = acc
                break
        print(account)
    if choice == "0":
        break
