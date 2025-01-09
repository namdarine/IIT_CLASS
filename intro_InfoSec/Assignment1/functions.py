'''
---------------
 CS 458       |
 Fall 2024    |
 Nam Gyu Lee  |
 Assignment 1 |
 Functions    |
---------------
'''

# Import libraries
import nltk
from nltk.corpus import words
import re

nltk.download('words')

class function:
    def encryption(plaintext, key):
        # Raise error if empty plaintext.
        if not plaintext:
            raise ValueError("\nYou typed empty plaintext. Enter your plaintext.\n")
        
        result = ""
        
        for text in plaintext:
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
    
    def decryption(ciphertext, key):
        if not ciphertext:
            raise ValueError("\nYou typed empty ciphertext. Enter your ciphertext.\n")
        
        result = ""
        
        for text in ciphertext:
            # If the word in ciphertext is lower case
            if text.islower():
                shift = chr((ord(text) - ord('a') - key) % 26 + ord('a'))
                result += shift
            
            # If the word in ciphertext is upper case
            elif text.isupper():
                shift = chr((ord(text) - ord('A') - key) % 26 + ord('A'))
                result += shift
            
            # If the word in ciphertext is not string
            else:
                result += text
        
        return result
    
    # The following is just for fun
    def clean_text(text):
        return re.sub(r'[^\w\s]', '', text).lower()
    
    def check(plaintext, key):
        result = ""
        word_list = set(words.words())
        
        cleaned_plaintext = function.clean_text(plaintext)
        plaintext_words = cleaned_plaintext.split()
        
        for word in plaintext_words:
            if word in word_list:
                result += word + " "
         
        result = result.strip()
        
        if cleaned_plaintext == function.clean_text(result):
            return key
        else:
            return None
                    
        
        
        
            
    