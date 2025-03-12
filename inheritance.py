#inheritance hakkında kolay bir örnek

class Animal():
    def __init__ (self,name:str,age:int):
        self.name=name
        self.age=age

    def say_name(self):
        print(f'Name:{self.name}')



class Dog(Animal):
    def __init__(self,name:str,age:int,type:str):
        super().__init__(name,age)
        self.type=type

    def make_noise(self):
        print('bork!')



dog1=Dog('Wolf',12,'vbvb')
dog1.make_noise()
dog1.say_name()

#Manager-employee
class Employee():
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary



    def calculate_bonus(self):
        bonus=self.salary*0.10
        return bonus

    def display_Info(self):
        print(f'Name:{self.name}\n'
              f'Salary:{self.salary}\n'
              f'Bonus:{self.calculate_bonus()}')



class Manager(Employee):
    def __init__ (self,name,salary,department):
     super().__init__(name,salary)
     self.department=department

     def calculate_bonus(self):
         bonus=self.salary*0.20
         return bonus

     def display_Info(self):
         print(f'Name:{self.name}\n'
               f'Salary:{self.salary}\n'
               f'Bonus:{self.calculate_bonus()}')



employee1=Employee('Ayşe',12000)
employee1.calculate_bonus()
employee1.display_Info()

manager1=Manager('Kader',40000,'data')
manager1.calculate_bonus()
manager1.display_Info()






