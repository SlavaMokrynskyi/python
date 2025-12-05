class Money:
    def __init__(self,dollars,cents):
        self.dollars = dollars
        self.cents = cents

    def show_balance(self):
        print(f"{self.dollars}.{self.cents}$")

    def set_balance(self,dollars,cents):
        self.dollars = dollars
        self.cents = cents

    def __lt__(self,other):
        self_sum = float(self.cents) / 100 + float(self.dollars)
        other_sum = float(other.cents) / 100 + float(other.dollars)
        return self_sum < other_sum
    
    def __gt__(self,other):
        self_sum = float(self.cents) / 100 + float(self.dollars)
        other_sum = float(other.cents) / 100 + float(other.dollars)
        return self_sum > other_sum

class Product:
    def __init__(self,name, price : Money):
        self.name = name
        self.price = price

    def buy_product(self, balance: Money):
        if self.price > balance:
            raise ValueError("Not enough money")

        bal_total = balance.dollars * 100 + balance.cents
        price_total = self.price.dollars * 100 + self.price.cents
        
        result = bal_total - price_total
        
        # назад у долари і центи
        balance.set_balance(result // 100, result % 100)

        print(f"You successfully bought {self.name}!")
        balance.show_balance()


money = Money(130,99)
product = Product("Apple",Money(1,50))
product.buy_product(money)


