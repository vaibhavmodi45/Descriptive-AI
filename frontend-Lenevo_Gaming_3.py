import streamlit as st # type: ignore
# from streamlit_option_menu import option_menu # type: ignore

# Page configuration
st.set_page_config(page_title="Descriptive AI", layout="wide")

# CSS for custom styling
st.markdown("""
    <style>
    /* Navbar styling */
    .navbar {
        background-color: #ff4b4b;  
        padding: 10px;
        margin-bottom: 10px;
        margin-left: -50px;
        margin-right: -50px;
        font-family: Anton-Bold;
        text-align: Left;
        font-weight: bolder;
        font-size: 34px;
        color: white;
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
    }
    
    /* Footer */
    .footer {
        text-align: center;
        padding: 10px;
        background-color: #ff4b4b;
        color: white;
        position: fixed;
        width: 100%;
        bottom: 0;
    }
    
    </style>
""", unsafe_allow_html=True)

# Navbar
st.markdown('<div class="navbar">DESCRIPTIVE AI</div>', unsafe_allow_html=True)

# Input field
user_input = st.text_input("Enter title or content")

# Generate button
if st.button("Generate"):
    # Placeholder for the generated content
    st.success(f"Generated content for: {user_input}")

# Steps to use Descriptive AI
st.markdown('<div class="steps-container">', unsafe_allow_html=True)
st.markdown("### Steps to use Descriptive AI:")
st.markdown("1. Enter the appropriate title in the input field.")x
st.markdown("2. Click on the generate button.")
st.markdown("3. Get your generated content displayed below.")
st.markdown('</div>', unsafe_allow_html=True)

# Footer
st.markdown('<div class="footer">All Rights Reserved Developed by Vaibhav Modi</div>', unsafe_allow_html=True)