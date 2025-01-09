'''
---------------
 CS 458       |
 Fall 2024    |
 Nam Gyu Lee  |
 Assignment 2 |
 Main         |
---------------
'''
# Import libraries
from functions import functions
import binascii

while True:
    print("\nChoose an option:")
    print("1. Shift Cipher")
    print("2. Permutation Cipher")
    print("3. Simple Transposition")
    print("4. Double Transposition")
    print("5. Vigenère Cipher")
    print("6. AES-128")
    print("7. DES")
    print("8. 3DES")
    choice = input("Enter your choice (1/2/3/4/5/6/7/8): ")
    
    mode = input("Do you want Encryption or Decryption? ")
    mode = mode.lower()
    if mode not in ['encryption', 'decryption']:
        raise ValueError("Mode must be either 'encryption' or 'decryption'.")
    
    if choice == '1':
        # If user wants encryption
        if mode == 'encryption':
            while True:
                try:
                    # Get user's plaintext and key
                    text = input("Enter plaintext: ")
                    
                    key_input = input("Enter key (or press Enter to use the default key): ")
                    if key_input == '':
                        key = 3

                    # Handle wrong key value, non-numeric.
                    else:
                        try:
                            key = int(key_input)
                        except ValueError:
                            raise ValueError("\nWrong key value. Enter 'numeric' key.\n")
                    
                    ciphertext = functions.shift_cipher(text, key, mode)
                    print('\nCiphertext:', ciphertext)
                    
                    break
                
                # Display Error message if empty plaintext.
                # And get user's plaintext
                except ValueError as value:
                    print(value)
            break

        elif mode == 'decryption':
            while True:
                try:
                    # Get user's ciphertext and key
                    text = input("Enter Ciphertext: ")
                    
                    key_input = input("Enter key (or press Enter to use the default key): ")
                    if key_input == '':
                        key = 3

                    # Handle wrong key value, non-numeric.
                    else:
                        try:
                            key = int(key_input)
                        except ValueError:
                            raise ValueError("\nWrong key value. Enter 'numeric' key.\n")
                    
                    plaintext = functions.shift_cipher(text, key, mode)
                    print('\nPlaintext:', plaintext)
                    
                    break
                
                # Display Error message if empty ciphertext.
                # And get user's ciphertext
                except ValueError as value:
                    print(value)
            break
    
    elif choice == '2':
        if mode == 'encryption':
            while True:
                try:
                    # Get user's ciphertext and key
                    text = input("Enter plaintext: ")
                    
                    key_input = input("Enter key (or press Enter to use the default key): ")
                    if key_input == "":
                        key = None  # Use default key

                    # Handle wrong key value, non-numeric.
                    else:
                        try:
                            key = list(map(int, key_input.split(',')))
                        except ValueError:
                            raise ValueError("\nWrong key value. Enter 'numeric' key.\n")
                    
                    ciphertext = functions.permutation_cipher(text, key, mode)
                    print('\nCiphertext:', ciphertext, '\n')
                    
                    break
                
                # Display Error message if empty plaintext.
                # And get user's plaintext
                except ValueError as value:
                    print(value)
            
            break

        elif mode == 'decryption':
            while True:
                try:
                    # Get user's ciphertext and key
                    text = input("Enter Ciphertext: ")
                    
                    key_input = input("Enter key (or press Enter to use the default key): ")
                    if key_input == "":
                        key = None  # Use default key

                    # Handle wrong key value, non-numeric.
                    else:
                        try:
                            key = list(map(int, key_input.split(',')))
                        except ValueError:
                            raise ValueError("\nWrong key value. Enter 'numeric' key.\n")
                    
                    plaintext = functions.permutation_cipher(text, key, mode)
                    print('\nPlaintext:', plaintext, '\n')
                    
                    break
                
                # Display Error message if empty ciphertext.
                # And get user's ciphertext
                except ValueError as value:
                    print(value)
            break
    
    elif choice == '3':
        if mode == 'encryption':
            while True:
                try:
                    # Get user's plaintext and key
                    text = input("Enter plaintext: ")
                    
                    key_input = input("Enter key (or press Enter to use the default key): ")
                    if key_input == "":
                        key = 3  # Use default key

                    # Handle wrong key value, non-numeric.
                    else:
                        try:
                            key = key_input
                        except ValueError:
                            raise ValueError("\nWrong key value. Enter 'numeric' key.\n")
                    
                    ciphertext = functions.simple_tranpos(text, key, mode)
                    print('\nCiphertext:', ciphertext)
                    
                    break
                
                # Display Error message if empty plaintext.
                # And get user's plaintext
                except ValueError as value:
                    print(value)
            
            break

        elif mode == 'decryption':
            while True:
                try:
                    # Get user's ciphertext and key
                    text = input("Enter Ciphertext: ")
                    
                    key_input = input("Enter key (or press Enter to use the default key): ")
                    if key_input == "":
                        key = 3  # Use default key

                    # Handle wrong key value, non-numeric.
                    else:
                        try:
                            key = key_input
                        except ValueError:
                            raise ValueError("\nWrong key value. Enter 'numeric' key.\n")
                    
                    plaintext = functions.simple_tranpos(text, key, mode)
                    print('\nPlaintext:', plaintext)
                    
                    break
                
                # Display Error message if empty ciphertext.
                # And get user's ciphertext
                except ValueError as value:
                    print(value)
            break
    
    elif choice == '4':
        if mode == 'encryption':
            while True:
                try:
                    # Get user's plaintext and key
                    text = input("Enter plaintext: ")
                    
                    key_input1 = input("Enter the first key (or press Enter to use the default key): ")
                    if key_input1 == "":
                        key1 = 3  # Use default key

                    key_input2 = input("Enter the second key (or press Enter to use the default key): ")
                    if key_input2 == "":
                        key2 = 3 # Use default key

                    # Handle wrong key value, non-numeric.
                    else:
                        try:
                            key1 = key_input1
                            key2 = key_input2
                        except ValueError:
                            raise ValueError("\nWrong key value. Enter 'numeric' key.\n")
                    
                    ciphertext = functions.double_tranpos(text, key1, key2, mode)
                    print('\nCiphertext:', ciphertext)
                    
                    break
                
                # Display Error message if empty plaintext.
                # And get user's plaintext
                except ValueError as value:
                    print(value)
            
            break

        elif mode == 'decryption':
            while True:
                try:
                    # Get user's ciphertext and key
                    text = input("Enter Ciphertext: ")
                    
                    key_input1 = input("Enter the first key (or press Enter to use the default key): ")
                    if key_input1 == "":
                        key1 = 3  # Use default key

                    key_input2 = input("Enter the second key (or press Enter to use the default key): ")
                    if key_input2 == "":
                        key2 = 3 # Use default key

                    # Handle wrong key value, non-numeric.
                    else:
                        try:
                            key1 = key_input1
                            key2 = key_input2
                        except ValueError:
                            raise ValueError("\nWrong key value. Enter 'numeric' key.\n")
                    
                    plaintext = functions.double_tranpos(text, key1, key2, mode)
                    print('\nPlaintext:', plaintext)
                    
                    break
                
                # Display Error message if empty ciphertext.
                # And get user's ciphertext
                except ValueError as value:
                    print(value)
            break 
    
    elif choice == '5':
        if mode == 'encryption':
            while True:
                try:
                    # Get user's plaintext and key
                    text = input("Enter plaintext: ")
                    
                    key_input = input("Enter the alphabetic key (or press Enter to use the default key): ")
                    if key_input == "":
                        key = "ctyiqr"  # Use default key

                    # Handle wrong key value, non-alphabetic.
                    else:
                        key = key_input

                        if not key.isalpha():
                            raise ValueError("\nInvalid key value. Key must only contain alphabetic characters.\n")
                    
                    ciphertext = functions.vigenere_cipher(text, key, mode)
                    print('\nCiphertext:', ciphertext)
                    
                    break
                
                # Display Error message if empty plaintext.
                # And get user's plaintext
                except ValueError as value:
                    print(value)
            
            break

        elif mode == 'decryption':
            while True:
                try:
                    # Get user's ciphertext and key
                    text = input("Enter ciphertext: ")

                    key_input = input("Enter the alphabetic key (or press Enter to use the default key): ")
                    if key_input == "":
                        key = "ctyiqr"  # Use default key

                    # Handle wrong key value, non-alphabetic.
                    else:
                        key = key_input

                        if not key.isalpha():
                            raise ValueError("\nInvalid key value. Key must only contain alphabetic characters.\n")
                    
                    plaintext = functions.vigenere_cipher(text, key, mode)
                    print("\nPlaintext: ", plaintext)

                    break
                
                # Display Error message if empty ciphertext.
                # And get user's ciphertext
                except ValueError as value:
                    print(value)
            
            break
    
    elif choice == '6':     # AES-128
        # Get user's encryption mode
        print('\nChoose encryption mode:')
        print('a. ECB')
        print('b. CBC')
        print('c. OFB')
        encrypt_mode = input('Enter your choice (a/b/c): ').lower()

        if encrypt_mode == 'a':
            encryption_mode = 'ecb'
        elif encrypt_mode == 'b':
            encryption_mode = 'cbc'
        elif encrypt_mode == 'c':
            encryption_mode = 'ofb'
        else:
            raise ValueError("Invalid input. Please choose either a, b, or c")

        if mode == 'encryption':
            while True:
                try:
                    # Get user's plaintext
                    text = input('Enter plaintext: ')

                    key_input = input("Enter the key (or press Enter to use the random generated key): ")
                    if key_input == "":
                        key = None
                    else:
                        key = binascii.unhexlify(key_input)     # Convert hexadecimal string to byte
                    
                    iv = None

                    if encryption_mode in ['cbc', 'ofb']:
                        iv_input = input('Enter the Initial Vector (or press Enter to use randomly generated IV): ')
                        
                        if iv_input == "":
                            iv = None
                        else:
                            iv = binascii.unhexlify(iv_input)
                    
                    ciphertext, key_out, iv_out = functions.aes(text, key, iv, mode=mode, encryption_mode=encryption_mode)

                    ciphertext = binascii.hexlify(ciphertext).decode('utf-8')       # Convert byte to String
                    key_out = binascii.hexlify(key_out).decode('utf-8')             # Convert byte to String

                    print('\nCiphertext: ', ciphertext, '\nKey: ', key_out)

                    if encryption_mode in ['cbc', 'ofb']:
                        iv_out = binascii.hexlify(iv_out).decode('utf-8')               # Convert byte to String
                        print('IV: ', iv_out)
                    
                    break

                # Display Error message if empty plaintext.
                # And get user's plaintext
                except ValueError as value:
                    print(value)
            
            break

        elif mode == 'decryption':
            while True:
                try:
                    # Get user's ciphertext
                    text = input('Enter ciphertext: ')
                    text = binascii.unhexlify(text)     # Convert hexadecimal string to byte

                    key_input = input('Enter the key (or press Enter to use the random generated key): ')
                    if key_input == "":
                        key = None
                    else:
                        key = binascii.unhexlify(key_input)     # Convert hexadecimal string to byte
                    
                    if encryption_mode in ['cbc', 'ofb']:
                        iv_input = binascii.unhexlify(input('Enter the Initial Vector: '))
                    elif encryption_mode == 'ecb':
                        iv_input = None
                    
                    plaintext, key_out, iv_out = functions.aes(text, key, iv=iv_input, mode=mode, encryption_mode=encryption_mode)

                    key_out = binascii.hexlify(key_out).decode('utf-8')     # Convert byte to String

                    print('\nPlaintext: ', plaintext, '\nKey: ', key_out)
                    if encryption_mode in ['cbc', 'ofb']:
                        iv_out = binascii.hexlify(iv_out).decode('utf-8')       # Convert byte to String
                        print('IV: ', iv_out)
                    
                    break

                # Display Error message if empty ciphertext.
                # And get user's ciphertext
                except ValueError as value:
                    print(value)
            
            break

    elif choice == '7':     # DES
        # Get user's encryption mode
        print('\nChoose encryption mode:')
        print('a. ECB')
        print('b. CBC')
        print('c. OFB')
        encrypt_mode = input('Enter your choice (a/b/c): ').lower()

        if encrypt_mode == 'a':
            encryption_mode = 'ecb'
        elif encrypt_mode == 'b':
            encryption_mode = 'cbc'
        elif encrypt_mode == 'c':
            encryption_mode = 'ofb'
        else:
            raise ValueError("Invalid input. Please choose either a, b, or c")
        
        if mode == 'encryption':
            while True:
                try:
                    # Get user's plaintext
                    text = input('Enter plaintext: ')

                    key_input = input("Enter the key (or press Enter to use the random generated key): ")
                    if key_input == "":
                        key = None
                    else:
                        key = binascii.unhexlify(key_input)     # Convert hexadecimal string to byte
                    
                    iv = None
                    
                    if encryption_mode in ['cbc', 'ofb']:
                        iv_input = input('Enter the Initial Vector (or press Enter to use randomly generated IV): ')
                        
                        if iv_input == "":
                            iv = None
                        else:
                            iv = binascii.unhexlify(iv_input)

                    
                    ciphertext, key_out, iv_out = functions.des(text, key, iv, mode=mode, encryption_mode=encryption_mode)

                    ciphertext = binascii.hexlify(ciphertext).decode('utf-8')       # Convert byte to String
                    key_out = binascii.hexlify(key_out).decode('utf-8')             # Convert byte to String

                    print('\nCiphertext: ', ciphertext, '\nKey: ', key_out)

                    if encryption_mode in ['cbc', 'ofb']:
                        iv_out = binascii.hexlify(iv_out).decode('utf-8')               # Convert byte to String
                        print('IV: ', iv_out)
                    
                    break

                # Display Error message if empty plaintext.
                # And get user's plaintext
                except ValueError as value:
                    print(value)
            
            break

        elif mode == 'decryption':
            while True:
                try:
                    # Get user's ciphertext
                    text = input('Enter ciphertext: ')
                    text = binascii.unhexlify(text)     # Convert hexadecimal string to byte

                    key_input = input('Enter the key (or press Enter to use the random generated key): ')
                    if key_input == "":
                        key = None
                    else:
                        key = binascii.unhexlify(key_input)     # Convert hexadecimal string to byte
                    
                    if encryption_mode in ['cbc', 'ofb']:
                        iv_input = binascii.unhexlify(input('Enter the Initial Vector: '))
                    elif encryption_mode == 'ecb':
                        iv_input = None
                    
                    plaintext, key_out, iv_out = functions.des(text, key, iv=iv_input, mode=mode, encryption_mode=encryption_mode)

                    key_out = binascii.hexlify(key_out).decode('utf-8')     # Convert byte to String

                    print('\nPlaintext: ', plaintext, '\nKey: ', key_out)
                    if encryption_mode in ['cbc', 'ofb']:
                        iv_out = binascii.hexlify(iv_out).decode('utf-8')       # Convert byte to String
                        print('IV: ', iv_out)
                    
                    break

                # Display Error message if empty ciphertext.
                # And get user's ciphertext
                except ValueError as value:
                    print(value)
            
            break

    
    elif choice == '8':     # 3DES
        # Get user's encryption mode
        print('\nChoose encryption mode:')
        print('a. ECB')
        print('b. CBC')
        print('c. OFB')
        encrypt_mode = input('Enter your choice (a/b/c): ').lower()

        if encrypt_mode == 'a':
            encryption_mode = 'ecb'
        elif encrypt_mode == 'b':
            encryption_mode = 'cbc'
        elif encrypt_mode == 'c':
            encryption_mode = 'ofb'
        else:
            raise ValueError("Invalid input. Please choose either a, b, or c")
        
        if mode == 'encryption':
            while True:
                try:
                    # Get user's plaintext
                    text = input('Enter plaintext: ')

                    key_input = input("Enter the key (or press Enter to use the random generated key): ")
                    if key_input == "":
                        key = None
                    else:
                        key = binascii.unhexlify(key_input)     # Convert hexadecimal string to byte
                    
                    iv = None
                    
                    if encryption_mode in ['cbc', 'ofb']:
                        iv_input = input('Enter the Initial Vector (or press Enter to use randomly generated IV): ')
                        
                        if iv_input == "":
                            iv = None
                        else:
                            iv = binascii.unhexlify(iv_input)

                    
                    ciphertext, key_out, iv_out = functions.des3(text, key, iv, mode=mode, encryption_mode=encryption_mode)

                    ciphertext = binascii.hexlify(ciphertext).decode('utf-8')       # Convert byte to String
                    key_out = binascii.hexlify(key_out).decode('utf-8')             # Convert byte to String

                    print('\nCiphertext: ', ciphertext, '\nKey: ', key_out)

                    if encryption_mode in ['cbc', 'ofb']:
                        iv_out = binascii.hexlify(iv_out).decode('utf-8')               # Convert byte to String
                        print('IV: ', iv_out)
                    
                    break

                # Display Error message if empty plaintext.
                # And get user's plaintext
                except ValueError as value:
                    print(value)
            
            break

        elif mode == 'decryption':
            while True:
                try:
                    # Get user's ciphertext
                    text = input('Enter ciphertext: ')
                    text = binascii.unhexlify(text)     # Convert hexadecimal string to byte

                    key_input = input('Enter the key (or press Enter to use the random generated key): ')
                    if key_input == "":
                        key = None
                    else:
                        key = binascii.unhexlify(key_input)     # Convert hexadecimal string to byte
                    
                    if encryption_mode in ['cbc', 'ofb']:
                        iv_input = binascii.unhexlify(input('Enter the Initial Vector: '))
                    elif encryption_mode == 'ecb':
                        iv_input = None
                    
                    plaintext, key_out, iv_out = functions.des3(text, key, iv=iv_input, mode=mode, encryption_mode=encryption_mode)

                    key_out = binascii.hexlify(key_out).decode('utf-8')     # Convert byte to String

                    print('\nPlaintext: ', plaintext, '\nKey: ', key_out)
                    if encryption_mode in ['cbc', 'ofb']:
                        iv_out = binascii.hexlify(iv_out).decode('utf-8')       # Convert byte to String
                        print('IV: ', iv_out)
                    
                    break

                # Display Error message if empty ciphertext.
                # And get user's ciphertext
                except ValueError as value:
                    print(value)
            
            break
                    
    else:
        print(f"\n'{choice}' is not a valid option. Enter either 1, 2, 3, 4, 5, 6, 7, or 8.\n")