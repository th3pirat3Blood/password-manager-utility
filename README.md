# Password Manager Utility
---

## Description
This project is aimed at providing a tool for safe password storage and generation.
The tool supports both command line interface and GUI mode.

## Table of Contents

* [Command line usage]()

* [GUI tool usage]()

## Command line usage

### Help

For checking all the command line arguments check help message using:

```bash
python3 password_manager.py --help
```
```bash
usage: password_manager_cmd.py [-h] [-g] [-l NUMBER] [--alpha]
                               [--alpha-decimal] [--all] [-e] [-d] [-k KEY]
                               [-kf FILE] [-t TEXT] [-f FILE] [-o FILE]

Password manager is a command line utility for managing passwords

options:
  -h, --help            show this help message and exit
  -g, --gen             generate a new password
  -l NUMBER, --length NUMBER
                        specify length of password to be generated
  --alpha               generate passwords using only alphabets
  --alpha-decimal       generate passwords using only alpha numerals
  --all                 generate passwords using alphanumerical and special
                        characters
  -e, --enc             encrypt a file
  -d, --dec             decrypt a file
  -k KEY, --key KEY     key to be used for encryption/decryption
  -kf FILE, --key-file FILE
                        use key from FILE for encryption/decryption
  -t TEXT, --text TEXT  text to encrypt/decrypt
  -f FILE, --file FILE  file to encrypt/decrypt
  -o FILE, --out FILE   output file to store decrypted/encrypted file
```

### Generating password

For generating new password

```bash
python3 password_manager.py -g
```

For generating new password of length 12 using alphabets and numerals
```bash
python3 password_manager_cmd.py -g --length 12 --alpha-decimal
```

For generating new password of length 12 using alphabets, decimals and special characters

```bash
python3 password_manager_cmd.py -g --length 12 --all
```

### Encrypting

For encrypting text without a key

```bash
python3 password_manager_cmd.py -e -t "some_text_here"
```

For encrypting text with a key

```bash
python3 password_manager_cmd.py -e -k "some_key" -t "some_text"
```

For encrypting text with a key located inside a file

```bash
python3 password_manager_cmd.py -e -kf "path_to_key_file" -t "some_text" 
```

For encrypting a file with a key located inside a file with output to a user defined file

```bash
python3 password_manager_cmd.py -e -kf "path_to_key_file" -f "path_to_file_to_encrypt" -o "path_for_encrypted_file_output"
```

