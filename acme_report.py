from random import randint, sample, uniform
from acme import Product

# Useful to use with random.sample to generate names
ADJECTIVES = ['Awesome', 'Shiny', 'Impressive', 'Portable', 'Improved']
NOUNS = ['Anvil', 'Catapult', 'Disguise', 'Mousetrap', '???']


def generate_products(num_products=30):
    products = []
    for i in range(num_products):
        product = Product(f'{sample(ADJECTIVES, 1)} {sample(NOUNS, 1)}',
                          randint(5, 100), randint(5, 100), uniform(0.0, 2.5))
        products.append(product)
    return products


def inventory_report(products):
    unique_names = []
    total_price = 0
    total_weight = 0
    total_flam = 0.0
    for i in products:
        if i.name not in unique_names:
            unique_names.append(i.name)
        total_price += i.price
        total_weight += i.weight
        total_flam += i.flammability
    num_uniq_names = len(unique_names)
    avg_price = total_price / len(products)
    avg_weight = total_weight / len(products)
    avg_flam = total_flam / len(products)
    print("ACME CORPORATION OFFICIAL INVENTORY REPORT")
    print(f"Unique product names: {num_uniq_names}")
    print(f"Average price: {avg_price}")
    print(f"Average weight: {avg_weight}")
    print(f"Average flammability: {avg_flam}")


if __name__ == '__main__':
    inventory_report(generate_products())
