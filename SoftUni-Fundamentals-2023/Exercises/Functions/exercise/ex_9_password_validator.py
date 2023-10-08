def password_validation(attempt):
    error_list = []
    if len(password) < 6 or len(password) > 10:
        error_list.append("Password must be between 6 and 10 characters")
    if not password.isalnum():
        error_list.append("Password must consist only of letters and digits")
    digits_counter = 0
    for character in attempt:
        if character.isdigit():
            digits_counter += 1
    if digits_counter < 2:
        error_list.append("Password must have at least 2 digits")
    return error_list


password = input()
errors_in_password = password_validation(password)
if not errors_in_password:
    print("Password is valid")
else:
    print("\n".join(errors_in_password))
