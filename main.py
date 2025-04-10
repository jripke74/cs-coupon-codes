base_price = input("Enter cart total: ")

# Available coupon codes include 15% off and $12 off.
percent_discount = float(base_price) - float(base_price) * .15
fixed_discount = float(base_price) - 12

# Pick the coupon that offers the best discount.
final_price = min(fixed_discount, percent_discount)
print("Your best price is $" + str(round(final_price, 2)))
