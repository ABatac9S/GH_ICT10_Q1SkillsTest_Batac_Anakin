from pyscript import display, document

def create_order(e):
    name = document.getElementById("client_name").value
    address = document.getElementById("client_loc").value
    contact = document.getElementById("client_num").value

    menu = {
        "pasta_bowl": ("Pasta Bowl", 120),
        "chicken_wrap": ("Chicken Wrap", 90),
        "veggie_soup": ("Vegetable Soup", 70),
        "mint_drink": ("Mint Drink", 45),
        "bottled_water": ("Bottled Water", 25)
    }

    total = 0
    ordered_items = []

    for item_id, (label, price) in menu.items():
        checkbox = document.getElementById(item_id)
        if checkbox.checked:
            ordered_items.append(label)
            total += price

    items_list = ", ".join(ordered_items) if ordered_items else "No items selected"
    order_message = f"""
    Order for: {name}
    Address: {address}
    Contact number: {contact}
    Ordered Items: {items_list}
    Total: ₱ {total:.2f}
    """

    display("", target="result_box")
    display(order_message, target="result_box")