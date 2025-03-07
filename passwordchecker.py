import re

# List of common dictionary words (you can expand this list)
COMMON_WORDS = ["password", "123456", "qwerty", "admin", "letmein", "welcome", "monkey", "sunshine", "password1"]

def is_common_word(password):
    """Check if the password is a common dictionary word."""
    return password.lower() in COMMON_WORDS

def evaluate_password_strength(password):
    """Evaluate the strength of the password based on the given rules."""
    feedback = []

    # Rule 1: Must be at least 12 characters long
    if len(password) < 12:
        feedback.append("Password must be at least 12 characters long.")
    
    # Rule 2: Must include at least one uppercase letter
    if not re.search(r'[A-Z]', password):
        feedback.append("Password must include at least one uppercase letter.")
    
    # Rule 3: Must include at least one lowercase letter
    if not re.search(r'[a-z]', password):
        feedback.append("Password must include at least one lowercase letter.")
    
    # Rule 4: Must include at least one number
    if not re.search(r'[0-9]', password):
        feedback.append("Password must include at least one number.")
    
    # Rule 5: Must include at least one special character (!@#$%^&*)
    if not re.search(r'[!@#$%^&*]', password):
        feedback.append("Password must include at least one special character (!@#$%^&*).")
    
    # Rule 6: Cannot be a common dictionary word
    if is_common_word(password):
        feedback.append("Password cannot be a common dictionary word.")

    # Determine strength based on feedback
    if not feedback:
        return "Strong", "Your password meets all the requirements."
    elif len(feedback) <= 2:
        return "Moderate", "Your password is okay but could be stronger. Issues: " + ", ".join(feedback)
    else:
        return "Weak", "Your password is weak. Issues: " + ", ".join(feedback)

# Main program
if __name__ == "__main__":
    while True:
        password = input("Enter your password: ")
        strength, message = evaluate_password_strength(password)
        print(f"Password Strength: {strength}")
        print(message)

        # Ask the user if they want to continue or exit
        choice = input("Do you want to check another password? (yes/no): ").strip().lower()
        if choice != 'yes':
            print("Exiting the program. Goodbye!")
            break
