'''
>>> Program: Generates a program that keeps track of bank account balances and
allows the user to deposit, withdraw, and display the account balance.
>>> Author: JAAR
>>> Date: 10/10/2023
>>> Version 1.1
>>> Update: Allowed the user to verify initial account information inputted.
>>> Allows the user to update any info that was initially inputted incorrectly.

>>> TODO: Implement functionality of withdraw and deposit
>>> TODO: Create a history of transactions
>>> TODO: Should I use a JSON for the transactions?

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
        print(f'Account Holders Name: {self.f_name} {self.l_name}')
        print(f'\tAccount Balance: ${self.account_amount:.2f}')

def verify()->str :
    while True :
        response = input().lower()
        if response == "y" or response == "n" :
            return response
        else :
            print("Your input was invalid! Enter a new response: ", end = '')

def user_input()->dict :
    a_info = ["f_name", "l_name", "i_deposit"]
    categories = ["First Name", "Last Name", "Initial Deposit"]

    account = {"f_name" : input(f"\t{categories[0]}: "),
            "l_name" : input(f"\t{categories[1]}: "),
            "i_deposit" : None}

    while not isinstance(account["i_deposit"], float) or account["i_deposit"] <= 0 :
        try :
            account["i_deposit"] = float(input(f"{categories[2]}: "))
            if account["i_deposit"] <= 0 :
                raise ValueError
        except ValueError :
            print("Your input was invalid!\n\t")

    print(f'''
    Please verify the account information you entered is correct:
        First Name: {account["f_name"]}
        Last Name: {account["l_name"]}
        Initial Deposit: ${account["i_deposit"]:.2f}
    (Y/N): ''', end = '')
    response = verify()

    while response != "y" :
        update = ''
        while not isinstance(update, int) or update not in range(len(a_info)) :
            try :
                update = int(input(f'''
    Enter the number corresponding to the field you want to update:
        1. First Name: {account["f_name"]}
        2. Last Name: {account["l_name"]}
        3. Initial Deposit: ${account["i_deposit"]:.2f}
    Field: ''')) - 1
                if update not in range(len(a_info)) :
                    raise ValueError
            except ValueError :
                print("Your input was invalid!")

        if a_info[update] != "i_deposit" :
                account[a_info[update]] = input(f'''
            {categories[update]}: ''')
        else :
            while True :
                try :
                    account["i_deposit"] = float(input(f"{categories[2]}: "))
                    if account["i_deposit"] <= 0 :
                        raise ValueError
                except ValueError :
                    print("Your input was invalid!\n\t")
                else :
                    break

        print(f'''
    Is the information correct:
        First Name: {account["f_name"]}
        Last Name: {account["l_name"]}
        Initial Deposit: ${account["i_deposit"]:.2f}
    (Y/N): ''', end = '')
        response = verify()
    return account

def main() :

    print("Enter the full name and initial deposit for an account and I'll"
        " open a new account for the client.")
    account = user_input()
    user = Bank_Account(account["f_name"], account["l_name"], account["i_deposit"])
    user.display()


if __name__ == '__main__' :
    main()