import re


def is_valid_url(test_string):
    pattern = r'[(http(s)?):\/\/(www\.)?a-zA-Z0-9@:%._\+~#=]{2,256}\.[a-z]{2,6}\b([-a-zA-Z0-9@:%_\+.~#?&//=]*)'
    return re.match(pattern, test_string) is not None


user_input = input("Enter the test value: ")


if is_validurl(user_input):
    print(f"{user_input} is valid URL: {is_valid_url(user_input)}")
else:
    print(f"{is_valid_url(user_input)} : {user_input} is invalid")
