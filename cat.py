class Cat:

    def __init__(self, name: str, age: float, money: float):
        self.Name = name
        self.Age = age
        self.Money = money

        def String(self):
            print(f"Name:\t{self.Name}\n"
                  f"Age:\t{self.Age}\n"
                  f"Money:\t{self.Money}$")

    def Buy(self, price: float):
        if (self.Money >= price):
            self.Money -= price
        else:
            print(f"Not enough money!\n"
                  f"Your buget:\t{self.Money}")



