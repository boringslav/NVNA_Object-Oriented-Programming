class Dish:
    def __init__(self, material: str) -> None:
            self.material = material
      
    def __str__(self) -> str:
        return f"Dish:\n Material: {self.material}"

    def setMaterial(self, material:str) -> None :
            self.material = material
      
    
class Plate(Dish):
    def __init__(self,material:str, diameter:int) -> None:
        super().__init__(material)
        self.diameter = diameter

    def __str__ (self)-> str:
        return f"Plate:\n Material: {self.material} Diameter: {self.diameter}"
    
    def __eq__(self, other: object) -> bool:
        return self.material == other.material and self.diameter == other.diameter

    def get_diameter(self) -> int:
        return self.diameter


class Cup(Dish):
    def __init__(self, material:str, volume:int, has_handle: bool) -> None :
        super().__init__(material)
        self.volume = volume
        self.has_handle = has_handle

    def __str__(self) -> None :
        return f"Cup\n Material: {self.material} Volume: {self.material} Handle: {self.has_handle}"

    def __eq__(self, other: object) -> bool:
        return self.has_handle == other.has_handle and self.material == other.material and self.volume == other.volume

    def __gt__(self, other: object) -> bool:
        return self.volume > other.volume

    def get_volume(self) -> int:
        return self.volume


plate1=Plate("Wood",45) #create an instance of plate
plate2=Plate("Plastic", 45)

print("Plate1 is made from {}".format(plate1.material))
print("Plate2 has a diameter of {} cm".format(plate2.get_diameter()))
print("plate1 is the same as plate2: {}".format(plate1==plate2))


cup1 = Cup("Plastic", 500, True) #create an instance of cup
cup2 = Cup("Plastic", 550, True)

print("cup1 has volume of {} ml".format(cup1.get_volume()))
print("cup1 is the same as cup2: {}".format(cup1==cup2))
print("cup2 is bigger than cup1: {}".format(cup2>cup1))
