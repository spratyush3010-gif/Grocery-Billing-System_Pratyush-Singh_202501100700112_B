x = int(input("Enter total products: "))
total_price = 0

for i in range(x):
    a = int(input("Enter the price of product: "))
    total_price += a   

if total_price > 100:
    print("You get a discount of 10%")
    discount = total_price * 0.1
    total_price -= discount

print("Total price after discount: ", total_price)
