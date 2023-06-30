import csv


class Item:
    pay_percent = 0.8
    all = []

    def __init__(self, name: str, price: int, quantity=0):
        assert price >= 0, f"Price {price} is less than zero"
        assert quantity > 0, f"quantity {quantity} cannot be zero"

        self.name = name
        self.price = price
        self.quantity = quantity

        Item.all.append(self)

    def total_price(self):
        return self.price * self.quantity

    def apply_discount(self):
        self.price = (
            # self.price * Item.pay_percent
            self.price
            * self.pay_percent
        )  # apply_discount can be reached either by class or instance

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.name}',{self.price},{self.quantity})"

    @staticmethod
    def check_integer(num):
        if isinstance(num, float):
            return num.is_integer()
        elif isinstance(num, int):
            return True
        else:
            return False

    @classmethod
    def open_csv(cls):
        with open("file.csv", "r") as f:
            reader = csv.DictReader(f)
            items = list(reader)
        for item in items:
            Item(
                name=item.get("firstname"),
                price=float(item.get("price")),
                quantity=int(item.get("quantity")),
            )


item1 = Item("Laptop", 2000, 1)
item2 = Item("Mouse", 200, 2)
print(item1.name, item1.price, item1.pay_percent, item2.total_price())
print(Item.__dict__)  # gives all the attributes present at class level
print(item1.__dict__)  # gives all the attributes present aat instance level

item1.apply_discount()
print(item1.price)

# if we want variable discount
item2.pay_percent = 0.6
item2.apply_discount()
print(
    item2.price
)  # we see still percent is happening cause in the method we used we set Item.pay_percent rather self
item1 = Item("Phone", 100, 1)
item2 = Item("Laptop", 1000, 3)
item3 = Item("Cable", 10, 5)
item4 = Item("Mouse", 50, 5)
item5 = Item("Keyboard", 75, 5)

# print(Item.all)
# for i in Item.all:
#     print(i.name)

# Item.open_csv()
# print(Item.all)
# print(Item.check_integer(item3.price))
# print(Item.all)


class Phone(Item):
    def __init__(self, name: str, price: float, quantity=0, broken_phones=0):
        # Call to super function to have access to all attributes / methods
        super().__init__(name, price, quantity)

        # Run validations to the received arguments
        assert (
            broken_phones >= 0
        ), f"Broken Phones {broken_phones} is not greater or equal to zero!"

        # Assign to self object
        self.broken_phones = broken_phones


phone1 = Phone("jscPhonev10", 500, 5, 1)


print(Phone.all)
