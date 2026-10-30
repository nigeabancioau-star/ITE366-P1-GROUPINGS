from calculate import MENU, calculate_total


def clear_screen():
    print("\n" * 2)


def show_menu():
    print("=" * 50)
    print("          CANTEEN MENU (₱)")
    print("=" * 50)
    for num, item in MENU.items():
        print(f"  {num:2}. {item['name']:<30} ₱{item['price']:.2f}")
    print("=" * 50)


def show_cart(cart):
    """Display the current cart and return the total."""
    if not cart:
        print("\nYour cart is empty.")
        return 0.0

    print("\n" + "-" * 50)
    print("YOUR ORDER:")
    print("-" * 50)
    total = calculate_total(cart)
    for i, item in enumerate(cart, 1):
        subtotal = item["price"] * item["qty"]
        print(f"  {i}. {item['name']} x{item['qty']}  =  ₱{subtotal:.2f}")
    print("-" * 50)
    print(f"  TOTAL: ₱{total:.2f}")
    print("-" * 50)
    return total


def show_order_confirmed(total):
    print("\n" + "=" * 50)
    print("          ORDER CONFIRMED!")
    print(f"          Please pay ₱{total:.2f}")
    print("          Thank you! Enjoy your meal!")
    print("=" * 50)


def show_goodbye():
    print("\nThank you! Goodbye!")


def show_invalid_choice():
    print("Invalid choice! Please choose A, V, C, or X.")


def show_added_item(qty, name):
    print(f"\nAdded {qty}x {name} to cart.")