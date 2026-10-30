MENU = {
    1: {"name": "Chicken Adobo with Rice", "price": 85.00},
    2: {"name": "Beef Tapa with Rice", "price": 95.00},
    3: {"name": "Pork Sisig", "price": 120.00},
    4: {"name": "Pancit Canton", "price": 70.00},
    5: {"name": "Burger Steak with Rice", "price": 80.00},
    6: {"name": "Fried Chicken (2pcs) + Rice", "price": 90.00},
    7: {"name": "Milo With Rice", "price": 60.00},
    8: {"name": "Turon With Rice (2pcs)", "price": 30.00},
    9: {"name": "Soft Drink With Rice (Coke/Sprite)", "price": 25.00},
    10: {"name": "Bottled Water With Rice", "price": 15.00},
}


def calculate_total(cart):
    """Calculate the total price of all items in the cart."""
    total = 0.0
    for item in cart:
        total += item["price"] * item["qty"]
    return total


def add_to_cart(cart, item_num, qty):
    """Add a selected menu item to the cart."""
    selected = MENU[item_num]
    cart.append({
        "name": selected["name"],
        "price": selected["price"],
        "qty": qty
    })
    return selected["name"]