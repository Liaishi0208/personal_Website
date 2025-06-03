import streamlit as st
from PIL import Image
import os

def home_page():
    left_col, right_col = st.columns(2)
    left_col.markdown(
        """
        <h4>LI Aishi</h4>
        <p>Recent Master's Graduate in Marketing<br>
        Chinese University of Hong Kong<br>
        12 Chak Cheung St., Ma Liu Shui, HKSAR<br>
        <a href="mailto:aishili02@outlook.com">aishili02@outlook.com</a></p>
        """,
        unsafe_allow_html=True
    )

    # add a photo to the right column
    image_path = os.path.join("static", "images", "images.jpg")
    if os.path.exists(image_path):
        image = Image.open(image_path)
        right_col.image(image, width=200)
    else:
        right_col.warning("Profile image not found")

    st.markdown("---")

    st.markdown(
        """
        ### About Me
        Hello, I’m Aishi (Alice) Li, a dynamic and results-oriented Master of Science in Marketing candidate at The Chinese University of Hong Kong, specializing in Big Data. With a solid foundation in finance from my Bachelor’s degree at Bentley University and hands-on experience in data analysis, I’ve honed my skills in market research and strategic marketing. During my internships at MCI CPA Limited, Forkaia, and Guosen Securities, I contributed to financial due diligence, business expansion analysis, and asset fund predictions, sharpening my analytical and teamwork abilities. As Director of Operations for the Chinese Students & Scholars Association, I led event planning and resource management, fostering collaboration and professional growth. Proficient in Python, RStudio, and tools like Bloomberg and Adobe Suite, I’m eager to leverage my skills to enhance brand visibility and customer engagement.
        """
    )

    st.markdown(
        """
        ### Skills
        - Communication: Presentation Skills, Technical Writing
        - Microsoft Office Suite, Bloomberg, FactSet, Adobe Suite, Access, RStudio, Python, Canva. 
        - Due Diligence in English and Mandarin, excellent verbal and written communication skills, logical and analytical thinking, sales, and ability to multitask and prioritize projects. 
        """
    )

    st.markdown("---")
    
    # Interactive component has been moved to the experience page 