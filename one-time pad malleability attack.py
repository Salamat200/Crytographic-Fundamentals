# Step 1: Read original ciphertext from "ciphertext.txt"
with open("ciphertext.txt", "r") as file:
    ciphertext_hex = file.read()

# Step 2: Copy ciphertext to "ciphertext1.txt"
with open("ciphertext1.txt", "w") as file:
    file.write(ciphertext_hex)

# Step 3: Modify the ciphertext to change "$1000" to "$3000"
# Find the position of '1' in "1000" in ASCII hex (0x31)
original_plaintext = "Pay $1000 to Bob"
modified_plaintext = "Pay $3000 to Bob"

# Locate the byte position of '1' in the original text
pos = original_plaintext.index('1')  # Find index of '1' in the string
byte_pos = pos * 2  # Each character takes 2 hex digits

# Convert ciphertext to a list of hex pairs for modification
ciphertext_bytes = bytearray.fromhex(ciphertext_hex)

# XOR the corresponding ciphertext byte with 0x02 (to change '1' (0x31) to '3' (0x33))
ciphertext_bytes[pos] ^= 0x02  # Modify the correct byte

# Convert back to hex
modified_ciphertext_hex = ciphertext_bytes.hex()

# Save modified ciphertext to "ciphertext1.txt"
with open("ciphertext1.txt", "w") as file:
    file.write(modified_ciphertext_hex)

# Step 4: Read and print ciphertext files
print("Original Ciphertext (Hex):", ciphertext_hex)
print("Modified Ciphertext (Hex):", modified_ciphertext_hex)

# Step 5: Read key from "key.txt"
with open("key.txt", "r") as file:
    key_hex = file.read()

key_bytes = bytes.fromhex(key_hex)

# Step 6: Decrypt modified ciphertext
modified_ciphertext_bytes = bytes.fromhex(modified_ciphertext_hex)
decrypted_bytes = bytes([c ^ k for c, k in zip(modified_ciphertext_bytes, key_bytes)])
decrypted_text = decrypted_bytes.decode("utf-8")
decrypted_hex = decrypted_bytes.hex()

# Step 7: Print the modified decrypted plaintext
print("Modified Decrypted Plaintext (Text):", decrypted_text)
print("Modified Decrypted Plaintext (Hex):", decrypted_hex)

