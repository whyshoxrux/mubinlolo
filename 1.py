import os
os.system("cls")

class Computer:
    def __init__(self, model, price, year, colour, ram, memory):
        self.__model = model
        self.__price = price
        self.__year = year
        self.__colour = colour
        self.__ram = ram
        self.__memory = memory


    @property
    def model(self):
        return self.__model
    
    @model.setter
    def model(self):
        return self.__model
    
    @model.deleter
    def model(self):
        return self.__model
    

   
   
   
   
   
    @property
    def price(self):
        return self.__price
    
    @price.setter
    def price(self):
        return self.__price
    
    @price.deleter
    def price(self):
        return self.__price
    






    @property
    def year(self):
        return self.__year
    
    @year.setter
    def year(self):
        return self.__year
    
    @year.deleter
    def year(self):
        return self.__year
    





    @property
    def colour(self):
        return self.__colour

    @colour.setter
    def colour(self):
        return self.__colour
    
    @colour.deleter
    def colour(self):
        return self.__colour
    



    @property
    def ram(self):
        return self.__ram
    
    @ram.setter
    def ram(self):
        return self.__ram
    
    @ram.deleter
    def ram(self):
        return self.__ram
    

    @property
    def memory(self):
        return self.__memory
    
    @memory.setter
    def memory(self):
        return self.__memory
    
    @memory.deleter
    def memory(self):
        return self.__memory




laptop = Computer("Lenovo", "800$", 2023, "Black", "8GB", "256GB")

print(laptop.colour)
laptop.colour = "Red"
print(laptop.colour)
del laptop.colour













            

