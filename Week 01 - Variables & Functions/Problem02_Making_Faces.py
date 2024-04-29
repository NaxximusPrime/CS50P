def main():
	convert()


def convert():
	user_input = input("Tell me something: ")
	print(user_input.replace(":)", "🙂").replace(":(", "🙁"))


main()
