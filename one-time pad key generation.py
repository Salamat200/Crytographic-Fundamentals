import os

# Step 1: Define the key length (same as plaintext length)
plaintext = "Pay $1000 to Bob"
key_length = len(plaintext)  # Each ASCII character = 1 byte

# Step 2: Generate a random key (secure random bytes)
key = os.urandom(key_length)  # Generates cryptographically secure random bytes

# Step 3: Convert key to hex
key_hex = key.hex()

# Step 4: Save the key to "key.txt"
with open("key.txt", "w") as file:
    file.write(key_hex)

# Step 5: Read and print the key from file
with open("key.txt", "r") as file:
    key_content = file.read()
print("Generated One-Time Pad Key (Hex):", key_content)
