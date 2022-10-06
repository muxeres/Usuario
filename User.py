class User:
    def __init__(self,firstname,lastname):
        self.firstname = firstname
        self.lastname = lastname
        self.account_balance =  0 

    def depositar(self,amount):
        self.account_balance += amount
    def girar(self, amount):
        self.account_balance -= amount
    def balance_usuario(self):
        print(f'User: {self.firstname} {self.lastname}, Balance: ${self.account_balance}')
    def transferir_dinero(self, other_user, amount):
        self.account_balance -= amount
        other_user.account_balance += amount
        self.balance_usuario()
        other_user.balance_usuario()