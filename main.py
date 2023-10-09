'''
>>> Program: Generates a program that keeps track of bank account balances and
allows the user to deposit, withdraw, and display the account balance.
>>> Author: JAAR
>>> Date: 10/09/2023
>>> Version 1

>>> TODO: Verify the user input is a positive int or float, implement withdraw
>>> and deposit functionality. Allow the user to verify input before proceeding.
'''

class Bank_Account() :
    '''
    >>> Generates an instance of a bank account.

    >>> Param: First and Last Name, Phone Number, Address, initial deposit.
    >>> Assume all users will input a single valid phone number and address.
    '''
    def __init__(self, f_name: str, l_name: str, account_amount: (int, float)) -> None:
        self.f_name = f_name
        self.l_name = l_name
        self.account_amount = account_amount

    def deposit(self, deposit_amount : (int, float)) :
        '''
        >>> Updates the current account_amount based on the deposit amount.

        >>> Param: deposit_amount
        '''
        self.account_amount += deposit_amount

    def withdraw(self, withdraw_amount: (int, float)) :
        self.account_amount -= withdraw_amount

    def display(self) :
        print(f'${self.account_amount}')

def main() :

    print("Enter the full name and initial deposit for an account and I'll"
        " open a new account for the client.")

    f_name = input("\tFirst Name: ")
    l_name = input("\tLast Name: ")
    # Assume the user enters a positive numerical value.
    initial_deposit = float(input("\tInitial Deposit: "))

    user = Bank_Account(f_name, l_name, initial_deposit)
    user.display()

    # should I use a dictionary for this or???
    

if __name__ == '__main__' :
    main()