# Ask user for his name, capitalize and strips its whitespace
name = input("name? ").strip().title()

# Plit user's name into first and last name
first, last = name.split()

# Say hello to the user
print(f"Hello, {first}")
