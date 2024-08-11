import random
import string
def generate_password(length):
    uppercase_letters = string.ascii_uppercase
    lowercase_letters = string.ascii_lowercase
    digits = string.digits
    symbols = string.punctuation
    
    all_characters = uppercase_letters + lowercase_letters + digits + symbols
    password = ''.join(random.choice(all_characters) for _ in range(length))
    return password
def main():
    while True:
        try:
            length = int(input("Enter the desired length of the password: "))
            if length < 1:
                print("Password length must be at least 1.")
            else:
                break
        except ValueError:
            print("Invalid input. Please enter a valid number.")
    password = generate_password(length)
    print(f"Generated Password: {password}")
if __name__ == "__main__":
    main()