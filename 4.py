class Car:
    def __init__(self, brand, model, color, vin_code, price):
        self.brand = brand
        self.model = model
        self.color = color
        self.vin_code = vin_code
        self.price = price

    def __str__(self):
        return f"{self.brand} - {self.model}, color: {self.color}, vin-code: {self.vin_code}, price: €{self.price}"

    def __repr__(self):
        return f"Car(brand={self.brand}, model={self.model}, color={self.color}, vin-code={self.vin_code}, price={self.price})"


class Showroom:
    def __init__(self, name):
        self.name = name
        self.cars_list = []

    def add_car(self, car):
        if car not in self.cars_list:
            self.cars_list.append(car)
            print(f"+++ The vehicle {car} has been added")
        else:
            print(f"XXX The vehicle {car} already IS in the showroom.")

    def remove_car(self, car):
        if car in self.cars_list:
            self.cars_list.remove(car)
            print(f"--- The vehicle {car} has been sold")
        else:
            print(f"XXX The vehicle {car} ISN'T in the showroom.")

    def show_cars(self):
        print(f"\nCars in {self.name}:")
        for i, car in enumerate(self.cars_list, 1):
            print(f"{i}: {car}")
        print()


car1 = Car("Rolls Royce", "Cullinan", "White Pearl", "vin0001", 450000)
car2 = Car("Maserati", "Levante", "Silver", "vin0002", 120000)
car3 = Car("Mercedes", "S500", "Black", "vin0003", 210000)
car4 = Car("Lucid", "Air", "Gold", "vin0004", 180000)
car5 = Car("Suzuki", "Swift", "Grey", "vin0005", 20000)


lux_sr = Showroom("Alex's Showroom")
lux_sr.add_car(car1)
lux_sr.add_car(car2)
lux_sr.add_car(car3)
lux_sr.add_car(car3)
lux_sr.add_car(car4)
lux_sr.add_car(car5)

lux_sr.show_cars()

lux_sr.remove_car(car1)
lux_sr.remove_car(car1)
lux_sr.show_cars()
