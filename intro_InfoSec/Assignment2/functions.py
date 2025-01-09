'''
---------------
 CS 458       |
 Fall 2024    |
 Nam Gyu Lee  |
 Assignment 2 |
 Functions    |
---------------
'''

from Crypto.Cipher import AES, DES, DES3
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes


class functions:
    def shift_cipher(texts, key, mode = 'encryption'):
        # Raise error if empty plaintext.
        if not texts:
            raise ValueError("\nYou typed empty plaintext. Enter your plaintext.\n")
        
        result = ""

        if mode == 'decryption':
            key = -key

        elif mode == 'encryption':
            key = key
        
        else:
            raise ValueError("Invalid option. Please select either ‘Encryption’ or ‘Decryption’.")
        
        for text in texts:
            # If the word in plaintext is lower case
            if text.islower():
                shift = chr((ord(text) - ord('a') + key) % 26 + ord('a'))
                result += shift
            
            # If the word in plaintext is upper case
            elif text.isupper():
                shift = chr((ord(text) - ord('A') + key) % 26 + ord('A'))
                result += shift
            
            # If 'the word in plaintext is not string
            else:
                result += text
        
        return result
    
    def permutation_cipher(texts, key=None, mode = 'encryption'):
        # Raise error if empty plaintext.
        if not texts:
            raise ValueError("\nYou typed empty plaintext. Enter your plaintext.\n")
        
        default_key = [3, 0, 4, 1, 2]
        
        # If the key is the default, generalize randomly the same length as the texts
        if key == None:
            key = default_key

        if len(key) != 5:
            key = default_key

        key = functions.adjust_key(key, len(texts))
        
        result = ""

        if mode == 'encryption':
            for i in range(0, len(texts), 5):
                # slice the texts as 5 letter size
                block = texts[i:i+5]

                # If there are less than 5 letters in a block, add empty space
                if len(block) < 5:
                    block += ' ' * (5 - len(block))

                for j in key[:len(block)]:
                    result += block[j]
            
            
        
        elif mode == 'decryption':
            # Create a list to hold decrypted characters
            result_list = [''] * len(texts)
            for i in range(0, len(texts), 5):
                block = texts[i:i+5]

                for j, k in enumerate(key[:len(block)]):
                    # Prevent exceed index
                    if i + k < len(result_list) and j < len(block):
                        result_list[i + k] = block[j]
    

            result = ''.join(result_list).rstrip()
            result = result[:len(texts)]
        
        else:
            raise ValueError("Invalid option. Please select either ‘Encryption’ or ‘Decryption’.")
        
        return result
    
    # adjust the key length to the same length as the texts length
    def adjust_key (key, len_texts):
        if len(key) < len_texts:
            a = (len_texts // len(key)) + 1
            key = (key * a)[:len_texts]

        elif len(key) > len_texts:
            key = key[:len_texts]
        
        return key

    
    def simple_tranpos(texts, key, mode = 'encryption'):
        # Raise error if empty plaintext.
        if not texts:
            raise ValueError("\nYou typed empty plaintext. Enter your plaintext.\n")
        
        if mode == 'encryption':
            encryp_text = [''] * key

            for column in range(key):
                pointer = column
                while(pointer < len(texts)):
                    encryp_text[column] += texts[pointer]
                    pointer += key

            return ''.join(encryp_text)
        
        elif mode == 'decryption':
            columns = key
            rows = len(texts) // key
            shaded = len(texts) % key

            decryp_text = [''] * (rows + 1 if shaded > 0 else rows)
            column = 0
            row = 0

            for text in texts:
                decryp_text[row] += text
                row += 1
            
                # If reached last row or empty space, move to the next column
                if (row == rows and column >= shaded) or row == rows + 1:
                    column += 1
                    row = 0
            
            return ''.join(decryp_text)
        
        else:
            raise ValueError("Invalid option. Please select either ‘Encryption’ or ‘Decryption’.")
    
    def double_tranpos(texts, key1, key2, mode='encryption'):
        # Raise error if empty plaintext.
        if not texts:
            raise ValueError("\nYou typed empty plaintext. Enter your plaintext.\n")
        
        if mode == 'encryption':
            texts = functions.pad_text(texts, max(key1, key2))

            enc_tranpos1 = functions.simple_tranpos(texts, key1, mode)
            enc_tranpos2 = functions.simple_tranpos(enc_tranpos1, key2, mode)

            return enc_tranpos2
        
        elif mode == 'decryption':
            dec_tranpos1 = functions.simple_tranpos(texts, key2, mode)
            dec_tranpos2 = functions.simple_tranpos(dec_tranpos1, key1, mode)

            return functions.remove_pad(dec_tranpos2)
        
        else:
            raise ValueError("Invalid option. Please select either ‘Encryption’ or ‘Decryption’.")
    
    def pad_text(text, key):
        # Add space If the length of the key does not divide evenly
        padding_length = len(text) % key
        if padding_length != 0:
            padding_length = key - padding_length
            text += ' ' * padding_length
        return text

    def remove_pad(text):
        # Remove space
        return text.rstrip()
    
    def vigenere_cipher(texts, key, mode='encryption'):
        # Raise error if empty plaintext.
        if not texts:
            raise ValueError("\nYou typed empty plaintext. Enter your plaintext.\n")
        
        key = list(key)
        if len(texts) == len(key):
            key = key
        else:
            for i in range(len(texts) - len(key)):
                key.append(key[i % len(key)])
            key = "".join(key)
        
        result = []

        if mode == 'encryption':
            for i in range(len(texts)):
                text = texts[i]
                if text.islower():
                    encrypted_text = chr((ord(text) + ord(key[i]) - 2 * ord('a')) % 26 + ord('a'))
                
                elif text.isupper():
                    encrypted_text = chr((ord(text) + ord(key[i]) - 2 * ord('A')) % 26 + ord('A'))
                
                else:
                    encrypted_text = text
                
                result.append(encrypted_text)
            
            results = ''.join(result)
        
        elif mode == 'decryption':
            for i in range(len(texts)):
                text = texts[i]
                if text.islower():
                    decrypted_text = chr((ord(text) - ord(key[i]) + 26) % 26 + ord('a'))

                elif text.isupper():
                    decrypted_text = chr((ord(text) - ord(key[i]) + 26) % 26 + ord('A'))
                
                else:
                    decrypted_text = text
                
                result.append(decrypted_text)
            
            results = ''.join(result)
        
        else:
            raise ValueError("Invalid option. Please select either ‘Encryption’ or ‘Decryption’.")

        return results

    def aes(texts, key=None, iv=None, mode='encryption', encryption_mode='ecb'):
        # Raise error if empty plaintext.
        if not texts:
            raise ValueError("\nYou typed empty plaintext. Enter your plaintext.\n")
        
        if key is None:
            key = get_random_bytes(16)
        
        # Raise error if key length is not 16
        if len(key) != 16:
            raise ValueError("Key length must be 16 bytes for AES.")
        
        # Create Initial Vector for CBC, OFB if there is not initial vector
        if encryption_mode in ['cbc', 'ofb']:
            if iv is None:
                iv = get_random_bytes(16)
        
        if encryption_mode == 'ecb':
            cipher = AES.new(key, AES.MODE_ECB)
        
        elif encryption_mode == 'cbc':
            cipher = AES.new(key, AES.MODE_CBC, iv)
        
        elif encryption_mode == 'ofb':
            cipher = AES.new(key, AES.MODE_OFB, iv)
        
        else:
            raise ValueError("Invalid Encryption Mode. Please select either 'ECB', 'CBC', or 'OFB'.")
        
        if mode == 'encryption':
            text = pad(texts.encode(), AES.block_size)
            ciphertext = cipher.encrypt(text)
            return ciphertext, key, iv
        
        elif mode == 'decryption':
            text = cipher.decrypt(texts)
            plaintext = unpad(text, AES.block_size).decode()
            return plaintext, key, iv
        
        else:
            raise ValueError("Invalid option. Please select either ‘Encryption’ or ‘Decryption’.")
    
    def des(texts, key=None, iv=None, mode='encryption', encryption_mode='ecb'):
        # Raise error if empty plaintext.
        if not texts:
            raise ValueError("\nYou typed empty plaintext. Enter your plaintext.\n")
        
        if key is None:
            key = get_random_bytes(8)
        
        # Raise error if key length is not 8
        if len(key) != 8:
            raise ValueError("Key length must be 16 bytes for DES.")
        
        # Create Initial Vector for CBC, OFB if there is not initial vector
        if encryption_mode in ['cbc', 'ofb']:
            if iv is None:
                iv = get_random_bytes(8)
        
        if encryption_mode == 'ecb':
            cipher = DES.new(key, DES.MODE_ECB)
        
        elif encryption_mode == 'cbc':
            cipher = DES.new(key, DES.MODE_CBC, iv)
        
        elif encryption_mode == 'ofb':
            cipher = DES.new(key, DES.MODE_OFB, iv)
        
        else:
            raise ValueError("Invalid Encryption Mode. Please select either 'ECB', 'CBC', or 'OFB'.")
        
        if mode == 'encryption':
            text = pad(texts.encode(), DES.block_size)
            ciphertext = cipher.encrypt(text)
            return ciphertext, key, iv
        
        elif mode == 'decryption':
            text = cipher.decrypt(texts)
            plaintext = unpad(text, DES.block_size).decode()
            return plaintext, key, iv
        
        else:
            raise ValueError("Invalid option. Please select either ‘Encryption’ or ‘Decryption’.")
    
    def des3(texts, key=None, iv=None, mode='encryption', encryption_mode='ecb'):
        # Raise error if empty plaintext.
        if not texts:
            raise ValueError("\nYou typed empty plaintext. Enter your plaintext.\n")
        
        if not key:
            key = get_random_bytes(16)
        
        if len(key) not in [16, 24]:
            raise ValueError("Key length must be either 16 or 24 bytes for 3DES.")
        
        if encryption_mode in ['cbc', 'ofb']:
            if not iv:
                iv = get_random_bytes(8)
        
        if encryption_mode == 'ecb':
            cipher = DES3.new(key, DES3.MODE_ECB)
        
        elif encryption_mode == 'cbc':
            cipher = DES3.new(key, DES3.MODE_CBC, iv)
        
        elif encryption_mode == 'ofb':
            cipher = DES3.new(key, DES3.MODE_OFB, iv)
        
        else:
            raise ValueError("Invalid Encryption Mode. Please select either 'ECB', 'CBC', or 'OFB'.")
        
        if mode == 'encryption':
            text = pad(texts.encode(), DES3.block_size)
            ciphertext = cipher.encrypt(text)
            return ciphertext, key, iv
        
        elif mode == 'decryption':
            text = cipher.decrypt(texts)
            plaintext = unpad(text, DES3.block_size).decode()
            return plaintext, key, iv
        
        else:
            raise ValueError("Invalid option. Please select either ‘Encryption’ or ‘Decryption’.")
