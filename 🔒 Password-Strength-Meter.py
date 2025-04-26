#🔒 Password Strength Meter with Streamlit

import streamlit as st
import re

# Streamlit App Title
st.title("🔐 Password Strength Meter")

# User input for password
password = st.text_input("Enter your password", type="password")

# Password strength evaluation function
def evaluate_password_strength(password):
    strength = 0
    remarks = []

    # Length check
    if len(password) >= 8:
        strength += 1
    else:
        remarks.append("Use at least 8 characters")

    # Digit check
    if re.search(r"\d", password):
        strength += 1
    else:
        remarks.append("Include at least one number")

    # Uppercase check
    if re.search(r"[A-Z]", password):
        strength += 1
    else:
        remarks.append("Include at least one uppercase letter")

    # Lowercase check
    if re.search(r"[a-z]", password):
        strength += 1
    else:
        remarks.append("Include at least one lowercase letter")

    # Special character check
    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        strength += 1
    else:
        remarks.append("Include at least one special character")

    return strength, remarks

# Display password strength
if password:
    strength, suggestions = evaluate_password_strength(password)
    st.progress(strength / 5)
    
    if strength == 5:
        st.success("Strong password! ✅")
    elif strength >= 3:
        st.warning("Moderate password. 🟡 Try improving it.")
    else:
        st.error("Weak password! 🔴 Consider updating it.")

    if suggestions:
        st.info("Suggestions:")
        for suggestion in suggestions:
            st.write(f"- {suggestion}")
