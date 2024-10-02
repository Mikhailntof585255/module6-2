class Vehicle:
    COLOR_VARIANTS = ['blue', 'red', 'green', 'black', 'white']

    def __init__(self,__model, __engine_power,__color,owner):
        self.__color=__color
        self.owner=owner
        self.__model=__model
        self.__engine_power= __engine_power
        self.set_color(__color)
    def get_model(self,__model:str):
       #self.__model=__model
        return print(f'Модель: {__model}')

    def get_horsepower(self,__engine_power:int):
        #self.__engine_power=__engine_power
        return print(f"Мощность двигателя: {__engine_power}")

    def get_color(self,__color:str):
        #self.__color=__color
        self.set_color(__color)

        return print(f'Цвет: {__color}')

    def set_color(self,__color:str):
        __color=__color.lower()
        if __color not in self.COLOR_VARIANTS:
            new_color = __color
            print(f'Нельзя сменить цвет на {new_color}')

        def get_owner(self,owner:str):
        return print(f'Владелец: {self.owner}')

    def print_info (self,__model:str,__engine_power:int,__color:str,owner:str):
         print(f"{self.get_model(__model)}, {self.get_horsepower(__engine_power)}, {self.get_color(__color)}, {self.get_owner(owner)}")


class Sedan(Vehicle):
    __PASSENGERS_LIMIT = 5

    pass

vehicle1 = Sedan("Toyta Mark II",500,"blue","Fedos" )
vehicle1.print_info("Toyta Mark II",500,"blue","Fedos" )
vehicle1.set_color("Pink")
vehicle1.set_color('BLACK')
vehicle1.owner = 'Vasyok'
print(vehicle1.owner)
vehicle1.print_info('Toyta Mark II',500,'BLAK','Vasyok')

