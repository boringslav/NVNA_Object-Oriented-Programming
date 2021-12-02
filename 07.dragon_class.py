class Dragon:
 
    __dragons_count__ = []
    
    @staticmethod
    def count():
        return len(Dragon.__dragons_count__)
    
    def __init__(self, **kwargs):
        self.__name__ = kwargs["name"] if "name" in kwargs else "No name"
        self.__wingspan__ = kwargs["wingspan"] if "wingspan" in kwargs else 1
        self.energy = 100 
        Dragon.__dragons_count__.append(self)
        
        for key in kwargs:
            if key not in ("name", "wingspan", "energy"):
                setattr(self, key, kwargs[key])
      
        if(not hasattr(self, "color")):
            setattr(self, "color", input("Vavedete cvqt za drakona"))
                
    def checkDuration(self, minutes):
        return self.energy - (minutes * 3) > 0
    
    def fly(self, minutes):
        if self.checkDuration(minutes):
            self.energy -= minutes * 3
    
    def eat(self, amount):
        self.energy += amount * 0.8
        
    def grow(self):
        self.__wingspan__ += 1
        
    def __str__(self):
        result = ""
        for attr, val in self.__dict__.items():
            result += attr + "=" + str(val) + "\n"
        return result

    def filter_attributes(self):
        return len(({key:value for(key,value) in self.__dict__.items() if type(value) in (int,float) and value >= 100 }).keys())  
            

d1 = Dragon(name="Cows Eat Noobs", color="4eren", age=100, money=9999, hoes=9999)
print(d1.filter_attributes());
