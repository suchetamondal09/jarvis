import tkinter as tk
from tkinter import messagebox

# Menu with prices
menu = {
    'Pasta': 50,
    'Pizza': 250,
    'Burger': 50,
    'Juice': 60,
    'Salad': 40,
    'Coffee': 80
}

# GUI window
app = tk.Tk()
app.title("Out of Beyond - Order System")
app.geometry("400x500")

order_total = 0
order_list = []

#add to order
def add_to_order():
    global order_total
    item = item_choice.get()
    qty = qty_entry.get()

    if not qty.isdigit():
        messagebox.showerror("Error", "Please enter a number")
        return

    qty = int(qty)
    cost = menu[item] * qty
    order_total += cost
    order_listbox.insert(tk.END, f"{qty} x {item} = ₹{cost}")
    total_label.config(text=f"Total: ₹{order_total}")

#finalize
def finalize():
    global order_total
    if is_member.get():
        discount = order_total * 0.1
        order_total -= discount
        messagebox.showinfo("Discount", f"10% Discount: ₹{discount:.2f}")
    total_label.config(text=f"Total: ₹{order_total:.2f}")

#submit review
def submit_review():
    review = review_input.get("1.0", tk.END).strip()
    messagebox.showinfo("Review", f"Thanks for your review:\n{review}")
    app.quit()

# GUI layout
tk.Label(app, text="Welcome to Out of Beyond", font=("Arial", 14, "bold")).pack(pady=10)

#item dropdown
tk.Label(app, text="Choose Item").pack()
item_choice = tk.StringVar(value="Pasta")
tk.OptionMenu(app, item_choice, *menu).pack()

#Quantity input
tk.Label(app, text="Quantity").pack()
qty_entry = tk.Entry(app)
qty_entry.pack()


#add to order buttom
tk.Button(app, text="Add to Order", command=add_to_order).pack(pady=10)


#list of order items
tk.Label(app, text="Your Order").pack()
order_listbox = tk.Listbox(app, width=60)
order_listbox.pack()


#Total bill display
total_label = tk.Label(app, text="Total: ₹0")
total_label.pack(pady=5)


#checkbox for regular number
is_member = tk.IntVar()
tk.Checkbutton(app, text="Regular Member (10% off)", variable=is_member).pack()


#Finalize button(apply discount)
tk.Button(app, text="Finalize Order", command=finalize, bg="red", fg="white").pack(pady=10)


#Review input 
tk.Label(app, text="Write a Review").pack()
review_input = tk.Text(app, height=5, width=40)
review_input.pack()


#Submit input
tk.Button(app, text="Submit Review & Exit", command=submit_review, bg="blue", fg="white").pack(pady=10)

app.mainloop()