import os

# Step 1: Read plaintext from "plaintext.txt"
with open("plaintext.txt", "r", encoding="utf-8") as file:
    plaintext = file.read()

# Print plaintext as text and hex
print("Plaintext (Text):", plaintext)
plaintext_hex = plaintext.encode("utf-8").hex()
print("Plaintext (Hex):", plaintext_hex)

# Step 2: Read key from "key.txt"
with open("key.txt", "r") as file:
    key_hex = file.read()

# Convert key back to bytes
key = bytes.fromhex(key_hex)

# Print key in hex
print("Key (Hex):", key_hex)

# Step 3: Compute ciphertext (OTP encryption)
plaintext_bytes = plaintext.encode("utf-8")  # Convert plaintext to bytes
ciphertext = bytes([p ^ k for p, k in zip(plaintext_bytes, key)])  # XOR operation

# Convert ciphertext to hex
ciphertext_hex = ciphertext.hex()
print("Ciphertext (Hex):", ciphertext_hex)

# Step 4: Save ciphertext to "ciphertext.txt"
with open("ciphertext.txt", "w") as file:
    file.write(ciphertext_hex)

# Step 5: Decrypt ciphertext (OTP decryption)
ciphertext_bytes = bytes.fromhex(ciphertext_hex)  # Convert hex back to bytes
decrypted_bytes = bytes([c ^ k for c, k in zip(ciphertext_bytes, key)])  # XOR operation

# Convert decrypted bytes back to text
decrypted_text = decrypted_bytes.decode("utf-8")

# Convert decrypted text to hex
decrypted_hex = decrypted_bytes.hex()

# Print decrypted plaintext as text and hex
print("Decrypted Plaintext (Text):", decrypted_text)
print("Decrypted Plaintext (Hex):", decrypted_hex)

# Step 6: Save decrypted plaintext to "plaintext_dec.txt"
with open("plaintext_dec.txt", "w", encoding="utf-8") as file:
    file.write(decrypted_text)
