class Human:

    def __init__(self, name: str, age: int, money: int ):
        self.name = name
        self.age = age
        self.money = money

    def info(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        if self.money >= 0:
            print(f"Money: {self.__money}")
        print(f'Money status: debt in the amount of {self.money * (-1)}')

    def earn_money(self, salary):
        if salary <= 0:
            raise ValueError('Salary less than zero')
        self.money += salary
        print(f'You have earned {salary}, now your balance is:{self.money}')


class User:

    logins = set()

    def __init__(self, login: str, password: str):
        if login in User.logins:
            raise ValueError('Логин уже занят')
        User.logins.add(login)
        self.login = login
        if len(password) < 6:
            raise ValueError(f'Слишком короткий пароль')
        if not password.isalnum:
            raise TypeError('Пароль должен быть буквенно- цифровым')
        self.password = password

    def change_login(self, new_login: str):
        if self.login == new_login:
            raise TypeError('Логин Вами был уже использован')
        self.login = new_login


    def change_password(self, new_password: str):
        if len(new_password) < 6:
            raise ValueError(f'Слишком короткий пароль')
        if not new_password.isalnum:
            raise TypeError('Пароль должен быть буквенно- цифровым')
        if self.login == new_password:
            raise TypeError('Пароль слишком простой')
        self.password = new_password

class Point:

    def __init__(self, x: int, y: int, z: int):
        if not isinstance((x, y, z), int):
            raise TypeError('координаты должны быть числом')
        self.x = x
        self.y = y
        self.z = z

    def move_to(self, new_x, new_y, new_z):
        ...

    def get_distance(self, other_point):
        ...