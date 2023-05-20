# Zip Decrypter
# Author - Cyber Penetrate

#These are import statements in Python that import necessary modules for the script to run.
import sys
import time
import zipfile
import argparse
import threading

"""
This Python function attempts to extract a password-protected zip file using a list of passwords
provided as a text file.
"""
def main():
    try_count = 0
    parser = argparse.ArgumentParser()
    parser.add_argument('-f', help="Name of Zip File")
    parser.add_argument('-p', help="Password List")
    args = parser.parse_args()

    if not args.f or not args.p:
        print("Usage: python ZipDecryptor.py -f <name_of_zipfile.zip> -p <name_of_password_list.txt>")
        sys.exit(1)

    zip_file = zipfile.ZipFile(args.f)
    password_list = open(args.p, 'r')

    start_time = time.time()
    print("[+]Please Wait While Extracting...")

    for password in password_list.readlines():
        try_count += 1
        password = password.strip()

        zip_process = threading.Thread(target=extract_zip, args=(zip_file, password))
        zip_process.start()

    for thread in threading.enumerate():
        if thread != threading.main_thread():
            thread.join()

    print("[+]Tried:",try_count)
    end_time = time.time()
    print("[+]Duration:",end_time - start_time)

"""
This function attempts to extract the contents of a zip file using a given password and prints the
password if successful.

:param zip_file: a zip file object that needs to be extracted
:param password: The password parameter is a string that represents the password that will be used
to extract the contents of a zip file. The password is encoded using the encode() method to convert
it into bytes before it is passed to the extractall() method
"""
def extract_zip(zip_file, password):
    try:
        zip_file.extractall(pwd=password.encode())
        print("[+]Password Found:",password)
        sys.exit(0)
    except Exception:
        pass

if __name__ == '__main__':
    main()