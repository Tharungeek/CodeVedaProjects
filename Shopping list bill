items = {
    "1": {"name": "Rice", "price": 140},
    "2": {"name": "Atta", "price": 160},
    "3": {"name": "Oil", "price": 200},
    "4": {"name": "Sugar", "price": 50},
    "5": {"name": "Soap", "price": 40},
    "6": {"name": "BREAD", "price": 30},
}

coupons = {
    "Taggedhe ley": 0,
    "taggi bro": 0.10,
    "plz": 0.20,
    "tharun": 0.50,
}

bill = {}


def show_item_list():
    print("\nPlease select item number. Press 0 to generate bill:")
    for item in items:
        print(item, "-", items[item]["name"])


def generate_bill(code):
    final_amount = 0

    print("\n+++ Items Purchased +++")
    print("============================")
    print("Name | Price | Qty | Amount")
    print("----------------------------")

    for item_number in bill:
        if item_number in items:
            product_price = items[item_number]["price"]
            total_products = bill[item_number]["item_count"]
            total_price = product_price * total_products

            print(
                f"{items[item_number]['name']} | {product_price} | {total_products} | {total_price}"
            )

            final_amount += total_price

    print("============================")
    discount = final_amount * coupons.get(code, 0)
    payable = final_amount - discount

    print(f"Total Bill: {final_amount}/-")
    print(f"Discount: {discount}/-")
    print(f"Amount to Pay: {payable}/-")


if __name__ == "__main__":
    print("====== Welcome to Konda Gorre Shopping Mall ======")

    show_item_list()
    user_choice = input("\nEnter your choice: ")

    while user_choice != "0":
        if user_choice in items:
            if user_choice in bill:
                bill[user_choice]["item_count"] += 1
            else:
                bill[user_choice] = {"item_count": 1}
        else:
            print("Invalid choice!")

        show_item_list()
        user_choice = input("\nEnter your choice: ")

    print("\nDo you have any coupons?")
    print("1. Yes   2. No")

    if int(input()) == 1:
        code = input("Enter coupon code: ")
        generate_bill(code)
    else:
        print("No coupon added!")
        generate_bill("Taggedhe ley")  # 0% discount