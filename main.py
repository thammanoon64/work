import streamlit as st
import random
import string

def generate_password(length, uppercase, lowercase, special_chars, digits, text_to_include):
    characters = ''
    if lowercase:
        characters += string.ascii_lowercase
    if uppercase:
        characters += string.ascii_uppercase
    if special_chars:
        characters += string.punctuation
    if digits:
        characters += string.digits
    
    if text_to_include:
        if not all(char in characters for char in text_to_include):
            st.error("Text to include contains characters not selected in options!")
            return None
    
    password = ''.join(random.choice(characters) for _ in range(length - len(text_to_include)))
    password += text_to_include
    password = ''.join(random.sample(password, len(password)))  # Shuffle the password
    return password

st.title("Generate Password")

# เลือกความยาวของรหัสผ่านโดยใช้สไลด์
length = st.slider("Select Length", 8, 100, 8)

# เลือกประเภทของอักขระที่ต้องการให้เป็นส่วนประกอบของรหัสผ่าน
lowercase = st.checkbox("Include Lowercase Letters")
uppercase = st.checkbox("Include Uppercase Letters")
special_chars = st.checkbox("Include Special Characters")
digits = st.checkbox("Include Digits")

# ป้อนข้อความที่ต้องการจะเพิ่มในรหัสผ่าน
text_to_include = st.text_input("Text to include in password", "")

# ปุ่มสำหรับสร้างรหัสผ่าน
if st.button("Generate Password"):
    password = generate_password(length, uppercase, lowercase, special_chars, digits, text_to_include)
    if password:
        st.success(f"Your password is: {password}")
