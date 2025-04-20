def evaluate_password_strength(password):
    """Evaluate the strength of a password based on various criteria."""
    score = 0
    feedback = []
    
    # Check length
    if len(password) >= 8:
        score += 1
    else:
        feedback.append("Password should be at least 8 characters long.")
    
    # Check for uppercase letters
    if any(char.isupper() for char in password):
        score += 1
    else:
        feedback.append("Password should contain at least one uppercase letter.")
    
    # Check for lowercase letters
    if any(char.islower() for char in password):
        score += 1
    else:
        feedback.append("Password should contain at least one lowercase letter.")
    
    # Check for digits
    if any(char.isdigit() for char in password):
        score += 1
    else:
        feedback.append("Password should contain at least one digit (0-9).")
    
    # Check for special characters
    special_chars = "!@#$%^&*"
    if any(char in special_chars for char in password):
        score += 1
    else:
        feedback.append(f"Password should contain at least one special character ({special_chars}).")
    
    # Determine strength rating
    if score <= 2:
        strength = "Weak"
    elif score <= 4:
        strength = "Moderate"
    else:
        strength = "Strong"
    
    return score, strength, feedback

def main():
    print("Password Strength Meter")
    print("-----------------------")
    
    while True:
        password = input("Enter your password (or 'quit' to exit): ")
        
        if password.lower() == 'quit':
            print("Exiting the program...")
            break
        
        score, strength, feedback = evaluate_password_strength(password)
        
        print(f"\nPassword Strength: {strength} (Score: {score}/5)")
        
        if strength == "Strong":
            print("✅ Excellent! Your password meets all security criteria.")
        else:
            print("🔍 Suggestions to improve your password:")
            for suggestion in feedback:
                print(f"- {suggestion}")
        
        print("\n" + "="*50 + "\n")

if __name__ == "__main__":
    main()
    
    