phone_book = {}


def add_new_contact():
    name = input("Enter contact name: ")
    number = input("Enter contact number: ")
    phone_book[name] = number
    print(f"Contact {name} added successfully!")


def edit_contact():
    name = input("Enter contact name to edit: ")
    if name in phone_book:
        print(f"Contact found: {name} - {phone_book[name]}")
        choice = input("Enter 'U' to update or 'D' to delete: ").upper()
        if choice == 'U':
            new_number = input("Enter new number: ")
            phone_book[name] = new_number
            print(f"{name}'s number updated successfully!")
        elif choice == 'D':
            del phone_book[name]
            print(f"{name} deleted from contacts.")
        else:
            print("Invalid choice!")
    else:
        print("Contact not found.")


def delete_contact():
    name = input("Enter contact name to delete: ")
    if name in phone_book:
        del phone_book[name]
        print(f"{name} deleted from contacts.")
    else:
        print("Contact not found.")


def search_contact():
    name = input("Enter contact name to search: ")
    if name in phone_book:
        print(f"Contact found: {name} - {phone_book[name]}")
    else:
        print("Contact not found.")


# i define here my main loop:


while True:
    print("\nPhone Book Menu:")
    print("1. Add New Contact")
    print("2. Edit Contact")
    print("3. Delete Contact")
    print("4. Search Contact")
    print("5. Exit")
    choice = input("Enter your choice (1-5): ")

    if choice == '1':
        add_new_contact()
    elif choice == '2':
        edit_contact()
    elif choice == '3':
        delete_contact()
    elif choice == '4':
        search_contact()
    elif choice == '5':
        print("Exiting phone book.")
        break
    else:
        print("Invalid choice. Please enter a number between 1 and 5.")

# exercise 2
import number_operations as no


def get_numbers():
    while True:
        try:
            num_input = input("Enter a series of numbers separated by commas: ")
            if not num_input:
                raise ValueError("Empty input! Please enter some numbers.")

            numbers = no.parse_numbers(num_input)
            return numbers

        except ValueError as ve:
            print(f"Error: {ve}")
            print("Please try again.")


if __name__ == "__main__":
    numbers = get_numbers()

    if numbers:
        total_sum = no.calculate_sum(numbers)
        avg = no.calculate_average(numbers)

        print(f"Sum of the numbers: {total_sum}")
        print(f"Average of the numbers: {avg}")

# exercise 3:
import utilities


def get_valid_input(prompt, input_type=int):
    while True:
        try:
            user_input = input(prompt)
            validated_input = input_type(user_input)
            return validated_input
        except ValueError:
            print("Invalid input! Please enter a valid value.")


if __name__ == "__main__":
    print("Welcome to the Utilities Program!")
    num = get_valid_input("Enter a number: ")

    fact = utilities.factorial(num)
    prime_check = utilities.is_prime(num)
    fibonacci_sequence = utilities.generate_fibonacci(num)

    print(f"The factorial of {num} is: {fact}")
    print(f"{num} {'is' if prime_check else 'is not'} a prime number.")
    print(f"The Fibonacci sequence up to {num} is: {fibonacci_sequence}")

# exercise 4:
import random


def roll_dice(sides=6):
    """
    Simulates rolling a dice with a specified number of sides.

    Args:
    sides (int): Number of sides on the dice (default is 6 for a standard dice).

    Returns:
    int: Result of the dice roll.
    """
    return random.randint(1, sides)


def main():
    print("Welcome to the Dice Simulator!")

    while True:
        user_input = input("Press 'r' or 'roll' to roll the dice. Press any other key to quit: ").lower()

        if user_input == 'r' or user_input == 'roll':
            result = roll_dice()
            print(f"You rolled: {result}")
        else:
            print("Thanks for playing!")
            break


if __name__ == "__main__":
    main()
