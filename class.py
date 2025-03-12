#class mantığını anlatan basit bir örnek
class Student():
    def __init__(self,name:str,surname:str,age:int):
        self.name=name
        self.surname=surname
        self.age=age
    def show_Info(self):
        print(f'Name:{self.name}\n'
              f'Surname:{self.surname}\n'
              f'Age:{self.age}')

student1=Student('Kader','Güneş',21)
student1.show_Info()

#Basit bir banka hesabı
class Account():
    def __init__(self,name:str,bakiye:float):
        self.name=name
        self.bakiye=bakiye

    def para_yatir(self,amount):
         self.amount=amount

         if amount>0:
             print('İşleminiz yapılıyor...')
             self.bakiye+=amount
             print(f'Güncel Bakiye:{self.bakiye}')
         else:
             print('Hatalı işlem yaptınız.')

    def para_cek(self,amount):
        self.amount=amount
        if amount>self.bakiye:
            print('Yeterli bakiye bulunmamakta.')
        elif amount<self.bakiye and amount>0:
            print('İşleminiz yapılıyor...')
            self.bakiye=self.bakiye-amount
            print(f'Güncel bakiye:{self.bakiye}')
        else:
            print('Hatalı giriş yaptınız.')

    def show_Info(self):
        print(f'Ad:{self.name}\n'
              f'Bakiye{self.bakiye}')

account1=Account('Kader',3200)
account1.para_cek(100)
account1.para_yatir(100)
account1.show_Info()


