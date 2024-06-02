class Car:
    def __init__(self, car: str, year_born_car: str, price_car: int, drive: int):
        self.car = car
        self.year_born_car = year_born_car
        self.price_car = price_car
        self.drive = drive
        self.price_car_after_drive = 0
        pass


    def __str__(self):
        return f'Car: {self.car}, Year_born_car: {self.year_born_car}, Price_car: {self.price_car}, Drive: {self.drive}'


    def __repr__(self) -> str:
        return f'Car: {self.car}, Year_born_car: {self.year_born_car}, Price_car: {self.price_car}, Drive: {self.drive}'


    def buy_price(self):
        price_car = self.price_car
        price = 0
        km = 0
        while km < self.drive:
            price += 10
            km += 1
        else:
            by_price = price_car - price
            self.price_car_after_drive += by_price
            return f'The {self.car} has price {str(by_price) + '$'}'


    @property
    def rate_car(self):
        if self.price_car_after_drive >= 10_000_000:
            return 'Elite class car'
        elif 2_000_000 <= self.price_car_after_drive < 10_000_000:
            return 'Middle class car'
        else:
            return 'Economy class car'





my_car = Car(car='lamborghini', year_born_car='2007', price_car=1_000_000, drive=124444)
print(my_car.buy_price())
print(my_car.rate_car)
