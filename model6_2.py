class  Vehicle:
    COLOR_VARIANTS = ['blue', 'red', 'green', 'black', 'white']
    def __init__(self,model:str,engine_power:int,color:str,owner:str):
        self.__color=color
        self.__model=model
        self.__engine_power = engine_power
        self.owner = owner

    def get_model(self):
        return f'Модель: {self.__model}'
    def get_horsepower(self):
        return f"Мощность двигателя: {self.__engine_power}"
    def get_color(self):
        return f'Цвет: {self.__color}'
    def set_color(self,__color):
        new_color = __color
        if new_color.lower() in self.COLOR_VARIANTS:
            self.__color = new_color
            print()
        else:
            print(f'Нельзя сменить цвет на {new_color}')
    def print_info(self):
        return print(f'{self.get_model()}\n{self.get_horsepower()}\n{self.get_color()}\nВладелец: {self.owner}')


class Sedan(Vehicle):
    __PASSENGERS_LIMIT = 5


vehicle1 = Sedan("Toyta Mark II",500,"blue","Fedos" )
vehicle1.print_info()
vehicle1.set_color('Pink')
vehicle1.set_color('BLACK')
vehicle1.owner='Vasyok'
vehicle1.print_info()
         
