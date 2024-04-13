# File Encryption:
# Write a Python program that takes a text file (input.txt) as input, encrypts its contents using a simple encryption algorithm (e.g., Caesar cipher or substitution cipher), and saves the encrypted text to another file (output.txt). Provide options for the user to specify the encryption key and the output file name.

def encrypt(text, key):
    """Encrypts the given text using a Caesar cipher with the specified key."""
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            # Shift the character by the key value
            shifted_char = chr((ord(char) - ord('a') + key) % 26 + ord('a')) if char.islower() else \
                           chr((ord(char) - ord('A') + key) % 26 + ord('A'))
            encrypted_text += shifted_char
        else:
            encrypted_text += char
    return encrypted_text


def enrypt_file(fileName, outfileName, key):
    with open(fileName, 'r') as f:
        text = f.read()
        encrypted_output = encrypt(text, key)

    with open(outfileName, 'w') as f:
        f.write(encrypted_output)


enrypt_file('q1.txt', 'output.txt', 3)


