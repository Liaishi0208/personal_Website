import streamlit as st
import base64
import os

def resume_page():
    pdf_file_path = os.path.join("static", "docs", "resume.pdf")

    if os.path.exists(pdf_file_path):
        with open(pdf_file_path, "rb") as pdf_file:
            PDFbyte = pdf_file.read()

        # Display the download button
        st.download_button(label="Download Resume",
                        data=PDFbyte,
                        file_name="LI Aishi.pdf",
                        mime='application/octet-stream')
    else:
        st.warning("Resume PDF file not found")

    st.title("LI Aishi")

    st.header("Contact Information")
    st.markdown("""
    - **Email:** aishili02@outlook.com
    - **Phone:** +852 94205259 
    - **GitHub:** [https://github.com/Liaishi0208/web.git](https://github.com/Liaishi0208/web.git)
    - **Address:** Southland, 11 Heung Yip Road | Wong Chuk Hang, Hong Kong
    """)

    st.header("Professional Summary")
    st.markdown("""
    Dynamic and results-oriented Master of Science in Marketing candidate at The Chinese University of Hong Kong, specializing in Big Data, with a Bachelor’s in Finance from Bentley University, offering a robust blend of financial expertise, data analysis, and strategic marketing skills, demonstrated through internships at MCI CPA Limited, Forkaia, and Guosen Securities, and leadership as Director of Operations at the Chinese Students & Scholars Association.
    """)

    st.header("Intern Experience")
    st.markdown("""
    **Finance Intern , MCI CPA LIMITED, Hong Kong**
    - *Summer 2023 *
    - Participated as a trainee in audit assignments, financial due diligence, and corporate restructuring exercise for pre-IPO project.  
    
    **Internship program, Forkaia, Irvine, CA**
    - *December 2021 – August 2022 *
    - Practiced multiple tasks such as collecting and analyzing data for potential business expansion, identifying specific business opportunities, prepare financial reports with reliable conclusions that management can use to implement more effective operational strategies.  
                
    **Asset Management Intern  , Guosen Securities (HK) Financial Holdings Co., Ltd, Hong Kong**
    - *Summer 2019 *
    - Learned the basic operation methods and teamwork skills within a large corporation and participated in practice projects of analyzing and predicting asset funds.  .             
    """)

    st.header("Education")
    st.markdown("""
    **Master of Science in Marketing, Big Data Concentration**
    - The Chinese University of Hong Kong
    - *Graduated: June 2025*
    - GPA: 3.4/4.0      


    **Bachelor of Science, Finance Major, Capital Markets Concentration, Psychology Minor**
    - Bentley University, Waltham, MA 
    - *Graduated: May 2024*
    - Cumulative GPA 3.11/4.00 Major GPA 3.48/4.00  
    
    **High School**
    - Aiglon College, Vaud, Switzerland
    - *Graduated: May 2020*
    - Dean’s List, Honor Roll, Duke of Edinburgh Bronze Award 
    """)

    st.header("Skills")
    st.markdown("""
    - **Computer:** Microsoft Office Suite, Bloomberg, FactSet, Adobe Suite, Access, RStudio, Python, Canva. 
    - **Soft Skills:** Team Leadership, Project Management, Problem-Solving, Communication
    """)


    st.header("Languages")
    st.markdown("""
    - **English:** Native
    - **Cantonese:** Intermediate
    - **Mandarin:** Native
    """)

    st.header("Interests")
    st.markdown("""
    - Blogging about technology trends
    - Hiking and outdoor activities
    """)

    st.markdown("---") 