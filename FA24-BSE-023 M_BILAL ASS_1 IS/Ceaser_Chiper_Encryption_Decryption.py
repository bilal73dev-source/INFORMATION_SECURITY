# Caesar Cipher Implementation
# Course: Information Security
# Lab Assignment 1

def caesar_encrypt(text, shift):#Function defination
    encrypted_text = ""#intializing with empty string for avoiding garbage vlaue
    
    for char in text:#char is a variable here that takes one character from the string that is stored in the parameter "text"

        # Check if character is uppercase
        if char.isupper():
            encrypted_text += chr((ord(char) - ord('A') + shift) % 26 + ord('A'))#ord change character in "char" into ASCII CODE and than chr will change back the the ASCII CODE into character
        
        # Check if character is lowercase
        elif char.islower():
            encrypted_text += chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
        
        # Keep spaces and special characters unchanged
        else:
            encrypted_text += char
            
    return encrypted_text


def caesar_decrypt(ciphertext, shift):
    # Decryption is encryption with negative shift
    return caesar_encrypt(ciphertext, -shift)


# Main Program
if __name__ == "__main__":
    message = input("Enter your message: ")
    shift_value = int(input("Enter shift value: "))
    encrypted = caesar_encrypt(message, shift_value)#passing arguments to parameters
    print("Encrypted Text:", encrypted)
    decrypted = caesar_decrypt(encrypted, shift_value)#passing arguments to parameters
    print("Decrypted Text:", decrypted)