class Budget:
    def __init__(self, category):
        self.name = category
        self.balance = 0
        expenditure = 0

    def get_option(self):
        print('1. Deposit')
        print('2. Withdraw')
        print('3. Check Balance')
        selected_option = int(input(' ***Select Your Preferred Option ***\n'))

        while True:
            if selected_option == 1:
                self.deposit()
                break

            elif selected_option == 2:
                self.withdraw()
                break

            elif selected_option == 3:
                self.get_balance()
                break

            else:
                print('Invalid Option, try again')
                selected_option = int(input('Select Option \n'))
                continue

    def get_balance(self):
        print('{} Have N-{}'.format(self.name, self.balance))
        return self.balance

    def deposit(self):
        amount = int(input('{} Amount :\n'.format(self.name)))
        self.balance += amount
        print('N-{} added to {}'.format(amount, self.name))

    def withdraw(self):
        amount = int(input('{} Amount :\n'.format(self.name)))
        if self.balance >= amount:

            if amount >= 100:
                self.balance -= amount
                self.expenditure += amount
            else:
                print('You Cannot Take Less Than N-100')
        else:
            print('You Do Not Have Enough Funds For This Transaction')
            


food = Budget('Food')
clothing = Budget('Clothing')
entertainment = Budget('Entertainment')


print('**** Welcome To The iBudget App ****')
print('Category List')
print('''
1. *** Food ***
2. *** Clothing ***
3. *** Entertainment ***
''')

category = int(input('Please, Select a Category :\n'))
while True:
    if category == 1:
        print(f'\n({food.name})')
        food.get_option()
        break

    elif category == 2:
        print(f'\n({clothing.name})')
        clothing.get_option()
        break

    elif category == 3:
        print(f'\n({entertainment.name})')
        entertainment.get_option()
        break

    else:
        print('Invalid Option, Try Again')
        category = int(input('Please, Select a Category :'))



