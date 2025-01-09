'''
---------------
 CS 458       |
 Fall 2024    |
 Nam Gyu Lee  |
 Assignment 1 |
 Main         |
---------------
'''
# Import libraries
from functions import function

while True:
    print("Choose an option:")
    print("1. Encryption")
    print("2. Decryption")
    print("3. Brute Force Attack")
    choice = input("Enter your choice (1/2/3): ")
    
    if choice == '1':
        while True:
            try:
                # Get user's plaintext and key
                text = input("Enter plaintext: ")
                
                # Handle wrong key value, non-numeric.
                try:
                    key = int(input("Enter key: "))
                except ValueError:
                    raise ValueError("\nWrong key value. Enter 'numeric' key.\n")
                
                ciphertext = function.encryption(text, key)
                print('\nCiphertext:', ciphertext)
                
                break
            
            # Display Error message if empty plaintext.
            # And get user's plaintext
            except ValueError as value:
                print(value)
        break
    
    elif choice == '2':
        while True:
            try:
                # Get user's ciphertext and key
                text = input("Enter ciphertext: ")
                
                # Handle wrong key value, non-numeric.
                try:
                    key = int(input("Enter key: "))
                except ValueError:
                    raise ValueError("\nWrong key value. Enter 'numeric' key.\n")
                
                plaintext = function.decryption(text, key)
                print('\nPlaintext:', plaintext)
                
                break
            
            # Display Error message if empty plaintext.
            # And get user's plaintext
            except ValueError as value:
                print(value)
        
        break
    
    elif choice == '3':
        while True:
            try:
                result_key = None
                result_text = None
                
                text = input("Enter ciphertext: ")
                print('Result of Brute Force Attack')
                
                for key in range(26):
                    plaintext = function.decryption(text, key)
                    result = function.check(plaintext, key)
                    
                    print(f'key {key}: {plaintext}')
                    
                    if result:
                        result_key = key
                        result_text = plaintext
                    
                        
                if result_key is not None:
                    print(f'\nkey and plaintext of {text}:\n{result_key}: {result_text}')
                    
                else:
                    print("Cannot find plaintext of your ciphertext.")
                
                break
    
            except ValueError as value:
                print(value)
                
        break
    
    else:
        print(f"\n'{choice}' is not a valid option. Enter 1, 2, or 3.\n")
                
    