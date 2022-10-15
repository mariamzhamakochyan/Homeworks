count_prod = int(input("Enter number of products: "))
product = {}
for i in range(count_prod):
    prod_name = input("Enter product name: ")
    product[prod_name] = int(input("Enter product price: "))

while True:
    prod_name  = input("Enter product for price or q to exit: ")
    if prod_name == ‘q’:
        break
    if prod_name in product:
        print(f'Price of {prod_name} is {product[prod_name]}')
    else:
        print(f"{prod_name} has not been added yet: ")
