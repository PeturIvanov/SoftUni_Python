def shop_from_grocery_list(budget, products_list, *args):

    for product, price in args:

        if product in products_list:

            if budget >= price:
                budget -= price
                products_list.remove(product)

            else:
                break

    if products_list:
        return f"You did not buy all the products. Missing products: {', '.join(products_list)}."

    else:
        return f"Shopping is successful. Remaining budget: {budget:.2f}."


print(shop_from_grocery_list(
    100,
    ["tomato", "cola", "chips", "meat", "chocolate"],
    ("cola", 15.8),
    ("chocolate", 30),
    ("tomato", 15.85),
    ("chips", 50),
    ("meat", 22.99),
))