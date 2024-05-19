menu = [200, 220, 170, 100, 130, 250, 90, 120, 50, 30, 130, 130, 100, 135, 110, 120, 120, 135, 100, 150]
total = []
user_name = input("Hello! Welcome to our coffee shop. May I have your name, please? ").strip().replace(" ", "_")
receipt_file = f"{user_name.upper()}_RECEIPT.txt"
report = open(receipt_file, 'a')
report.write('NO.\t\t unit price \t qty \t qty price\n')
report.write('---------------------------------------------\n')

class To_order:
    def menu_option(self):
        print('__________________________________________________')
        print('               WELCOME TO THE MENU                ')
        print('__________________________________________________')
        print('1. To read the menu')
        print('2. To order')
        print('3. To see your order')
        print('4. To confirm order and exit')

instance = To_order()

instance.menu_option()

class CAFE_TRUCK:
    def get_order(self):
        while True:
            option = int(input("Enter your option: "))
            if option == 1:
                menu_file = open("THE MENU.txt")
                print(menu_file.read())
                menu_file.close()
                print(instance.menu_option())
            elif option == 2:
                while True:
                    order_num = input("Enter your order number (type 'done' to finish): ")
                    if order_num == "done":
                        break
                    order_num = int(order_num)
                    if order_num < 1 or order_num > len(menu):
                        print("Invalid order number. Please choose a number within the menu range.")
                        continue
                    quantity = int(input("How many items of this order?: "))
                    unit_price = menu[order_num - 1]
                    total_price = unit_price * quantity
                    report.write(f"{order_num}\t\t\t{unit_price}\t\t\t{quantity}\t\t{total_price}\n")
                    total.append(total_price)
                print(instance.menu_option())   

            elif option == 3:
                print("-----------------------------------")
                print("TOTAL:" ,sum(total))
                print(instance.menu_option())
            elif option == 4:
                print("Your total bill is:" ,sum(total))
                print("THANK YOU, HAVE A LOVELY DAY!")
                break
            else:
                print("Oops, invalid option :(")

        report.write('---------------------------------------------\n')
        report.write(f"TOTAL: {sum(total)}\n")
        report.write('---------------------------------------------\n')
        report.close()

# Creating an instance of CAFE_TRUCK
cafe_truck_instance = CAFE_TRUCK()

# Calling the get_order method
cafe_truck_instance.get_order()


