from src.password_checker import check_password_strength


if __name__ == "__main__":
    password = input("Enter your password: ")
    result = check_password_strength(password)
    print(result)
