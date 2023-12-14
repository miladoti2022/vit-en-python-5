def parse_numbers(input_str):
    try:
        numbers = [float(num) for num in input_str.split(",")]
        return numbers
    except ValueError:
        raise ValueError("Invalid input! Please enter numeric values separated by commas.")


def calculate_sum(numbers):
    return sum(numbers)


def calculate_average(numbers):
    return sum(numbers) / len(numbers) if numbers else 0
