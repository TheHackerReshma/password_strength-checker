# Password Strength Checker

A Python-based tool to evaluate the strength of passwords based on various security criteria.

## Features
- ✅ Checks password length
- ✅ Evaluates uppercase, lowercase, numbers, and special characters
- ✅ Detects common weak passwords
- ✅ Provides a strength score and recommendations

## Installation
### Prerequisites
Ensure you have Python 3.x installed. If not, download it from [Python.org](https://www.python.org/).

### Install Dependencies
This script requires no external dependencies. However, to enhance functionality, you may install `getpass` for secure password entry:
```bash
pip install getpass
```

## Usage
### Run the Script
```bash
python password_checker.py
```
or  
```bash
python3 password_checker.py
```

### Enter a Password
The script will prompt you to enter a password:
```
Enter your password: ********
```

## Example Output
```
Password Strength: Weak
Issues:
- Password is too short (Minimum 8 characters required)
- Missing special characters
- Consider using a mix of uppercase and lowercase letters
```
If the password is strong:
```
Password Strength: Strong ✅
Your password meets all security requirements!
```

## Strength Criteria
- **Weak:** Less than 8 characters, no special characters, or a common password.
- **Moderate:** At least 8 characters with a mix of letters and numbers.
- **Strong:** 12+ characters, including uppercase, lowercase, numbers, and special symbols.

## How It Works
1. The script prompts the user to enter a password.
2. It evaluates the password based on:
   - Length
   - Character diversity (uppercase, lowercase, numbers, symbols)
   - Common weak passwords
3. Provides feedback and improvement suggestions.

## Disclaimer
- This tool is for **personal security awareness**.
- It **does not store passwords**.
- Always use a **password manager** for better security.

## License
This project is licensed under the **MIT License**. Feel free to modify and use it!

## Contributing
Want to improve this tool? Fork the repo and submit a PR!

