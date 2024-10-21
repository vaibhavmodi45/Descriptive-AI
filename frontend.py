import streamlit as st # type: ignore
from PIL import Image, ImageFilter
# from streamlit_option_menu import option_menu # type: ignore

# Page configuration
st.set_page_config(page_title="Descriptive AI", layout="wide")

# CSS for custom styling
st.markdown("""
    <style>
    /* Navbar styling */
    .navbar {
        background-color: ;
        padding-left:2px;
        text-align: left;
        font-weight: bolder;
        font-size: 44px;
        color: black;
    }

    hr {
        margin-top: 8px;
        margin-bottom: 48px;
    }
    
    /* Input, button, and generated content styling */
    .generate-btn {
        background-color: #ff4b4b;
        border-radius: 5px;
        padding: 10px;
        color: white;
        font-weight: bold;
    }
    
    /* Steps container */
    .steps-container {
        background-color: #f0f0f0;
        border-radius: 10px;
        padding: 20px;
        margin-top:50px;
    }
    
    /* Footer */
    .footer {
        text-align: center;
        padding: 10px;
        background-color: #ff4b4b;
        color: white;
        position: scroll;
        margin-top: 100px;
        width: 100%;
    }
    
    </style>
""", unsafe_allow_html=True)

# Navbar
st.markdown('<div class="navbar">DESCRIPTIVE AI 📝 <hr></div>', unsafe_allow_html=True)

# Toggle for Dark/Light Mode
#theme = st.sidebar.radio('Choose theme', ['Light', 'Dark'])

# Input field
user_input = st.text_input("Enter title or content")

# Generate button
if st.button("Generate"):
    # Placeholder for the generated content
    st.success(f"Generated content for: {user_input}")

# Steps to use Descriptive AI
st.markdown('<div class="steps-container">', unsafe_allow_html=True)
st.subheader("Steps to use Descriptive AI:")
st.markdown("1. Enter the appropriate title in the input field.")
st.image('1.png')
st.markdown("2. Click on the generate button.")
st.image('2.png')
st.markdown("3. Get your generated content displayed below.")
st.image('3.png')
st.markdown('</div>', unsafe_allow_html=True)

# Footer
st.markdown('<div class="footer">All Rights Reserved <br> Developed by Team @Descriptive_AI</div>', unsafe_allow_html=True)