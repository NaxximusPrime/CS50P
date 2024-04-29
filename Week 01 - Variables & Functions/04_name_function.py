def main():
	name = input("What's your name? ")
	hello(name)  # calling the function with input


def hello(to="World"):  # parameter with default
	print("Hello,", to)


# hello()  # calling the function with default

main()  # calling the main function
