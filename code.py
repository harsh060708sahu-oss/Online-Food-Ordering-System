# PS No. 45 - Online Food Ordering System
# Language: Python 3
# Concepts: Lists, Dictionaries, Functions, Billing

MENU = {
    "Burger": 120,
    "Pizza": 250,
    "Fries": 80,
    "Coke": 40
}

COUPON_CODE = "SAVE10"
DISCOUNT_RATE = 0.10
GST_RATE = 0.05
DELIVERY_CHARGE = 40
FREE_DELIVERY_LIMIT = 300


def display_menu():
    """Display all available food items and their prices."""
    print("\n========== FOOD MENU ==========")
    for item, price in MENU.items():
        print(f"{item:<12} Rs.{price:.2f}")
    print("===============================")


def find_cart_item(cart, item_name):
    """Find an item in the cart (case-insensitive)."""
    for cart_item in cart:
        if cart_item["name"].lower() == item_name.lower():
            return cart_item
    return None


def add_item(cart):
    """Add an available food item to the cart."""
    display_menu()
    item_name = input("Enter item name to add: ").strip()

    # Validate item name
    actual_name = next(
        (name for name in MENU if name.lower() == item_name.lower()),
        None
    )

    if actual_name is None:
        print("Item not available. Menu: Burger, Pizza, Fries, Coke.")
        return

    # Validate quantity
    try:
        quantity = int(input("Enter quantity: "))
        if quantity <= 0:
            print("Invalid quantity. Please enter a quantity greater than 0.")
            return
    except ValueError:
        print("Invalid quantity. Please enter a whole number.")
        return

    existing_item = find_cart_item(cart, actual_name)

    if existing_item:
        existing_item["quantity"] += quantity
    else:
        cart.append({
            "name": actual_name,
            "price": MENU[actual_name],
            "quantity": quantity
        })

    print(f"{actual_name} x{quantity} added to cart.")


def remove_item(cart):
    """Remove an item or reduce its quantity in the cart."""
    if not cart:
        print("Your cart is empty.")
        return

    print("\n========== YOUR CART ==========")
    for item in cart:
        print(f'{item["name"]} x{item["quantity"]} - '
              f'Rs.{item["price"] * item["quantity"]:.2f}')

    item_name = input("Enter item name to remove: ").strip()
    cart_item = find_cart_item(cart, item_name)

    if cart_item is None:
        print("Item not found in your cart.")
        return

    try:
        quantity = int(input("Enter quantity to remove: "))
        if quantity <= 0:
            print("Invalid quantity. Enter a number greater than 0.")
            return
    except ValueError:
        print("Invalid quantity. Please enter a whole number.")
        return

    if quantity >= cart_item["quantity"]:
        cart.remove(cart_item)
        print(f'{cart_item["name"]} removed from cart.')
    else:
        cart_item["quantity"] -= quantity
        print(f'{quantity} quantity of {cart_item["name"]} removed.')


def calculate_subtotal(cart):
    """Calculate the total price of all items in the cart."""
    return sum(item["price"] * item["quantity"] for item in cart)


def apply_coupon(subtotal, coupon):
    """Apply SAVE10 coupon if valid; otherwise give no discount."""
    if coupon.strip().upper() == COUPON_CODE:
        discount = subtotal * DISCOUNT_RATE
        print("Coupon SAVE10 applied successfully!")
        return discount

    if coupon.strip() == "":
        print("No coupon applied.")
        return 0.0

    print("Invalid coupon code. Only SAVE10 is accepted.")
    return 0.0


def checkout(cart):
    """Calculate discount, GST, delivery charge and final bill."""
    if not cart:
        print("Your cart is empty. Add items before checkout.")
        return

    subtotal = calculate_subtotal(cart)

    print("\n========== CHECKOUT ==========")
    print("Your order:")
    for item in cart:
        item_total = item["price"] * item["quantity"]
        print(f'{item["name"]} x{item["quantity"]} '
              f'@ Rs.{item["price"]:.2f} = Rs.{item_total:.2f}')

    print(f"\nSubtotal: Rs. {subtotal:.2f}")

    coupon = input("Enter coupon code (press Enter for no coupon): ")
    discount = apply_coupon(subtotal, coupon)

    # GST is calculated on the amount after discount.
    amount_after_discount = subtotal - discount
    gst = amount_after_discount * GST_RATE

    # Free delivery is based on the original subtotal.
    delivery = 0.0 if subtotal >= FREE_DELIVERY_LIMIT else DELIVERY_CHARGE

    total = amount_after_discount + gst + delivery

    print("\n========== FINAL BILL ==========")
    print(f"Subtotal:          Rs. {subtotal:.2f}")
    print(f"Discount:          Rs. {discount:.2f}")
    print(f"GST (5%):          Rs. {gst:.2f}")

    if delivery == 0:
        print("Delivery:          Rs. 0.00 (Free)")
    else:
        print(f"Delivery:          Rs. {delivery:.2f}")

    print("--------------------------------")
    print(f"Total Amount:      Rs. {total:.2f}")
    print("Thank you for ordering!")
    print("================================")

    # Clear cart after successful checkout.
    cart.clear()


def view_cart(cart):
    """Display cart items and subtotal."""
    if not cart:
        print("\nYour cart is empty.")
        return

    print("\n========== YOUR CART ==========")
    for item in cart:
        item_total = item["price"] * item["quantity"]
        print(f'{item["name"]} x{item["quantity"]} - Rs.{item_total:.2f}')

    print(f"Cart subtotal: Rs. {calculate_subtotal(cart):.2f}")


def main():
    """Main program loop."""
    cart = []

    print("===================================")
    print("     ONLINE FOOD ORDERING SYSTEM")
    print("===================================")

    while True:
        print("\n1. Display Menu")
        print("2. Add Item to Cart")
        print("3. Remove Item from Cart")
        print("4. View Cart")
        print("5. Checkout")
        print("6. Exit")

        choice = input("\nEnter your choice (1-6): ").strip()

        if choice == "1":
            display_menu()
        elif choice == "2":
            add_item(cart)
        elif choice == "3":
            remove_item(cart)
        elif choice == "4":
            view_cart(cart)
        elif choice == "5":
            checkout(cart)
        elif choice == "6":
            print("Thank you for using Online Food Ordering System!")
            break
        else:
            print("Invalid choice. Please select a number from 1 to 6.")


if __name__ == "__main__":
    main()
