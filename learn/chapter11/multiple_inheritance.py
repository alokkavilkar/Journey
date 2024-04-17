
class Parent1:
    money = 20

    def sense_humor(self):
        return f"I'm happy and having nice sense of humor"

class Parent2:
    money = 40

    def sense_humor(self):
        return "I'm quite rude with people"

class Child(Parent1, Parent2):

    money = 0

me = Child()
print(me.sense_humor())

