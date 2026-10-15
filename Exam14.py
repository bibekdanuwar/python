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
        elif amount > self.money:
            print("Insufficient balance. Could not withdraw.")
            return 0
        else:
            self.money = self.money - amount
            return amount


bank = Bank()

bank.set_pin(50000)
bank.set_pin(10000)

bank.set_pin(-5000)
bank.set_pin(-1)

bank.set_pin(5000)
bank.set_pin(0)
bank.set_pin(9999)

bank.deposit(1234, 1000)
bank.deposit(9999, 1000)

bank.check_balance(1234)
bank.check_balance(9999)

received1 = bank.withdraw(9999, 1001)
print(received1)

received2 = bank.withdraw(9999, 1000)
print(received2)