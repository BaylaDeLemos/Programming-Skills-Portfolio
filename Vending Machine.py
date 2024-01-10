"""
Vending Machine 
"""
import random

class VendingMachine:
    def __init__(self):
        # Define items with codes, categories, prices, and initial stock
        self.items = {
            '01': {'name': 'Coca Cola', 'category': 'Drinks', 'price': 1.50, 'stock': 10},
            '02': {'name': 'Water', 'category': 'Drinks', 'price': 1.00, 'stock': 10},
            '03': {'name': 'Starbucks Iced Coffee', 'category': 'Hot Drinks', 'price': 2.00, 'stock': 10},
            '04': {'name': 'Pringles', 'category': 'Snacks', 'price': 2.50, 'stock': 10},
            '05': {'name': 'Hershey Chocolate', 'category': 'Snacks', 'price': 1.50, 'stock': 10},
            '06': {'name': 'Lotus Biscuit', 'category': 'Snacks', 'price': 2.00, 'stock': 10},
            '07': {'name': 'Pocky', 'category': 'Snacks', 'price': 4.00, 'stock': 10},
            '08': {'name': 'Pretzels', 'category': 'Snacks', 'price': 3.00, 'stock': 10},
            '09': {'name': 'Kit-Kat', 'category': 'Snacks', 'price': 4.00, 'stock': 10},
            '10': {'name': 'Takis', 'category': 'Snacks', 'price': 4.00, 'stock': 10},
        }

        self.money_inserted = 0  # Amount of money inserted by the user

    def display_menu(self):
        print("\n===== WELCOME TO DAILY BAY'S VENDING MACHINE =====")
        for code, item in self.items.items():
            print(f"{code} - {item['name']} ({item['category']}): ${item['price']:.2f} | Stock: {item['stock']}")

    def insert_money(self):
        try:
            self.money_inserted = float(input("\nInsert money: $"))
        except ValueError:
            print("Invalid input. Please enter a valid amount.")
            self.insert_money()

    def select_item(self):
        code = input("\nEnter the code of the item you want to purchase: ").upper()
        if code in self.items:
            return code
        else:
            print("Invalid code. Please try again.")
            return self.select_item() 

    def dispense_item(self, code):
        item = self.items[code]
        if item['stock'] > 0 and self.money_inserted >= item['price']:
            print(f"\nDispensing {item['name']} ({item['category']})...")
            self.money_inserted -= item['price']
            item['stock'] -= 1
            return item
        elif item['stock'] == 0:
            print(f"\nSorry, {item['name']} is out of stock.")
            return None
        else:
            print("\nInsufficient funds. Please insert more money.")
            return None

    def return_change(self):
        print(f"\nChange returned: ${self.money_inserted:.2f}")
        return self.money_inserted

    def suggest_purchase(self, category):
        suggestions = [item['name'] for code, item in self.items.items() if item['category'] == category and item['stock'] > 0]
        if suggestions:
            print(f"\nMaybe consider buying {random.choice(suggestions)} as an extra?")

    def generate_receipt(self, item, change):
        print("\n====================== RECEIPT =======================")
        print(f"Item Purchased: {item['name']} ({item['category']})")
        print(f"Total Amount Paid: ${item['price']:.2f}")
        print(f"Change Returned: ${change:.2f}")
        print("=======================================================")

    def buy_additional_items(self):
        response = input("\nDo you want to buy additional items? (yes/no): ").lower()
        return response == 'yes'

    def run_vending_machine(self):
        while True:
            self.display_menu()
            self.insert_money()
            selected_code = self.select_item()
            purchased_item = self.dispense_item(selected_code)
            
            if purchased_item:
                change = self.return_change()
                self.generate_receipt(purchased_item, change)
                category = purchased_item['category']
                self.suggest_purchase(category)

            if not self.buy_additional_items():
                print("\nThank you for purchasing from Daily Bay!")
                break

if __name__ == "__main__":
    vending_machine = VendingMachine()
    vending_machine.run_vending_machine()
    
    
