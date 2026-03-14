def calculate_average(numbers):
    total = sum(numbers)
    average = total / len(numbers)
    return average

# Example usage
digits = [200, 120, 76, 90, 50]
print("Average:", calculate_average(digits))