import random
import string
import sys

def show_header():
    print("\n==================================================")
    print("             CODSOFT PASSWORD GENERATOR           ")
    print("==================================================")

def main():
    while True:
        try:
            show_header()
            
            # Request password character limit
            length_input = input("Enter desired password length (or type 'exit'): ").strip()
            if length_input.lower() in ['exit', 'quit']:
                print("\nExiting Password Generator. Goodbye!")
                break
                
            length = int(length_input)
            if length < 4:
                print("\033[1;31mError: Security length must be at least 4 characters.\033[0m")
                continue
                
            # Define standard cryptographic character pools
            letters = string.ascii_letters
            digits = string.digits
            symbols = string.punctuation
            
            # Combine pools for complex generation
            all_characters = letters + digits + symbols
            
            # Ensure the password contains at least one of each character type for true complexity
            password_chars = [
                random.choice(string.ascii_lowercase),
                random.choice(string.ascii_uppercase),
                random.choice(digits),
                random.choice(symbols)
            ]
            
            # Fill the remainder of the requested length
            password_chars += [random.choice(all_characters) for _ in range(length - 4)]
            
            # Shuffle the combined list matrix to randomize structural patterns
            random.shuffle(password_chars)
            final_password = "".join(password_chars)
            
            print("--------------------------------------------------")
            print(f"Generated Password: \033[1;32m{final_password}\033[0m")
            print("==================================================")
            
        except ValueError:
            print("\033[1;31mError: Please enter a valid whole numerical digit.\033[0m")
        except (KeyboardInterrupt, EOFError):
            print("\nExiting.")
            break

if __name__ == "__main__":
    main()