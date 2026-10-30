from calculate import MENU


def get_main_choice():
    """Get the main menu choice (A, V, C, X)."""
    return input("\nEnter choice: ").strip().upper()


def get_item_number():
    """Get a valid item number or 'B' to go back.
    Returns (item_num, None) or (None, 'B').
    """
    while True:
        item_input = input("Enter item number (or type [B] to go back): ").strip().upper()
        if item_input == "B":
            return None, "B"

        try:
            item_num = int(item_input)
            if item_num not in MENU:
                print("Invalid item number! Please choose from the menu.")
                input("Press Enter to try again...")
                continue
            return item_num, None
        except ValueError:
            print("Please enter a valid number for the item.")
            input("Press Enter to try again...")


def get_quantity():
    """Get a valid quantity (integer >= 1)."""
    while True:
        try:
            qty = int(input("Enter quantity: "))
            if qty <= 0:
                print("Quantity must be at least 1.")
                continue
            return qty
        except ValueError:
            print("Please enter a valid number for quantity.")


def get_checkout_confirmation():
    """Ask user to confirm the order (YES / NO)."""
    print("\nProceed to payment?")
    return input("Type YES to confirm order, or Type NO to go Back: ").strip().upper()


def pause():
    """Wait for user to press Enter."""
    input("Press Enter to continue...")