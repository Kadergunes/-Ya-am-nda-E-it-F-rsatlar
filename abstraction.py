from abc import ABC, abstractmethod


class Vehicle(ABC):
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    @abstractmethod
    def start_engine(self):
        pass

    @abstractmethod
    def stop_engine(self):
        pass


class Car(Vehicle):
    def __init__(self, brand, model, fuel_type):
        super().__init__(brand, model)
        self.fuel_type = fuel_type

    def start_engine(self):
        print(f'{self.brand} {self.model} ({self.fuel_type}) motoru çalıştırıldı.')

    def stop_engine(self):
        print(f'{self.brand} {self.model} motoru durduruldu.')


class Motorcycle(Vehicle):
    def __init__(self, brand, model, engine_capacity):
        super().__init__(brand, model)
        self.engine_capacity = engine_capacity

    def start_engine(self):
        print(f"{self.brand} {self.model} ({self.engine_capacity}cc) motoru çalıştırıldı.")

    def stop_engine(self):
        print(f'{self.brand} {self.model} motoru durduruldu.')


class ElectricCar(Vehicle):
    def __init__(self, brand, model, battery_capacity):
        super().__init__(brand, model)
        self.battery_capacity = battery_capacity

    def start_engine(self):
        print(f'{self.brand} {self.model} elektrik motoru çalıştırıldı.')

    def stop_engine(self):
        print(f'{self.brand} {self.model} elektrik motoru durduruldu.')


car = Car('Toyota', 'Corolla', 'Benzin')
motorcycle = Motorcycle('Honda', 'w123', 600)
electric_car = ElectricCar('Tesla', 'Model 3', '75kWh')


car.start_engine()
car.stop_engine()

motorcycle.start_engine()
motorcycle.stop_engine()

electric_car.start_engine()
electric_car.stop_engine()
