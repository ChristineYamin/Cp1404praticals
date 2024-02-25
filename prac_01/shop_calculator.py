
total_price = 0
user_input= int(input("Numbers of items : "))
for i in range(0,user_input):
    price=float(input("Price of the item : "))
    total_price+=price

if total_price >100 :
    discount_price= total_price*0.10
    total_price=total_price-discount_price
    print(f"Total price for {user_input} items is $ {total_price:.2f}.")
print(f"Total price for {user_input} items is $ {total_price:.2f}.")