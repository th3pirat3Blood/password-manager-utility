# Password Manager Utility
---

## Description

This project is aimed at providing a tool for safe password storage and generation.
The tool supports both command line interface and GUI mode.

## Usage

### Command line:

For checking all the command line arguments check help message using:
```bash
python3 password_manager.py --help
```

For generating new password
```bash
python3 password_manager.py -g
```

For generating new password of length 12 using alphabets and numerals
```bash
python3 password_manager_cmd.py -g --length 12 --a0
```

For saving password to the list of old passwords
```bash
python3 password_manaager.py -s <password> <password_filename.enc> <key>
```

For getting all the passwords from the list
```bash
python3 password_manager.py -d -a <password_filename.enc> <key>
```

For getting single password from list
```bash
python3 password_manager.py -d -u <username/email_id> <password_filename.enc> <key>
```
