from itertools import count
import re
from random import choice
from products import names, price, raiting


class IdCounter:

    '''Class that contain a generator of user_id and product_id'''
    product_id_count = count(1)
    user_id_count = count(1)

    @staticmethod
    def give_current_id_product():
        return IdCounter.product_id_count

    @staticmethod
    def give_current_id_user():
        return IdCounter.user_id_count



class Password:
    '''Class for set passwords'''
    def __init__(self, password):
        if self.is_valid(password):
            self._password = password
        self.__hash_pass = self.get(password)


    def get(self, password): #function that get hash value from password
        if self.is_valid(password):
            self.password = password
        self.hash_password = hash(self.password)
        return self.hash_password


    def is_valid(self, password: str): #function that checks password correctness
        if not isinstance(password, str):
            raise TypeError('Password should be string type')
        if not re.fullmatch(r'[A-Za-z0-9@#$%^&+=]{8,}', password):
            raise ValueError('Password should contain letters, numbers, special symbols and have len 8 or more')
        return True

    def check(self, password): #function that checks hash value of password
        if self.is_valid(password):
            return self.__hash_pass == hash(password)


    @property
    def password(self):
        return self._password


    @password.setter
    def password(self, password):
        self.__password = password


    @property
    def hash_pass(self):
        return self.__hash_pass




class Product:

    '''Class that contain info about products'''

    def __init__(self, name: str, price: float, rating: float):
        self.__id = next(IdCounter.product_id_count)
        if not isinstance(name, str):
            raise TypeError('name of product must be str')
        self.__name = name
        if not isinstance(price, float):
            raise TypeError('price of product must be float')
        self.__price = price
        if not 0 < rating <= 5:
            raise ValueError('Rating of product must be between 1 and 5')
        if not isinstance(price, float):
            raise TypeError('rating of product must be float')
        self.__rating = rating

    @property
    def id(self):
        return self.__id

    @property
    def name(self):
        return self.__name

    @property
    def price(self):
        return self.__price

    @property
    def rating(self):
        return self.__rating


    def __repr__(self):
        return f'Product: {self.__name}'

    def __str__(self):
        return f'Product: {self.__id}_{self.__name}'

    def __getitem__(self):
        return self.__price


class Cart:
    '''Class that have product list which contain of Product objects'''
    def __init__(self):
        self.__product_list = []


    @property
    def product_list(self):
        return self.__product_list


    def add_product(self, other: Product): # function that can add 1 product to Cart
        if not isinstance(other, Product):
            raise TypeError('Only Products can be in Cart')
        self.__product_list.append(other)
        print(f'{other.name} added in Cart')

    def give_products(self, number): # function that can add products with number argument to Cart
        for i in range(number):
            self.__product_list.append(Product(choice(names), choice(price), choice(raiting)))
    
    def give_final_price(self):  # function that calculate final price of products in cart
        return sum(self.__product_list)
    
    def remove_product(self): # function that can delete product from your cart
        while True:
            inp = input('What product do u want to remove? : ')
            for product in self.__product_list:
                if inp.lower() == product.name.lower():
                    self.__product_list.remove(product)
                    print(self.__product_list)
            if inp.lower() == 'cancel':
                break

    def __str__(self) -> str :
        return str(self.__product_list)


class User:
    '''Class that contain info about User'''
    username_list = []

    def __init__(self, username, password):
        self.__id = next(IdCounter.user_id_count)
        if username in User.username_list:
            raise ValueError('This username already taken')
        self.__username = username
        User.username_list.append(username)
        self.__password = Password(password)
        self.__cart = Cart()

    @property
    def id(self):
        return self.__id

    @property
    def username(self):
        return self.__username

    @property
    def password(self):
        return self.__password

    @password.setter
    def password(self, password):
        self.__password = password



    @property
    def cart(self):
        return self.__cart

    @cart.setter
    def cart(self, cart):
        self.__cart = Cart()


    def __repr__(self):
        return f'User: {self.__username}'

    def __str__(self):
        return f'User: {self.__id}_{self.__username} Password: password{str(self.__id)}'



class Store:
    '''Class that can interact with programm user in terminal'''
    users = []

    @classmethod
    def start(cls):
        while True:
            name = str(input("Welcome to our store!\nLet's register.Please, enter your Name: "))
            print(f'Nice to meet you, {name}!')
            password = str(input('Lets set password!'))
            print('All right! Now you can go for shopping!')
            new_user = User(name, password)
            Store.users.append(new_user)
            print(Store.users)
            print(f"{name} would you like to add some products in your cart?: ")
            answer = input()
            if answer.lower() == 'yes':
                num = int(input("How much products do you want to add?: "))
                new_user.cart.give_products(num)
                print(f'Nice! Now you have: \n{new_user.cart}')
                print('Would you like to pay this right now?')
                new_answer = input()
                if new_answer.lower() == 'yes':
                    print(f'Ok! Lets go to pay. Final price is: {round(sum([i.price for i in new_user.cart.product_list]), 2)}')
                    payment = input("Attach the card please: ")
                    if payment.lower() == 'pay':
                        print('Thank you for choosing our store!\nWe hope to meet you again.\nBye! :)')
                        break



if __name__ == '__main__':
    a = Store()
    Store.start()


