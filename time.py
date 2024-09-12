import re


def is_valid_time(time_str):
    pattern = r'^(0?[1-9]|1[0-2]):([0-5][0-9]) ?([APap][mM])?$|^([01]?[0-9]|2[0-3]):([0-5][0-9])$'
    return re.match(pattern, time_str) is not None


# Test Cases
# 00.00 AM
# 01:00 AM
# 11:00

# Example Usage
time_1 = "02:30 PM"  # 12-hour format
time_2 = "14:30"     # 24-hour format
time_3 = "25:00"     # Invalid time

print(f"{time_1} is valid time: {is_valid_time(time_1)}")
print(f"{time_2} is valid time: {is_valid_time(time_2)}")
print(f"{time_3} is valid time: {is_valid_time(time_3)}")
