def shopping_cart(*args):
    result = []

    cart = {
        "Soup": {"limit": 3, "products": []},
        "Pizza": {"limit": 4, "products": []},
        "Dessert": {"limit": 2, "products": []},
    }

    def meal_done(meal_name, product_name):
        if cart[meal_name]["limit"] == len(cart[meal_name]["products"]):
            return False

        if product_name in cart[meal_name]["products"]:
            return False

        return True

    for data in args:
        if data == "Stop":
            break

        meal_name, product_name = data

        if meal_done(meal_name, product_name):
            cart[meal_name]["products"].append(product_name)

    sorted_cart = sorted(cart.items(), key=lambda x: (-len(x[1]["products"]), x[0]))

    for meal_name, info in sorted_cart:
        result.append(f"{meal_name}:")

        if info["products"]:
            result.append('\n'.join([f" - {el}" for el in sorted(info["products"])]))

    if len(result) > len(cart):
        return  '\n'.join(result)

    else:
        return "No products in the cart!"



print(shopping_cart(
    ('Pizza', 'ham'),
    ('Dessert', 'milk'),
    ('Pizza', 'ham'),
    'Stop',
))
