class Dragon:
    def __init__(self, name:str, wing_span:float):
        self.__name = name
        self.__wing_span = wing_span
        self.energy = 100
        self.can_fly = True
        self.instances.append(self)
    instances = []

    def fly(self, minutes: float) -> None:
        energy_lost = minutes * 3

        if energy_lost > self.energy:
            raise Exception('Not enough energy!')
        self.energy -= energy_lost

    def eat(self, food:float) -> None:
        self.energy += food * 0.8

    def grow(self) -> None:
        self.__wing_span +=1

    def get_number_of_dragons(self) -> int:
        return len(self.instances)

    def __str__(self) -> str:
        return '\nDragon:\n \tName: {}\n\tEnergy: {}\n\tWingspan: {}\n'.format(self.__name, self.energy, self.__wing_span)


d1 = Dragon('Chochko', 2)
d2 = Dragon('Vihur', 3)

print(str(d1))
d1.grow()
d1.fly(1)
print(str(d1))
d1.eat(4)
print(str(d1))
print('Number of dragons is: {}'.format(d1.get_number_of_dragons()))