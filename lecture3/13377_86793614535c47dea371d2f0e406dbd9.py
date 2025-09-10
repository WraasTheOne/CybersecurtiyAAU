#!/usr/bin/env python3

import json
import base64
import codecs
import socket

# Recreate bytes_to_long and long_to_bytes using built-in Python methods
def bytes_to_long(b):
    return int.from_bytes(b, 'big')

def long_to_bytes(n):
    length = (n.bit_length() + 7) // 8
    return n.to_bytes(length, 'big')

def solve_challenge():
    # Connect to the remote server
    HOST, PORT = "socket.cryptohack.org", 13377
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.connect((HOST, PORT))
            
            # Loop for 101 rounds (100 challenges + 1 for the flag)
            for i in range(101):
                # Receive data from the server
                data_json = b''
                while True:
                    chunk = sock.recv(1024)
                    data_json += chunk
                    if b'}\n' in chunk:
                        break

                data = json.loads(data_json.decode('utf-8'))

                if 'flag' in data:
                    print(f"Flag received: {data['flag']}")
                    return

                encoding_type = data['type']
                encoded_value = data['encoded']

                decoded_value = ""

                if encoding_type == "base64":
                    decoded_value = base64.b64decode(encoded_value).decode('utf-8')
                elif encoding_type == "hex":
                    decoded_value = bytes.fromhex(encoded_value).decode('utf-8')
                elif encoding_type == "rot13":
                    decoded_value = codecs.decode(encoded_value, 'rot_13')
                elif encoding_type == "bigint":
                    decoded_value = long_to_bytes(int(encoded_value, 16)).decode('utf-8')
                elif encoding_type == "utf-8":
                    decoded_value = "".join([chr(b) for b in encoded_value])

                # Prepare the response and send it
                response = {"decoded": decoded_value}
                sock.sendall((json.dumps(response) + '\n').encode('utf-8'))

                print(f"Stage {i+1}: Solved {encoding_type} -> {decoded_value}")
                
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    solve_challenge()