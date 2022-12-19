from dataclasses import dataclass

@dataclass(frozen=True)
class Person:
    name: str
    surname: str
    age: int

    def toString(self):
        return f"Name: {self.name}\nSurname: {self.surname}\nAge: {self.age}"

@dataclass(frozen=True)
class Driver(Person):
    work_experience: int


    def toString(self):
        return f"Name: {self.name}" \
               f"\nSurname: {self.surname}" \
               f"\nAge: {self.age}" \
               f"\n Work_experience: {self.work_experience}"

@dataclass(frozen=True)
class Engine:
    power: int
    creator: str

    def toString(self):
        return f"Power: {self.power}\n" \
               f"Creator: {self.creator}"

@dataclass(frozen=True)
class Car:
    brand: str
    carClass: str
    weight: float
    driver: Driver
    engine: Engine

    def toString(self):
        return f"Brand: {self.brand}\n" \
               f"carClass: {self.carClass}\n" \
               f"Weight: {self.weight}\n" \
               f"Driver: {self.driver.toString()}\n" \
               f"Engine: {self.engine.toString()}"

    @staticmethod
    def start():
        print("Поехали")

    @staticmethod
    def stop():
        print("Останавливаемся")

    @staticmethod
    def turnLeft():
        print("Поворот налево")

    @staticmethod
    def turnRight():
        print("Поворот направо")



@dataclass(frozen=True)
class Lorry(Car):
    carrying: int

    def toString(self):
        return super().toString() + \
                f"\nCarrying: {self.carrying}"

@dataclass(frozen=True)
class SportCar(Car):
    speed: float

    def toString(self):
        return super().toString() + \
                f"\nCarrying: {self.speed}"
