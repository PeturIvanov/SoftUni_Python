def shopping_list(number, **kwargs):
    budget = number

    if budget < 100:
        return "You do not have enough budget."

    basket_size = 5
    basket = []
    result = []

    for product_name, data in kwargs.items():
        product_price, quantity = data

        total_price = product_price * quantity

        if len(basket) == basket_size:
            break

        if total_price <= budget:
            budget -= total_price

            result.append(f"You bought {product_name} for {total_price:.2f} leva.")

            basket.append(product_name)

    return '\n'.join(result)

print(shopping_list(104,
                    cola=(1.20, 2),
                    candies=(0.25, 15),
                    bread=(1.80, 1),
                    pie=(10.50, 5),
                    tomatoes=(4.20, 1),
                    milk=(2.50, 2),
                    juice=(2, 3),
                    eggs=(3, 1),
                    ))