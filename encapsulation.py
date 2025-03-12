class Bank_account():
    def __init__(self,balance,account_holder,account_number):
        self.__balance=balance
        self.account_holder=account_holder
        self.account_number=account_number


    def set_values(self,__balance):
        self.__balance=__balance

    def deposit(self,amount):
        self.amount=amount
        if amount>0:
         self.__balance += self.amount
         print(f'Güncel bakiye:{self.__balance}\n')
        else:
            print('hata')

    def witdraw(self,amount):
        self.amount=amount
        if self.__balance<=0:
            print('Yeterli bakiyeniz bulunmamakta')
        elif amount<self.__balance:
            print('İşleminiz gerçekleştiriliyor.')
            self.__balance -= amount
            print(f'Güncel bakiye:{self.__balance}')
        else:
            print('Hata')
    def get_balance(self):
        print(f'Güncel bakiye:{self.__balance}')


account1=Bank_account(1200,'kader',321)
account1.deposit(200)
account1.witdraw(100)
account1.get_balance()

#ornek2
class Student():
    def __init__(self,name,student_id):
        self.name=name
        self.student_id=student_id

    def save_to_file(self):
        with open(file='student_save.txt',mode='a',encoding='utf-8')as file:
            file.write(f'Adı: {self.name}, Öğrenci No: {self.student_id}\n')
            print(f'{self.name} verisi dosyaya kaydedildi.')


    def add_student(self,name,student_id):
        with open(file='student_add',mode='a',encoding='utf-8') as file:
            file.write(f'{student_id,name}\n')
        print('Öğrenci başarıyla eklendi.')


s1=Student('Kader',321)
s1.add_student('Kader',321)
s1.save_to_file()







