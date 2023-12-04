def main():
	x = get_int("What's x? ")
	print(f"x is {x}")


def get_int(prompt):
	while True:
		try:
			return int(input(prompt))  # all in one line or define a variable and return it later
		except ValueError:
			print("x is not a number. Try again.")  # or just pass(...) it to don't show it to the user.


main()
