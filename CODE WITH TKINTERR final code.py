import tkinter as tk
from tkinter import messagebox

menu = [200, 220, 170, 100, 130, 250, 90, 120, 50, 30, 130, 130, 100, 135, 110, 120, 120, 135, 100, 150]
total = []

class CafeTruckApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('OUR CAFE TRUCK')
        self.geometry('740x440')
        self.configure(bg='#FDADB6')

        self.welcome_page()

    def welcome_page(self):
        self.label = tk.Label(self, text='Hello!\n WELCOME TO OUR COFFEE SHOP ', bg='#FDADB6', fg='#FCFCFA', font=('Georgia', 30))
        self.label.pack(pady=10)

        self.entry_name = tk.Entry(self)
        self.entry_name.pack(pady=10)  

        self.start_button = tk.Button(self, text='START ORDERING', bg='#FDADB6', fg='#FCFCFA', font=('Elegante classica', 16), command=self.start_ordering)
        self.start_button.pack() 

    def start_ordering(self):
        self.user_name = self.entry_name.get().strip().replace(" ", "_")

        self.receipt_file = f"{self.user_name.upper()}_RECEIPT.txt"
        self.report = open(self.receipt_file, 'a')
        self.report.write('NO.\t\t unit price \t qty \t qty price\n')
        self.report.write('---------------------------------------------\n')

        self.label.config(text='OPTIONS', bg='#FDADB6', fg='#FCFCFA', font=('Georgia', 30))
        self.label.pack(pady=20)

        self.start_button.destroy()

        self.entry_name.delete(0, tk.END)  # Clear the entry

        # Configure entry_name to display text in the specified format
        self.entry_name.insert(0, f"{self.user_name}'s Order")


        self.button1 = tk.Button(self, text='Read the Menu', bg='#FDADB6', fg='#FCFCFA', font=('Elegante classica', 16), command= self.open_menu)
        self.button1.pack(pady=10)

        self.button2 = tk.Button(self, text='To order', bg='#FDADB6', fg='#FCFCFA', font=('Elegante classica', 16),command=self.order_page)
        self.button2.pack(pady=10)

        self.button3 = tk.Button(self, text='To see your total', bg='#FDADB6', fg='#FCFCFA', font=('Elegante classica', 16), command=self.show_total)
        self.button3.pack(pady=10)

        self.button4 = tk.Button(self, text='To confirm order and exit', bg='#FDADB6', fg='#FCFCFA', font=('Elegante classica', 16),command=self.confirm_exit)
        self.button4.pack(pady=10)

    def open_menu(self):
        menu_window = tk.Tk()  # Create the menu window
        menu_window.title("The Menu")
        menu_window.geometry('600x700')

        try:
            with open("THE MENU.txt", "r") as file:
                menu_option = file.readlines()
            
            
        except FileNotFoundError:
            tk.messagebox.showerror("Error", "Menu file not found.")
            return   

        for option in menu_option:
            option = option.strip()
            menu_label = tk.Label(menu_window, text=option)
            menu_label.pack() 

    def order_page(self):
        order_window = tk.Tk()
        order_window.title("ORDER PAGE.")
        order_window.geometry('440x600')
        label_text = '''
            
        MENU
-----------------------------
DISH                   PRICE
-----------------------------
----------SWEETS-------------
1-COOKIES                200
2-CHESSECAKES            220
3-BROWNIES               170
4-CREPE                  100
5-DONUTS                 130
6-CINNAMMON ROLLS        250

---------HOT DRINKS----------
7-ESPRESSO                90
8-HOT CHOCOLATE           120
9-TURKISH COFFEE          50
10-TEA                    30
11-LATTE                  130
12-CAPPUCCINO             130
13-AMERICAN0              100

--------COLD DRINKS-----------
14-ICED LATTE             135
15-ICED AMERICAN0         110
16-COLD BREW              120
17-CHOCOLATE MILKSHAKE    120
18-ICED WHITE MOCHA LATTE 135
19-V60                    100
20-ICED MATCHA LATTE      150

'''
        label = tk.Label(order_window, text = label_text)
        label.grid(row=0, column=0, columnspan=2, sticky="w")

        self.order_label = tk.Label(order_window, text = ("Enter order no:") )
        self.order_label.grid(row=1, column=0, sticky="w")
        self.order_text = tk.Entry(order_window)
        self.order_text.grid(row=1, column=1, sticky="e")

        self.quantity_label = tk.Label(order_window, text = "How many items of this order would you like?:")
        self.quantity_label.grid(row=2, column=0, sticky="w")
        self.quantity_entry = tk.Entry(order_window)
        self.quantity_entry.grid(row=2, column=1, sticky="e")

        orderingbutton = tk.Button(order_window, text = "Add order", command = self.add_order)
        orderingbutton.grid(row=3, column=0, columnspan=2)

        exit_button = tk.Button(order_window, text="Done", command=order_window.destroy)
        exit_button.grid(row=4, column=0, columnspan=2)



    def add_order(self):
        try:
            order_num = int(self.order_text.get())
            quantity = int(self.quantity_entry.get())
        except ValueError:
            tk.messagebox.showerror("Error", "Please enter valid integers for order number and quantity.")
            return

        if order_num < 1 or order_num > len(menu):
            tk.messagebox.showerror("Error", "Invalid order number. Please choose a number within the menu range.")
            return

        unit_price = menu[order_num - 1]  # Adjust the index to match the menu list
        total_price = unit_price * quantity
        self.report.write(f"{order_num}\t\t\t{unit_price}\t\t\t{quantity}\t\t{total_price}\n")
        total.append(total_price)

    def show_total(self):
        total_window = tk.Toplevel(self)
        total_window.title("Total")
        total_window.geometry('200x200')
        total_window.config(bg='#FDADB6')
        tk.Label(total_window, text=f"Total: ${sum(total)}",bg='#FDADB6', fg='#FCFCFA', font=('Elegante classica', 16)).place(x=50,y=70)     

    def confirm_exit(self):
        self.report.write('---------------------------------------------\n')
        self.report.write(f"TOTAL: {sum(total)} TL\n")
        self.report.write('---------------------------------------------\n')
        self.report.close()
        self.quit()         


app = CafeTruckApp()
app.mainloop()
