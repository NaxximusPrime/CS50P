# x = int(input("What's x? "))
#
# if x % 2 == 0:
# 	print("x is even")
# else:
# 	print("x is odd")

def main():
	x = int(input("What's x? "))
	if is_even(x):
		print("Even")
	else:
		print("Odd")


def is_even(n):
	return n % 2 == 0


main()
