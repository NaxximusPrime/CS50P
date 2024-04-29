x = float(input("What's x? "))
y = float(input("What's y? "))

# rounds to 2 digits after komma
z = round(x + y, 2)
# print (f"{z:.2f}")

# format a number to show 1,000,000 insted of 1000000
print(f"{z:,}")
