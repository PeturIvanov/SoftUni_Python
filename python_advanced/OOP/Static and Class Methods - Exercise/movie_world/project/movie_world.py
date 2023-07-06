from typing import List

from project.dvd import DVD
from project.customer import Customer


class MovieWorld:
    DVD_CAPACITY = 15
    CUSTOMER_CAPACITY = 10
    def __init__(self, name: str):
        self.name = name
        self.customers: List[Customer] = []
        self.dvds: List[DVD] = []

    def __repr__(self):
        movie_world_data = []
        movie_world_data.extend([str(c) for c in self.customers])
        movie_world_data.extend([str(d) for d in self.dvds])

        return "\n".join(movie_world_data)

    @staticmethod
    def dvd_capacity() -> int:
        return MovieWorld.DVD_CAPACITY

    @staticmethod
    def customer_capacity() -> int:
        return MovieWorld.CUSTOMER_CAPACITY

    def add_customer(self, customer: Customer) -> None:
        if len(self.customers) < MovieWorld.customer_capacity():
            self.customers.append(customer)

    def add_dvd(self, dvd: DVD) -> None:
        if len(self.dvds) < MovieWorld.dvd_capacity():
            self.dvds.append(dvd)

    def __find_customer(self, customer_id: int) -> Customer:
        return next(filter(lambda x: x.id == customer_id, self.customers))

    def __find_dvd(self, dvd_id) -> DVD:
        return next(filter(lambda x: x.id == dvd_id, self.dvds))

    def rent_dvd(self, customer_id: int, dvd_id: int) -> str:
        customer = self.__find_customer(customer_id)
        dvd = self.__find_dvd(dvd_id)

        if dvd in customer.rented_dvds:
            return f"{customer.name} has already rented {dvd.name}"

        if dvd.is_rented:
            return "DVD is already rented"

        if customer.age < dvd.age_restriction:
            return f"{customer.name} should be at least {dvd.age_restriction} to rent this movie"

        customer.rented_dvds.append(dvd)
        dvd.is_rented = True

        return f"{customer.name} has successfully rented {dvd.name}"

    def return_dvd(self, customer_id, dvd_id):
        customer = self.__find_customer(customer_id)
        dvd = self.__find_dvd(dvd_id)

        if dvd not in customer.rented_dvds:
            return f"{customer.name} does not have that DVD"

        dvd.is_rented = False
        customer.rented_dvds.remove(dvd)

        return f"{customer.name} has successfully returned {dvd.name}"
