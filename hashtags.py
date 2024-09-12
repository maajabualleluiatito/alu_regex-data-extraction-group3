import re


def is_valid_hashtag(hashtag):
    pattern = r'^#[a-zA-Z0-9_]'
    return re.match(pattern, hashtag) is not None

# Test Cases


# Example Usage
hashtag_1 = "hello"  # invalid hashtag
hashtag_2 = "hello#world"  # Invalid hashtag
hashtag_3 = "#hello-world"  # valid hashtag
hashtag_4 = 'hello#hello'  # Invalid hashtag

print(f"{hashtag_3} is valid hashtag: {is_valid_hashtag(hashtag_3)}")
print(f"{hashtag_4} is valid hashtag: {is_valid_hashtag(hashtag_4)}")
