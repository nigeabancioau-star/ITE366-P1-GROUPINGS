from calculate import add_to_cart
from display import (
    clear_screen,
    show_menu,
    show_cart,
    show_order_confirmed,
    show_goodbye,
    show_invalid_choice,
    show_added_item,
)
from input import (
    get_main_choice,
    get_item_number,
    get_quantity,
    get_checkout_confirmation,
    pause,
)


def main():
    cart = []

    while True:
        clear_screen()
        show_menu()
        print("\nOptions:")
        print("  [A] Add item to order")
        print("  [V] View cart")
        print("  [C] Checkout")
        print("  [X] Exit")

        choice = get_main_choice()

        if choice == "A":
            item_num, go_back = get_item_number()
            if go_back == "B":
                continue

            qty = get_quantity()
            name = add_to_cart(cart, item_num, qty)
            show_added_item(qty, name)
            pause()

        elif choice == "V":
            show_cart(cart)
            pause()

        elif choice == "C":
            total = show_cart(cart)
            if total == 0:
                pause()
                continue

            confirm = get_checkout_confirmation()

            if confirm == "YES":
                show_order_confirmed(total)
                cart.clear()
                break
            elif confirm == "NO":
                print("\nReturning to menu...")
                pause()
            else:
                print("Invalid choice. Returning to menu...")
                pause()

        elif choice == "X":
            show_goodbye()
            break

        else:
            show_invalid_choice()
            pause()

if'__name__'== "_main_":
    main()