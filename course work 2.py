import random
import string


def generate_random_key(length):
    key = []
    for _ in range(length):
        key.append(random.randint(1, 26))
    return key


def encrypt(message, key):
    encrypted_message = ""
    for i, char in enumerate(message):
        if char.isalpha():
            char_shift = ord('A') if char.isupper() else ord('a')
            encrypted_char = chr((ord(char) - char_shift + key[i % len(key)]) % 26 + char_shift)
        else:
            encrypted_char = char
        encrypted_message += encrypted_char
    return encrypted_message


def decrypt(encrypted_message, key):
    decrypted_message = ""
    for i, char in enumerate(encrypted_message):
        if char.isalpha():
            char_shift = ord('A') if char.isupper() else ord('a')
            decrypted_char = chr((ord(char) - char_shift - key[i % len(key)]) % 26 + char_shift)
        else:
            decrypted_char = char
        decrypted_message += decrypted_char
    return decrypted_message


def get_key_from_user():
    key = input("Enter the key sequence (comma-separated integers): ").split(',')
    key = [int(k.strip()) for k in key]
    return key


def generate_random_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password


def menu():
    print("Select an option:")
    print("1. Encrypt a message")
    print("2. Decrypt a message")
    print("3. Generate a random password")
    print("4. Quit")


# Main program loop
while True:
    menu()
    choice = input("Enter your choice (1-4): ")

    if choice == '1':
        message = input("Enter the message to encrypt: ")
        key = get_key_from_user()
        encrypted = encrypt(message, key)
        print("Encrypted message:", encrypted)
        print()
    elif choice == '2':
        encrypted_message = input("Enter the message to decrypt: ")
        key = get_key_from_user()
        decrypted = decrypt(encrypted_message, key)
        print("Decrypted message:", decrypted)
        print()
    elif choice == '3':
        password_length = int (input("Enter the length of the password: "))
        random_password = generate_random_password(password_length)
        print("Random password:", random_password)
        print()
    elif choice == '4':
        break
    else:
        print("Invalid choice. Please try again.")
        print()