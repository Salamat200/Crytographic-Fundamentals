# Step 1: Create plaintext.txt and write the message
with open("plaintext.txt", "w", encoding="utf-8") as file:
    file.write("Pay $1000 to Bob")

# Step 2: Read and print the plaintext file
with open("plaintext.txt", "r", encoding="utf-8") as file:
    plaintext = file.read()
print("Plaintext from file:", plaintext)

# Step 3: Convert plaintext to hex
plaintext_hex = plaintext.encode("utf-8").hex()

# Step 4: Save the hex encoding to plaintext_hex.txt
with open("plaintext_hex.txt", "w") as file:
    file.write(plaintext_hex)

# Step 5: Read and print the hex file
with open("plaintext_hex.txt", "r") as file:
    hex_content = file.read()
print("Hex representation:", hex_content)

# Step 6: Convert hex back to ASCII
decoded_text = bytes.fromhex(hex_content).decode("utf-8")
print("Decoded text:", decoded_text)
