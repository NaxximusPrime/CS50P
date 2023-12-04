# =================Vertical Hashtags===============
# def main():
# 	print_column(3)
#
#
# def print_column(height):
# 	print("#\n" * height, end="")
#
#
# main()

# ============Horizontal Questionmarks=============
# def main():
# 	print_row(4)
#
#
# def print_row(width):
# 	print("?" * width)
#
#
# main()

# ===========Creation full square blocks===========
def main():
	print_square(3)


def print_square(size):
	# For each row in square
	for i in range(size):
		# For each brick in row
		for j in range(size):
			# print brick
			print("#", end="")
		print()


main()
