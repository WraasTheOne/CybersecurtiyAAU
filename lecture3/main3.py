def hex_to_bytes(hex_string):
    """Converts a hexadecimal string to a bytes object."""
    return bytes.fromhex(hex_string)

def xor_bytes(a, b):
    """
    Performs a bitwise XOR on two bytes objects.
    If the keys are of different lengths, it repeats the shorter one.
    """
    # Pad the shorter bytes to match the longer one for XOR
    if len(a) > len(b):
        b = (b * (len(a) // len(b) + 1))[:len(a)]
    elif len(b) > len(a):
        a = (a * (len(b) // len(a) + 1))[:len(b)]

    return bytes(x ^ y for x, y in zip(a, b))

# The provided ciphertext in hexadecimal format
ciphertext_hex = "0e0b213f26041e480b26217f27342e175d0e070a3c5b103e2526217f27342e175d0e077e263451150104"

# The known plaintext prefix, which is used to recover the key.
# We've extended it to 'crypto{1' as manual analysis of the ciphertext
# suggests the key is 8 characters long, not 7.
known_plaintext = b"crypto{1"

# 1. Convert the ciphertext from hex to a byte string
ciphertext_bytes = hex_to_bytes(ciphertext_hex)

# 2. XOR the beginning of the ciphertext with the known plaintext.
# This recovers the key, which is repeated throughout the message.
key_part = xor_bytes(ciphertext_bytes[:len(known_plaintext)], known_plaintext)

# 3. Use the recovered key to decrypt the entire ciphertext.
# The xor_bytes function will automatically repeat the key as needed.
decrypted_flag_bytes = xor_bytes(ciphertext_bytes, key_part)

# 4. Decode the result into an ASCII string and print it
decrypted_flag = decrypted_flag_bytes.decode('ascii')

print(f"The XOR key is: {key_part.hex()}")
print(f"The full flag is: {decrypted_flag}")
