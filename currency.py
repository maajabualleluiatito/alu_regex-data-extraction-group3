#!/usr/bin/env python3

import re


def is_valid_currency(currency_str):
    # Regular expression to match currency amounts like $19.99 or $1,234.56
    pattern = r'^\$\d{1,3}(,\d{3})*(\.\d{2})?$'
    return re.match(pattern, currency_str) is not None


# Test Cases
currency_1 = "$19.99"     # Valid currency
currency_2 = "$1,234.56"  # Valid currency
currency_3 = "$123456"    # Invalid format (missing comma and decimal)
currency_4 = "$12,34.56"  # Invalid format (incorrect grouping)

# Example Usage
print(f"{currency_1} is valid currency: {is_valid_currency(currency_1)}")
print(f"{currency_2} is valid currency: {is_valid_currency(currency_2)}")
print(f"{currency_3} is valid currency: {is_valid_currency(currency_3)}")
print(f"{currency_4} is valid currency: {is_valid_currency(currency_4)}")
