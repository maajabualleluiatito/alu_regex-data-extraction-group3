import re


def is_valid_hashtag(hashtag):
    pattern = r'^#[a-zA-Z0-9_]'
    return re.match(pattern, hashtag) is not None


user_input = input("Enter the test value: ")


if is_valid_hashtag(user_input):
    print(f"{user_input} is valid hashtag: {is_valid_hashtag(user_input)}")
else:
    print(f"{is_valid_hashtag(user_input)} : {user_input} is invalid")
