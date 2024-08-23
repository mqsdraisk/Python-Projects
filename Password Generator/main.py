import random
import string

# Defining a function to generate password:
def generate_password(length=12, include_special_characters=True):

    #defining base variables:
    letters = string.ascii_letters
    digits = string.digits
    specials = string.punctuation

    #creating a base password:
    base_pwd = letters + digits
    if include_special_characters:
        base_pwd += specials
    
    #generating the password:
    password = "".join(random.choice(base_pwd) for _ in range(length))

    return password

# getting user preferences:
try:
    length = int(input("Enter your password length: "))
except ValueError:
    print("Invalid value for password length. Set to default value 12.")
    length = 12

include_special_characters = input("Do you want to use Special Characters? (yes/no): ").strip().lower()=="yes"

generated_password = generate_password(length, include_special_characters)
print(f"Your new generated password: {generated_password}")