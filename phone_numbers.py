#!/usr/bin/env python3
import re


def is_valid_phone_number(phone_str):
    # Updated regular expression to match specific phone number formats
    pattern = r'^\(\d{3}\) \d{3}-\d{4}$|^\d{3}-\d{3}-\d{4}$|^\d{3}\.\d{3}\.\d{4}$'
    return re.match(pattern, phone_str) is not None


# Test Cases
phone_1 = "(123) 456-7890"  # Valid format
phone_2 = "123-456-7890"    # Valid format
phone_3 = "123.456.7890"    # Valid format
phone_4 = "1234567890"      # Invalid (missing separators)
phone_5 = "(123)-456-7890"  # Invalid format (no space after parenthesis)
phone_6 = "(123)456-7890"   # Invalid format (missing space after parenthesis)
phone_7 = "(12) 345-67890"  # Invalid format (incorrect area code length and phone number length)

# Example Usage
print(f"{phone_1} is valid phone number: {is_valid_phone_number(phone_1)}")
print(f"{phone_2} is valid phone number: {is_valid_phone_number(phone_2)}")
print(f"{phone_3} is valid phone number: {is_valid_phone_number(phone_3)}")
print(f"{phone_4} is valid phone number: {is_valid_phone_number(phone_4)}")
print(f"{phone_5} is valid phone number: {is_valid_phone_number(phone_5)}")
print(f"{phone_6} is valid phone number: {is_valid_phone_number(phone_6)}")
print(f"{phone_7} is valid phone number: {is_valid_phone_number(phone_7)}")
