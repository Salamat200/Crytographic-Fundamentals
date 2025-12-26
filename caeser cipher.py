# Caesar Cipher Implementation

# Function for modular addition (Encryption)
def m_add(a, b):
    return (a + b) % 26

# Function for modular subtraction (Decryption)
def m_sub(a, b):
    return (a - b) % 26

# Function to encrypt a plaintext message
def caesar_encrypt(plaintext, key):
    encrypted_text = ""
    for char in plaintext:
        if char.isalpha():  # Only process letters
            num = ord(char.upper()) - ord('A')  # Convert letter to number
            encrypted_num = m_add(num, key)  # Apply modular addition
            encrypted_text += chr(encrypted_num + ord('A'))  # Convert back to letter
        else:
            encrypted_text += char  # Keep non-alphabet characters unchanged
    return encrypted_text

# Function to decrypt a ciphertext message
def caesar_decrypt(ciphertext, key):
    decrypted_text = ""
    for char in ciphertext:
        if char.isalpha():
            num = ord(char.upper()) - ord('A')  # Convert letter to number
            decrypted_num = m_sub(num, key)  # Apply modular subtraction
            decrypted_text += chr(decrypted_num + ord('A'))  # Convert back to letter
        else:
            decrypted_text += char
    return decrypted_text

# Test the implementation with the word "BACK" and different keys
plaintext = "BACK"
keys = [3, 7, 10]

for key in keys:
    encrypted = caesar_encrypt(plaintext, key)
    decrypted = caesar_decrypt(encrypted, key)
    print(f"Key: {key}")
    print(f"Encrypted: {encrypted}")
    print(f"Decrypted: {decrypted}")
    print("-" * 20)  # Separator for clarity

