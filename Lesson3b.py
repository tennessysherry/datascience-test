class Account:
    def _init_self_(self,account_type):
        self.account_type = account_type

    def check_balance(self,balance):
         return f"your balance is {balance} {self.account_type}"

    def withdraw(self):
        return "This is withdraw function"


account_instance = Account()
account_instance.account_type='savings'
# print(account_instance.account_type) # this prints the type of account
print(account_instance.check_balance(3000)) # this prints the balance and the type of account

current_account = Account()
current_account.account_type='current'
# print(current_account.account_type)
print(account_instance.check_balance(4000)) # or print ( current_account.check_balance(4000))
