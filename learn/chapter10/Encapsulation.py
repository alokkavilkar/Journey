class Car:

    def __init__(self, make, model) -> None:
        self.__make = make
        self.__model = model

    def get_model(self):
        print(self.__model, self.__make)

    def set_model(self, make):
        self.__make = make

    
car1 = Car('Toyota', 'bahs')
# print(car1.__model)
car1.get_model()
car1.set_model('H10')
car1.get_model()