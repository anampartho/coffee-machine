'''
Coffee Machine
'''

# Coffee Machine Class
class CoffeeMachine:
    def __init__(self, water, milk, beans, cups, money):
        self.water = water
        self.milk = milk
        self.beans = beans
        self.cups = cups
        self.money = money
        self.state = False

    def __str__(self):
        return 'This machine has {water}ml water, {milk}ml milk, {beans}g beans, {cups} cups and ${money}'.format(water=self.water, milk=self.milk, beans=self.beans, cups=self.cups, money=self.money)

    def toggle_machine(self):
        self.state = not self.state
    
    def is_on(self):
        return self.state
    
    def resource_check(self, water = None, milk = None, beans = None, cups = None):
        if water and self.water < water:
            return 'Sorry, not enough water!'
        
        if milk and self.milk < milk:
            return 'Sorry, not enough milk!'

        if beans and self.beans < beans:
            return 'Sorry, not enough beans!'

        if cups and self.cups < cups:
            return 'Sorry, not enough cups!'

    def machine_state(self):
        string = '\nThe coffee machine has:'
        string += '\n{water} of water'.format(water=self.water)
        string += '\n{milk} of milk'.format(milk=self.milk)
        string += '\n{beans} of coffee beans'.format(beans=self.beans)
        string += '\n{cups} of disposable cups'.format(cups=self.cups)
        string += '\n${money} of money'.format(money=self.money)

        return string
    
    def buy(self, coffee):
        print()
        if coffee == 'espresso':
            less_resources = self.resource_check(250, None, 16, 1)
            if less_resources:
                print(less_resources)
                return

            self.water -= 250
            self.beans -= 16
            self.money += 4

        elif coffee == 'latte':
            less_resources = self.resource_check(350, 75, 20, 1)
            if less_resources:
                print(less_resources)
                return

            self.water -= 350
            self.milk -= 75
            self.beans -= 20
            self.money += 7
        elif coffee == 'cappuccino':
            less_resources = self.resource_check(200, 100, 12, 1)
            if less_resources:
                print(less_resources)
                return

            self.water -= 200
            self.milk -= 100
            self.beans -= 12
            self.money += 6

        print('I have enough resources, making you a coffee!')

        self.cups -= 1
    def fill(self):
        self.water += int(input('Write how many ml of water do you want to add: '))
        self.milk += int(input('Write how many ml of milk do you want to add: '))
        self.beans += int(input('Write how many grams of coffee beans do you want to add: '))
        self.cups += int(input('Write how many disposable cups of coffee do you want to add: '))
        
    def take(self):
        print()
        print(f'I gave you ${self.money}')
        self.money = 0

    def start(self):
        while True:
            # Get user action
            print()
            user_action = input('Write action (buy, fill, take, remaining, exit): ')
            if user_action == 'exit':
                break

            if user_action == 'remaining':
                print(self.machine_state())
                continue

            if user_action == 'back':
                continue
            
            if user_action == 'buy':
                print()
                coffee_type = input('What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino: ')

                if coffee_type == 'back':
                    continue
                else:
                    coffee_type = int(coffee_type)

                if coffee_type == 1:
                    self.buy('espresso')
                elif coffee_type == 2:
                    self.buy('latte')
                elif coffee_type == 3:
                    self.buy('cappuccino')

            elif user_action == 'fill':
                self.fill()

            elif user_action == 'take':
                self.take()

coffee_machine = CoffeeMachine(400, 540, 120, 9, 550)
coffee_machine.start()