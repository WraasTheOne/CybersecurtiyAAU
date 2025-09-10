def hex_to_bytes(hex_string):
    """Converts a hexadecimal string to a bytes object."""
    return bytes.fromhex(hex_string)

def xor_bytes(a, b):
    """Performs a bitwise XOR on two bytes objects."""
    # zip() stops when the shorter of the two iterables is exhausted.
    return bytes(x ^ y for x, y in zip(a, b))

# The provided messages as hexadecimal strings
msg1_hex = "d55860b8bd9fb5da012f7d153627e5f0e28dd3536b5648eaa33d563955c59b7a984f14cd0e3f8c7488917f5ab83fbea8ad79c01ab4e2b957097e6fa5eea6de302e82db2b86fbd55ae8c2f8944eb210699ae5162968e973ec94c283c84436dfaaa732c14f2f98963885ae9a49dd64b79daba95b1c95081bac0223abdd4e10eada3cdceae39c0538550b03f2f9fbd0c997aca6e199b5e9cba354248757db"
msg2_hex = "d1527eb1bf9fb1d3523c625c3726edbeb0e4804d700345e3e6251372538a8166dd5805c4166a873b9cd5770aa229beb3a66acc5face3a85b596c79b2b9adc3746b82dd78ccd3e439dfeed7a16d94172ed4c7133e6ead72ea85c298d91c2e9ea5ad33d70e2d899615caa3981bcb21b498a5a95d1c8d0b07fd002be9913b06af9f1edaf5a6904151481118f6b4bdc9ded9b3a2fedcf3f1ddab536d865686e03eddc7000c5317e332f6f8ef2c1d3128cc161f311481ce1d272b0bcaeb88438aef5e89ccbe4ec7c42f68554acd5b5714e27ca39b5f55e9b9a20f658961c654f2978794e10132fb167ba40ea2c8cb04b77d76bd104caaf68f8d3fadfba160bd4efdf6794ff6659b93063b8e1ef128d73ae3ac1daa1eaf49f56a8dd377f96292eef14c64b14e05878b69d5067894e06d2b07c9d539e485c759b21467952f6305b2224e75b9d76c92435549446bd74d916857796a9786ff71725c00f8bab66532dd9cb93338b48f68d540fc76d9b09083b926fb23243e44907f7ca84f82003a2516e5fff0a3fa9198833af58a488da752c46edc2001910b1b0ed6de7a68ce6e87159db284b31b6c7864843ff654e9ab49276e4a481bb1beec6dfc708fe2fd444a"

# Convert hex strings to byte objects
c1 = hex_to_bytes(msg1_hex)
c2 = hex_to_bytes(msg2_hex)

# Bob's known plaintext greeting (the "crib")
p1_known = b"Hello my friend!"

# **THE FIX:** Assume the rest of plaintext 1 is padded with spaces to match the
# length of the first ciphertext.
p1_guess = p1_known + b' ' * (len(c1) - len(p1_known))

# Recover the keystream using the full guessed plaintext.
# The keystream will be the same length as c1 (the shorter ciphertext).
keystream = xor_bytes(c1, p1_guess)

# Use this keystream to decrypt the second ciphertext.
# The result will be the same length as the recovered keystream.
p2_decrypted = xor_bytes(c2, keystream)

print("Decrypted Message 2:")
print(p2_decrypted.decode('utf-8', 'ignore'))