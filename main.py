import streamlit as st
import random
import string

def generate_password(length, uppercase, special_chars, digits):
    characters = string.ascii_lowercase
    if uppercase:
        characters += string.ascii_uppercase
    if special_chars:
        characters += string.punctuation
    if digits:
        characters += string.digits
    
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

st.title("Generate Password")

# เลือกความยาวของรหัสผ่านโดยใช้สไลด์
length = st.slider("Select Length", 8, 100, 8)

# เลือกประเภทของอักขระที่ต้องการให้เป็นส่วนประกอบของรหัสผ่าน
uppercase = st.checkbox("Include Uppercase Letters")
special_chars = st.checkbox("Include Special Characters")
digits = st.checkbox("Include Digits")

# ปุ่มสำหรับสร้างรหัสผ่าน
if st.button("Generate Password"):
    password = generate_password(length, uppercase, special_chars, digits)
    st.success(f"Your password is: {password}")
