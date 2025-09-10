import base64
import pwn

arr = [99, 114, 121, 112, 116, 111, 123, 65, 83, 67, 73, 73, 95, 112, 114, 49, 110, 116, 52, 98, 108, 51, 125]

def xorsolve():
    
    s = "label"
    x = 13
    
    result_chars = []
    for char in s:
        # Get Unicode integer value of the character
        char_int = ord(char)
        # XOR with the given integer
        xored_int = char_int ^ x
        # Convert back to character
        result_chars.append(chr(xored_int))
    res = ''.join(result_chars)
    print(res)

def keyXors():
    k1 = 0xa6c8b6733c9b22de7bc0253266a3867df55acde8635e19c73313
    k1_2 = 0x37dcb292030faa90d07eec17e3b1c6d8daf94c35d4c9191a5e1e


    k2 = k1 ^ k1_2
    
    k2_3 = 0xc1545756687e7573db23aa1c3452a098b71a7fbf0fddddde5fc1


    k3 = k2_3 ^ k2
    
    flag = 0x04ee9855208a2cd59091d04767ae47963170d1660df7f56f5faf


    final_flag_value = flag ^ k1 ^ k2 ^ k3
    

    final_flag_hex = hex(final_flag_value)
    
    try:
        # Determine the number of bytes needed to represent the integer.
        num_bytes = (final_flag_value.bit_length() + 7) // 8

        # Convert the integer to a byte string (big-endian).
        flag_bytes = final_flag_value.to_bytes(num_bytes, 'big')

        # Decode the byte string as ASCII to get the final string.
        flag_ascii = flag_bytes.decode('ascii')
        
        print(f"The final flag is: {flag_ascii}")
    except UnicodeDecodeError:
        print("Error: The resulting bytes could not be decoded as ASCII.")
    

   



def Ascii():
    result = ""
    for i in arr:
        result += chr(i)
    print(result)
    
def Hex():
    a = '63727970746f7b596f755f77696c6c5f62655f776f726b696e675f776974685f6865785f737472696e67735f615f6c6f747d'
    # Convert hex string to a bytes object
    decoded_bytes = bytes.fromhex(a)
    # Decode the bytes to a UTF-8 string
    result = decoded_bytes.decode('utf-8')
    print(result)

def base64de():
    # This is a hexadecimal string
    hex_string = '72bca9b68fc16ac7beeb8f849dca1d8a783e8acf9679bf9269f7bf'
    
    # Step 1: Decode the hex string into bytes
    decoded_bytes = bytes.fromhex(hex_string)
    
    # Step 2: Encode the bytes into Base64
    base64_encoded = base64.b64encode(decoded_bytes)
    
    print(base64_encoded)


def byteschall():
    base10str = 11515195063862318899931685488813747395775516287289682636499965282714637259206269
    

    hex_string = hex(base10str)[2:]
    

    if len(hex_string) % 2 != 0:
        hex_string = '0' + hex_string
    

    hex_bytes = bytes.fromhex(hex_string)
    

    asciichar = hex_bytes.decode('ascii')
    
    print(asciichar)

def main():
    Ascii()
    Hex()
    base64de()
    byteschall()
    xorsolve()
    keyXors()
    

if __name__ == "__main__":
    main()