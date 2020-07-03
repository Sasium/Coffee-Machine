class CoffeeMachine:
    water = 400
    milk = 540
    coffee_beans = 120
    cups = 9
    money = 550

    def __init__(self, option):
        self.option = option

    def show(self):
        print("The coffee machine has:")
        print(self.water, " of water")
        print(self.milk, " of milk")
        print(self.coffee_beans, " of coffee beans")
        print(self.cups, " of disposable cups")
        print(self.money, " of money")

    def buy(self, sub_option):
        if sub_option == "1":
            if self.water < 250:
                print("Sorry, not enough water!")
            elif self.coffee_beans < 16:
                print("Sorry, not enough coffee beans!")
            elif self.cups < 1:
                print("Sorry, not enough disposable cups!")
            else:
                CoffeeMachine.water -= 250
                CoffeeMachine.coffee_beans -= 16
                CoffeeMachine.cups -= 1
                CoffeeMachine.money += 4
                print("I have enough resources, making you a coffee!")
        if sub_option == "2":
            if self.water < 350:
                print("Sorry, not enough water!")
            elif self.milk < 75:
                print("Sorry, not enough milk!")
            elif self.coffee_beans < 20:
                print("Sorry, not enough coffee beans!")
            elif self.cups < 1:
                print("Sorry, not enough disposable cups!")
            else:
                CoffeeMachine.water -= 350
                CoffeeMachine.milk -= 75
                CoffeeMachine.coffee_beans -= 20
                CoffeeMachine.cups -= 1
                CoffeeMachine.money += 7
                print("I have enough resources, making you a coffee!")
        if sub_option == "3":
            if self.water < 200:
                print("Sorry, not enough water!")
            elif self.milk < 100:
                print("Sorry, not enough milk!")
            elif self.coffee_beans < 12:
                print("Sorry, not enough coffee beans!")
            elif self.cups < 1:
                print("Sorry, not enough disposable cups!")
            else:
                CoffeeMachine.water -= 200
                CoffeeMachine.milk -= 100
                CoffeeMachine.coffee_beans -= 12
                CoffeeMachine.cups -= 1
                CoffeeMachine.money += 6
                print("I have enough resources, making you a coffee!")

    def fill(self, fill_water, fill_milk, fill_coffee_beans, fill_cups):
        CoffeeMachine.water += fill_water
        CoffeeMachine.milk += fill_milk
        CoffeeMachine.coffee_beans += fill_coffee_beans
        CoffeeMachine.cups += fill_cups

    def take(self):
        print("I gave you $", self.money)
        CoffeeMachine.money = 0

while True:
    coffee_monster = CoffeeMachine(input("Write action (buy, fill, take,remaining,exit):"))
    if coffee_monster.option == "exit":
        break
    if coffee_monster.option == "remaining":
        coffee_monster.show()
    if coffee_monster.option == "buy":
        coffee_monster.buy(input("What do you want to buy? "
                                 "1 - espresso, 2 - latte, 3 - cappuccino, "
                                 "back - to main menu:"))
    if coffee_monster.option == "fill":
        coffee_monster.fill(int(input("Write how many ml of water do you want to add:")),
                            int(input("Write how many ml of milk do you want to add:")),
                            int(input("Write how many grams of "
                                      "coffee beans do you want to add:")),
                            int(input("Write how many disposable cups of coffee "
                                      "do you want to add:")))
    if coffee_monster.option == "take":
        coffee_monster.take()

