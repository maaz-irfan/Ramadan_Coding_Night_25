import streamlit as st
import random
import string

def generator_password(length, use_digits, use_secial):
    characters = string.ascii_letters
    
    if use_digits:
        characters += string.digits
        
    if use_secial:
        characters += string.punctuation
        
    return ''.join(random.choice(characters) for i in range(length)) 

st.title('Password Generator')

length = st.slider("select password length", min_value=6, max_value=32, value=12)
      
use_digits = st.checkbox("Include Digits")

use_special = st.checkbox("Include Special Characters")

if st.button("Generate Password"):
    password = generator_password(length, use_digits, use_special)
    st.write(f"Gnerated Password: {password}")
    
st.write("------------------------")

st.write("Build with ❤️ by [maaz irfan](https://github.com/maaz-irfan)")          