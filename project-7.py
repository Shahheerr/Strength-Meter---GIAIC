import streamlit as st # type: ignore
import re
import random
import string

# List of common weak passwords
COMMON_PASSWORDS = ["password", "123456", "12345678", "qwerty", "password123", "abc123", "letmein"]

# Function to check password strength
def check_password_strength(password):
    score = 0
    feedback = []
    
    # Check if password is too common
    if password.lower() in COMMON_PASSWORDS:
        feedback.append("❌ This is a commonly used weak password! Choose something more secure.")
        return "Weak", feedback
    
    # Length Check
    if len(password) >= 8:
        score += 1
    else:
        feedback.append("❌ Password should be at least 8 characters long.")
    
    # Upper & Lowercase Check
    if re.search(r"[A-Z]", password) and re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("❌ Include both uppercase and lowercase letters.")
    
    # Digit Check
    if re.search(r"\d", password):
        score += 1
    else:
        feedback.append("❌ Add at least one number (0-9).")
    
    # Special Character Check
    if re.search(r"[!@#$%^&*]", password):
        score += 1
    else:
        feedback.append("❌ Include at least one special character (!@#$%^&*).")
    
    # Strength Rating
    if score == 4:
        return "Strong", ["✅ Strong Password! Your password is secure. 🔒"]
    elif score == 3:
        return "Moderate", ["⚠️ Moderate Password - Consider adding more security features."]
    else:
        return "Weak", feedback

# Function to generate a strong password
def generate_strong_password():
    length = 12
    characters = string.ascii_letters + string.digits + "!@#$%^&*"
    password = "".join(random.choice(characters) for _ in range(length))
    return password

# Streamlit UI
st.title("🔐 Password Strength Meter")
st.write("Check your password strength and get suggestions for a strong password.")

# User input
password = st.text_input("Enter your password:", type="password")

if password:
    strength, feedback = check_password_strength(password)
    
    if strength == "Strong":
        st.success("✅ Your password is strong!")
    elif strength == "Moderate":
        st.warning("⚠️ Your password is moderate. Try improving it.")
    else:
        st.error("❌ Your password is weak. Improve it using the suggestions below:")
    
    # Show feedback
    for tip in feedback:
        st.write("- " + tip)
    
    # Suggest a strong password if weak
    if strength == "Weak":
        st.write("🔹 **Suggested Strong Password:**", generate_strong_password())
