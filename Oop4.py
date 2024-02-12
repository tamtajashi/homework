class Heart:
    def __init__(self, owner):
        self.owner = owner

    @property
    def state(self):
        if self.owner.cardiac_output > 70:
            return "high blood pressure"
        else:
            return "feeling good"


class Brain:
    def __init__(self, owner):
        self.owner = owner

    @property
    def state(self):
        if self.owner.brain_load > 90:
            return "tired"
        else:
            return "rested"


class Person:
    def __init__(self, cardiac_output, brain_load):
        self.heart = Heart(self)
        self.brain = Brain(self)
        self.cardiac_output = cardiac_output
        self.brain_load = brain_load


class Leg:
    def __init__(self, person):
        self.person = person

    @property
    def movement(self):
        if self.person.moving_speed > 10:
            return "running"
        else:
            return "walking" if self.person.frofferty == "walking" else "standing"


# Example usage:
if __name__ == "__main__":
    person = Person(cardiac_output=75, brain_load=85)
    person.moving_speed = 15
    person.frofferty = "walking"

    leg = Leg(person)
    print("Heart state:", person.heart.state)
    print("Brain state:", person.brain.state)
    print("Leg movement:", leg.movement)
