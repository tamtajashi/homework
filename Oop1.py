# Define the Car class with private attributes and methods
class Car:
    def __init__(self, brand, model, production_year, color, horse_power, is_sport_car=False):
        # Constructor to initialize attributes
        self._brand = brand
        self._model = model
        self._production_year = production_year
        self._color = color
        self._horse_power = horse_power
        self._is_sport_car = is_sport_car

    # Getter methods for all attributes
    def get_brand(self):
        return self._brand
    
    def get_model(self):
        return self._model
    
    def get_production_year(self):
        return self._production_year
    
    def get_color(self):
        return self._color
    
    def get_horse_power(self):
        return self._horse_power
    
    def is_sport_car(self):
        return self._is_sport_car

    # Method to display information about the car
    def display_info(self):
        print(f"Brand: {self._brand}")
        print(f"Model: {self._model}")
        print(f"Production Year: {self._production_year}")
        print(f"Color: {self._color}")
        print(f"Horse Power: {self._horse_power}")
        print(f"Is Sport Car: {self._is_sport_car}")

    # Method to change the color of the car
    def change_color(self, new_color):
        if new_color != self._color:
            self._color = new_color
            return True
        else:
            return False

    # Method to increase the horse power of the car
    def increase_horse_power(self, hp):
        if hp > 0:
            self._horse_power += hp
            return True
        else:
            return False

# Example usage:
# Create an instance of the Car class for an Audi A6 2012
my_audi = Car(brand="Audi", model="A6", production_year=2012, color="Silver", horse_power=250)

# Display the initial information
print("Initial Information:")
my_audi.display_info()

# Attempt to change the color to "Black" (successful)
if my_audi.change_color("Black"):
    print("Color changed successfully!")
else:
    print("Color remains the same.")

# Attempt to change the color to the current color "Silver" (unsuccessful)
if my_audi.change_color("Silver"):
    print("Color changed successfully!")
else:
    print("Color remains the same.")

# Attempt to increase horse power by 50 (successful)
if my_audi.increase_horse_power(50):
    print("Horse power increased successfully!")
else:
    print("Invalid horse power value. Horse power remains the same.")

# Attempt to increase horse power by 0 (unsuccessful)
if my_audi.increase_horse_power(0):
    print("Horse power increased successfully!")
else:
    print("Invalid horse power value. Horse power remains the same.")

# Display updated information
print("\nUpdated Information:")
my_audi.display_info()

