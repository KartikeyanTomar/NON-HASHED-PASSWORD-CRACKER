import itertools
import string

# Brute Force Attack
def brute_force_crack(target_password, max_length):
    char_set = string.ascii_letters + string.digits + string.punctuation
    for length in range(1, max_length + 1):
        for attempt in itertools.product(char_set, repeat=length):
            attempt = ''.join(attempt)
            if attempt == target_password:
                return attempt
    return None

# Dictionary Attack
def dictionary_crack(target_password, dictionary_path):
    try:
        with open(dictionary_path, 'r') as file:
            for line in file:
                word = line.strip()
                if word == target_password:
                    return word
    except FileNotFoundError:
        print(f"Dictionary file {dictionary_path} not found.")
    return None

# Main function to demonstrate the attacks
def main():
    password_to_crack = input("Enter the password to crack: ")
    max_attempt_length = int(input("Enter the maximum length for brute force attack: "))
    dictionary_path = input("Enter the dictionary file path for dictionary attack: ")

    print("Starting dictionary attack...")
    found_password = dictionary_crack(password_to_crack, dictionary_path)
    if found_password:
        print(f"Password found using dictionary attack: {found_password}")
    else:
        print("Dictionary attack failed, starting brute force attack...")
        found_password = brute_force_crack(password_to_crack, max_attempt_length)
        if found_password:
            print(f"Password found using brute force attack: {found_password}")
        else:
            print("Brute force attack failed. Password not found.")

if __name__ == "__main__":
    main()
