water = 400
milk = 540
beans = 120
cups = 9
money = 550


def amount():
    global water, milk, beans, cups, money
    print("The coffee machine has:")
    print(str(water) + " of water")
    print(str(milk) + " of milk")
    print(str(beans) + " of coffee beans")
    print(str(cups) + " of disposable cups")
    if money == 0:
        print(str(money) + " of money")
    else:
        print("$" + str(money) + " of money")


def buy():
    global water, milk, beans, cups, money
    order = input("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:")
    if order == "1":
        if water < 250:
            print("Sorry, not enough water!")
        if beans < 16:
            print("Sorry, not enough coffee beans!")
        if cups < 1:
            print("Sorry, not enough cups!")
        else:
            water = water - 250
            beans = beans - 16
            cups = cups - 1
            money = money + 4
            print("I have enough resources, making you coffee!")
    elif order == "2":
        if water < 350:
            print("Sorry, not enough water!")
        elif beans < 20:
            print("Sorry, not enough coffee beans!")
        elif cups < 1:
            print("Sorry, not enough cups!")
        elif milk < 75:
            print("Sorry, not enough milk!")
        else:
            water = water - 350
            milk = milk - 75
            beans = beans - 20
            cups = cups - 1
            money = money + 7
            print("I have enough resources, making you coffee!")
    elif order == "3":
        if water < 200:
            print("Sorry, not enough water!")
        elif beans < 12:
            print("Sorry, not enough coffee beans!")
        elif cups < 1:
            print("Sorry, not enough cups!")
        elif milk < 100:
            print("Sorry, not enough milk!")
        else:
            water = water - 200
            milk = milk - 100
            beans = beans - 12
            cups = cups - 1
            money = money + 6
            print("I have enough resources, making you coffee!")
    elif order == "back":
        pass


def take():
    global money
    print("I gave you $" + str(money))
    money = money * 0


def fill():
    global water, milk, beans, cups
    water_add = int(input("Write how many ml of water do you want to add: "))
    water = water + water_add
    milk_add = int(input("Write how many ml of milk do you want to add: "))
    milk = milk + milk_add
    beans_add = int(input("Write how many grams of coffee beans do you want to add: "))
    beans = beans + beans_add
    cups_add = int(input("Write how many disposable cups do you want to add: "))
    cups = cups + cups_add


while True:
    action = input("Write action (buy, fill, take, remaining, exit):")
    if action == "buy":
        buy()
    elif action == "fill":
        fill()
    elif action == "take":
        take()
    elif action == "remaining":
        amount()
    elif action == "exit":
        break
