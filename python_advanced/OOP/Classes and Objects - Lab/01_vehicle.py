class Vehicle:
    def __init__(self, mileage: int, max_speed: int=150):
        self.mileage = mileage
        self.gadgets = []
        self.max_speed = max_speed


car = Vehicle(20)
print(car.max_speed)
print(car.mileage)
print(car.gadgets)
car.gadgets.append('Hudly Wireless')
print(car.gadgets)