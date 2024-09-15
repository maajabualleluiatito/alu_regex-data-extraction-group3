import re

def is_valid_credit(credit_no):
    pattern = r'(\d{4}[-. ]?){4}|\d{4}[-. ]?\d{6}[-. ]?\d{5}'
    pattern = r'(\d{4}[-. ]?){3}\d{4}|\d{4}[-. ]?\d{6}[-. ]?\d{5}'
    return re.match(pattern, credit_no) is not None

# Test Case
credit1 = "1234 5678 9012 3456"  # Should be True (16 digits)
credit2 = "1234-5678-9012-3456"  # Should be True (16 digits with dashes)
credit3 = "3729.288899.89564"    # Should be True (15 digits in special format)
credit4 = "12345678901234567"    # Should be False (17 digits)

print(f"{credit1} is valid: {is_valid_credit(credit1)}")
print(f"{credit2} is valid: {is_valid_credit(credit2)}")
print(f"{credit3} is valid: {is_valid_credit(credit3)}")
print(f"{credit4} is valid: {is_valid_credit(credit4)}")