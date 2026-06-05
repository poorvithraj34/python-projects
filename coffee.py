class coffee:
    def __init__(self, name, price):
        self.name = name
        self.price = price


class order:

    # initializing order with empty list
    def __init__(self):
        self.items = []

    # add coffee to order
    def add_item(self, coffee):
        self.items.append(coffee)
        print(f"added {coffee.name} to the order")

    # calculating total price
    def total(self):
        return sum(item.price for item in self.items)

    # show order summary
    def show_order(self):

        if not self.items:
            print("no items in order")
            return

        print("\nyour order:")

        for i, item in enumerate(self.items, 1):
            print(f"{i}. {item.name} - ${item.price}")

        print(f"total: ${self.total()}\n")

    # handle checkout process
    def checkout(self):

        if not self.items:
            print("your cart is empty")
            return

        self.show_order()

        confirm = input("proceed to checkout? (yes/no): ").strip().lower()

        if confirm == 'yes':

            print("order confirmed! Thank you.")

            self.items.clear()

        else:
            print("checkout cancelled")


def main():

    menu = [

        coffee("espresso", 2.5),

        coffee("latte", 3.5),

        coffee("cappuccino", 3.0),

        coffee("americano", 2.0)

    ]

    customer_order = order()

    while True:

        print("\n--- coffee menu ---")

        for i, coffee_item in enumerate(menu, 1):

            print(f"{i}. {coffee_item.name} - ${coffee_item.price}")

        print("5. view order")
        print("6. checkout")
        print("7. exit")

        choice = input("choose an option: ")

        if choice in ['1', '2', '3', '4']:

            customer_order.add_item(menu[int(choice) - 1])

        elif choice == '5':

            customer_order.show_order()

        elif choice == '6':

            customer_order.checkout()

        elif choice == '7':

            print("thanks for visiting. goodbye!")

            break

        else:

            print("invalid choice. try again")


if __name__ == "__main__":
    main()