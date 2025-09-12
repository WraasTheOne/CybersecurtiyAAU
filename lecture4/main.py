# This script is for educational purposes only, to be used in ethical hacking
# competitions (CTFs) with explicit permission.

import zipfile
import threading
import sys
import time
import string
import itertools
import queue

# A queue to hold the passwords to be checked by worker threads.
password_queue = queue.Queue()

# A counter to track the number of passwords checked
checked_passwords = 0
found = threading.Event()
lock = threading.Lock()

def extract_zip(zip_file, password, result_list, thread_id):
    """
    Attempts to extract the zip file with a given password.
    
    Args:
        zip_file (zipfile.ZipFile): The zip file object.
        password (str): The password to try.
        result_list (list): A list to store the successful password.
        thread_id (int): Identifier for the current thread.
    """
    global checked_passwords
    global found

    # If another thread has already found the password, exit this thread.
    if found.is_set():
        return

    try:
        # Attempt to extract the first file with the password.
        zip_file.extractall(pwd=password.encode('utf-8'))
        
        # If extraction is successful, this thread has found the password.
        print(f"\n[+] Password found by thread {thread_id}: {password}")
        result_list.append(password)
        found.set()  # Signal other threads to stop.
    except (zipfile.BadZipFile, RuntimeError, Exception):
        # A failed attempt; the password was incorrect.
        pass

    with lock:
        checked_passwords += 1
        # Optional: Print progress every 1000 attempts.
        if checked_passwords % 100000 == 0:
           print(f"[*] Passwords checked: {checked_passwords}", end='\r')


def worker(zip_file, result_list, thread_id):
    """
    Worker function for each thread to check passwords from the queue.
    """
    while not found.is_set():
        try:
            password = password_queue.get(timeout=1)
            extract_zip(zip_file, password, result_list, thread_id)
            password_queue.task_done()
        except queue.Empty:
            # The queue is empty, and we can exit the worker thread.
            break

def main(zip_filename):
    """
    Main function to orchestrate the brute-force attack.
    
    Args:
        zip_filename (str): Path to the zip file.
    """
    global checked_passwords
    global found

    try:
        zip_file = zipfile.ZipFile(zip_filename)
        print(f"[*] Loaded zip file: {zip_filename}")
    except zipfile.BadZipFile:
        print(f"[-] Error: '{zip_filename}' is not a valid zip file.")
        sys.exit(1)
    except FileNotFoundError:
        print(f"[-] Error: Zip file '{zip_filename}' not found.")
        sys.exit(1)

    # Set up multithreading.
    thread_count = 1000 # You can adjust this for more or less threads
    threads = []
    result_list = []
    
    print(f"[*] Starting brute-force with {thread_count} threads...")
    start_time = time.time()

    # Create and start worker threads.
    for i in range(thread_count):
        t = threading.Thread(target=worker, args=(zip_file, result_list, i + 1))
        threads.append(t)
        t.start()

    # Generate passwords and add them to the queue.
    print("[*] Generating passwords...")
    chars = string.ascii_letters
    for length in range(1, 10): # You can adjust the max password length.
        if found.is_set():
            break
        print(f"[*] Trying passwords of length {length}...")
        
        # Use itertools.product to generate combinations of characters.
        for combination in itertools.product(chars, repeat=length):
            if found.is_set():
                break
            password = "".join(combination)
            password_queue.put(password)

    # Wait for all passwords to be checked.
    password_queue.join()
    
    # Wait for all threads to finish.
    for t in threads:
        t.join()
        
    end_time = time.time()

    if found.is_set():
        print(f"\n[+] Brute-force complete. Password found: {result_list[0]}")
    else:
        print("\n[-] Password not found in the generated character set.")
    
    print(f"[*] Total time taken: {end_time - start_time:.2f} seconds.")
    print(f"[*] Passwords checked: {checked_passwords}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python zip_bruteforce.py <zip_file>")
        sys.exit(1)

    zip_file_arg = sys.argv[1]
    main(zip_file_arg)
