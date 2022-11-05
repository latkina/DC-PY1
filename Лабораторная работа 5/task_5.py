from random import sample
import string


def get_random_password() -> str:
    password_len = 8
    all_password_values = string.ascii_lowercase + string.ascii_uppercase + string.digits
    password = ''.join(sample([count for count in all_password_values], password_len))
    return password


print(get_random_password())
