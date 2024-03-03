import os
os.system("cls")

class Book:
    def __init__(self, name, read_time: int, spend_time: int):
        self._name = name 
        self.__read_time = read_time 
        self.__spend_time = spend_time 
    
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self):
        return self._name
    
    @name.deleter
    def name(self):
        return self._name



    @property
    def readtime(self):
        return int((self.__spend_time / self.__read_time) * 100)
    @readtime.setter
    def readtime(self):
        return self.__read_time

    @readtime.deleter
    def readtime(self):
        return self.__read_time


    @property
    def spendtime(self):
        return  self.__read_time // self.__spend_time

    @spendtime.setter
    def spendtime(self):
        return self.__spend_time

    @spendtime.deleter
    def spendtime(self):
        return self.__spend_time  
    

name = input("Lyuboy ismni kiriting kiriting: ")
read_time = int(input("Kitobni o'qish vaqti (daqiqa): "))
spend_time = int(input("Bitta varaqni o'qish vaqti (daqiqa): "))
month = int(input("Necha oyda qancha varaq o'qishni bilishi xolasez lyuboy sonni kiriting"))
year = int(input("Yilniyam kiritng endi: "))

book = Book(name, read_time, spend_time)
print(f"{book.name} kitobni 1 minutda {book.readtime} foizini o'qib tugatadi")
print(f"1 kunda {book.spendtime} varaq o'qib tugatadi")
print(f"1 oyda {book.spendtime * 30} varaq o'qib tugatadi")
print(f"{month} oyda {book.spendtime * (month * 30)} varaq o'qib tugatadi") 
print(f"{year} yilda {book.spendtime * (year * 365)} varaq o'qib tugatadi") 
