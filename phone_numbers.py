import re

def numbers(phone):
    phone_pattern = r"(\(?\+?\d{1,3}\)?[\s-]+)?\(?\d{1,3}\)?[\s-]+\d{3}[\s-]?\d{2}[\s-]?\d{2}"
    return re.match (phone_pattern, phone) is not None

# Test Cases

# Example Usage
number_1 ="(123) 456-7890"
number_2 = "123-456-7890"
number_3 = "123.456.7890"
number_4 = 762195728

print(f"{number_3} is valid phone: {phone_pattern(number_1)}")
print(f"{number_4} is valid phone: {phone_pattern(number_2)}")
print(f"{number_3} is valid phone: {phone_pattern(number_3)}")
print(f"{number_4} is valid phone: {phone_pattern(number_4)}")
~                                                           i
