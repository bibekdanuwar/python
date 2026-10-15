class Bank:
    def __init__(self):
        self.pin = 0
        self.money = 0

    def set_pin(self, pin):
        if pin >= 10000 or pin < 0:
            print("Invalid value")
        else:
            self.pin = pin
            print("PIN set")

    def deposit(self, pin, amount):
        if pin != self.pin:
            print("Incorrect PIN")
        else:
            print("Deposited " + str(amount) + " yen")
            self.money = self.money + amount

    def check_balance(self, pin):
        if pin != self.pin:
            print("Incorrect PIN")
        else:
            print("Balance is " + str(self.money) + " yen")

    def withdraw(self, pin, amount):
        if pin != self.pin:
            print("Incorrect PIN")
            return 0
        if amount > self.money:
            print("Insufficient balance. Could not withdraw.")
            return 0
        else:
            self.money = self.money - amount
            return amount


def read_number(message):
    while True:
        text = input(message)
        try:
            return int(text)
        except ValueError:
            print("Please enter a whole number")


bank = Bank()

while True:
    print()
    print("1: Set PIN")
    print("2: Deposit")
    print("3: Check balance")
    print("4: Withdraw")
    print("0: Quit")
    choice = input("Choose a number: ")

    if choice == "1":
        pin = read_number("New PIN: ")
        bank.set_pin(pin)
    elif choice == "2":
        pin = read_number("PIN: ")
        amount = read_number("Amount to deposit: ")
        bank.deposit(pin, amount)
    elif choice == "3":
        pin = read_number("PIN: ")
        bank.check_balance(pin)
    elif choice == "4":
        pin = read_number("PIN: ")
        amount = read_number("Amount to withdraw: ")
        received = bank.withdraw(pin, amount)
        print(received)
    elif choice == "0":
        print("Goodbye")
        break
    else:
        print("Please choose 0 to 4")