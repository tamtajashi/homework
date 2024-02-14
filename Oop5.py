from abc import ABC, abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def start_engine(self):
        pass

    @abstractmethod
    def stop_engine(self):
        pass

class Car(Vehicle):
    def __init__(self, max_speed):
        self.max_speed = max_speed
        self.current_speed = 0

    def start_engine(self):
        return "car started"

    def stop_engine(self):
        self.current_speed = 0
        return "car stopped"

class SportCar(Car):
    def start_engine(self):
        parent_return = super().start_engine()
        return f"{parent_return}. Max speed: {self.max_speed}"

    def stop_engine(self):
        parent_return = super().stop_engine()
        return f"{parent_return} - speed: {self.current_speed}"

# Example usage:
if __name__ == "__main__":
    car = SportCar(200)
    print(car.start_engine())  
    car.current_speed = 100
    print(car.stop_engine())   
