class Vehicle:
    COLOR_VARIANTS = ['blue', 'red', 'green', 'black', 'white']

    def __init__(self,model:str, engine_power:int,color:str,owner:str):
        self.__color=color
        self.owner=owner
        self.__model=model
        self.__engine_power= engine_power
        self.set_color(color)

    def get_model(self,model):
        return f'Модель: {model}'

    def get_horsepower(self,engine_power):
        return f"Мощность двигателя: {engine_power}"

      def get_color(self,new_color):
        return (f'Цвет: {new_color}')

    def set_color(self,color):
        new_color=color.lower()
        if new_color in self.COLOR_VARIANTS:
            self.color = new_color
        else:
            print(f' Нельзя сменить цвет на {color}')

    def print_info (self,__model,__engine_power,__color,owner):
        print(f" {self.get_model(__model)}\n {self.get_horsepower(__engine_power)}\n {self.get_color(__color)}\n Владелец: {owner}")

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

