# dict comprehension
menu = {"Kadahi Paneer": 450, "Matar Paneer": 350, "Chulbula Paneer": 550}
# convert menu price to dollars

dollar_menu = {
    item: f"$ {price / 100} (converted to dollar)" for item, price in menu.items()
}
print(dollar_menu)
