#type 3 Generate a randon password of fix length

import string
import random

def generate_password(length):
    m1 = string.ascii_lowercase
    m2 = string.ascii_uppercase
    m3 = string.digits
    m4 = string.punctuation

    m = []
    m.extend(list(m1))
    m.extend(list(m2))
    m.extend(list(m3))
    m.extend(list(m4))

    random.shuffle(m)
    return "".join(m[0:length])

def main():
    print("Generate a Password.")
    
    while True:
        try:
            passlen = int(input("Enter Password length (minimum 7): "))
            if passlen < 7 :
                print("Password length must be at least 7 characters.")
                continue
            password = generate_password(passlen)
            print("Generated Password:", password)
            
            save_option = input("Do you want to save this password to a file? (yes/no): ").strip().lower()
            if save_option == "yes":
                with open("password.txt", "w") as file:
                    file.write(password)
                print("Password saved to 'password.txt'.")
            
            another = input("Do you want to generate another password? (yes/no): ").strip().lower()
            if another != "yes":
                print("Goodbye!")
                break
        
        except ValueError:
            print("Invalid input. Please enter a number.")

if __name__ == "__main__":
    main()
