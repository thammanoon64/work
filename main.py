import streamlit as st
import random
import string

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

st.title("Generate Password")

# เลือกความยาวของรหัสผ่านโดยใช้สไลด์
length = st.slider("Select Length", 8, 100, 8)

# ปุ่มสำหรับสร้างรหัสผ่าน
if st.button("Generate Password"):
    password = generate_password(length)
    st.success(f"Your password is: {password}")