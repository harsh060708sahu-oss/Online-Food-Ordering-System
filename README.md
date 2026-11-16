# Online Food Ordering System

## Project Details
- **Project Number:** 45
- **Language:** Python 3
- **Developer:** Harsh Kumar Sahu
- **ERP:** RU-26-02383

## Project Mentor
- **Mentored by:** Mr. Satyaprakash Sethy(https://github.com/SATYAPRAKASHSETHY)
- **Github:** @SATYAPRAKASHSETHY(https://github.com/SATYAPRAKASHSETHY)
- **Role:** Python Mentor/ Technical Guide
## 1. Project Description

The Online Food Ordering System is a simple Python console application
that allows a user to view a food menu, add items to a shopping cart,
remove items, view the cart, and checkout to generate a final bill.

The project demonstrates the use of Python dictionaries, lists,
functions, loops, conditional statements, input validation, and basic
billing calculations.

## 2. Menu and Prices

  Food Item       Price
  ----------- ---------
  Burger        Rs. 120
  Pizza         Rs. 250
  Fries          Rs. 80
  Coke           Rs. 40

## 3. Main Features

-   Display the available food menu.
-   Add food items and quantities to the cart.
-   Increase the quantity when an item already exists in the cart.
-   Remove a selected quantity or remove an item completely.
-   View cart items and subtotal.
-   Apply the `SAVE10` coupon for a 10% discount.
-   Calculate 5% GST on the amount after discount.
-   Provide free delivery when the original subtotal is Rs. 300 or more.
-   Charge Rs. 40 delivery when the original subtotal is below Rs. 300.
-   Validate item names, quantities, coupon codes, and menu choices.
-   Clear the cart after successful checkout.

## 4. Requirements

-   Python 3.x
-   Any Python editor or IDE, such as Visual Studio Code, IDLE, or
    PyCharm.

No external Python packages are required.

## 5. How to Run

1.  Download or copy `online_food_ordering_system.py` into a folder.
2.  Open a terminal or command prompt in that folder.
3.  Run the following command:

``` bash
python online_food_ordering_system.py
```

If your system uses the `python3` command, run:

``` bash
python3 online_food_ordering_system.py
```

## 6. Application Menu

When the program starts, it displays these options:

1.  Display Menu
2.  Add Item to Cart
3.  Remove Item from Cart
4.  View Cart
5.  Checkout
6.  Exit

Enter the corresponding number to select an operation.

## 7. Billing Rules

-   **Subtotal:** Sum of each item's price multiplied by its quantity.
-   **Coupon:** Enter `SAVE10` to receive a 10% discount on the
    subtotal.
-   **GST:** 5% GST is calculated on the subtotal after discount.
-   **Delivery:** Free when the original subtotal is Rs. 300 or more;
    otherwise Rs. 40.
-   **Final Amount:** Amount after discount + GST + delivery charge.

### Sample Calculation

For Pizza × 2 and Fries × 1:

  Description                        Amount
  ----------------------- -----------------
  Subtotal                       Rs. 580.00
  SAVE10 discount (10%)          -Rs. 58.00
  Amount after discount          Rs. 522.00
  GST (5%)                        Rs. 26.10
  Delivery                  Rs. 0.00 (Free)
  **Final Total**            **Rs. 548.10**

## 8. Project Files

-   `online_food_ordering_system.py` -- Main Python source code.
-   `README.md` -- Project description and instructions.
-   `online_food_ordering_test_cases.pdf` -- Test cases and expected
    results.

Keep the files in the same project folder for easy access.

## 9. Testing

Refer to `online_food_ordering_test_cases.pdf` for test scenarios
covering menu display, valid and invalid item inputs, quantity
validation, cart removal, coupon handling, GST, delivery charges,
checkout, and exit.

---------------------------------------------------------------------
*End of README*
