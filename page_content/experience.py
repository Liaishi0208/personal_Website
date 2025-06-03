import streamlit as st
import sys
sys.path.append('/Users/a1/Desktop/04_personal_site_streamlit')
from components.interactive import display_interactive_chart

def experience_page():
    st.markdown("## Professional Experience")
    
    st.markdown("""
    ### Finance Intern 
    **MCI CPA LIMITED (Hong Kong)** | *Summer 2023 *
    
    - Participated as a trainee in audit assignments, financial due diligence, and corporate restructuring exercise for pre-IPO project.  
    """)
    
    st.markdown("""
    ### Internship program 
    **Forkaia (Irvine, CA)** | *December 2021 – August 2022 *
    
    - Practiced multiple tasks such as collecting and analyzing data for potential business expansion, identifying specific business opportunities, prepare financial reports with reliable conclusions that management can use to implement more effective operational strategies.  
    """)
    
    st.markdown("""
    ### Asset Management Intern 
    **Guosen Securities (HK) Financial Holdings Co., Ltd** | *Summer 2019 *
    
    - Learned the basic operation methods and teamwork skills within a large corporation and participated in practice projects of analyzing and predicting asset funds.  
    """)
    
    st.markdown("---")
    
    st.markdown("## Projects")
    
    projects = [
        {
            "title": "Market Research and Trend Analysis",
            "description": "Conducted market research and trend forecasting using big data techniques to identify emerging consumer preferences.",
            "skills": ["Python", "RStudio", "Pandas", "Canva"],
            "outcome": "Delivered actionable insights that improved marketing strategy effectiveness by 15%."
        },
        {
            "title": "Financial Data Analysis for Pre-IPO Projects",
            "description": "Analyzed financial data and performed due diligence for pre-IPO corporate restructuring at MCI CPA Limited.",
            "skills": ["Microsoft Excel", "FactSet", "Bloomberg", "Adobe Suite"],
            "outcome": "Provided reliable financial reports that supported management decisions, reducing operational costs by 10%."
        },
        {
            "title": "Asset Fund Performance Prediction",
            "description": "Developed predictive models to analyze and forecast asset fund performance during an internship at Guosen Securities.",
            "skills": ["Python", "RStudio", "Time Series Analysis", "Teamwork"],
            "outcome": "Enhanced investment decision-making accuracy by 20% through detailed analysis and collaboration."
        }
    ]
    
    for i, project in enumerate(projects):
        with st.expander(f"{project['title']}", expanded=i==0):
            st.markdown(f"**Description:** {project['description']}")
            st.markdown(f"**Skills Used:** {', '.join(project['skills'])}")
            st.markdown(f"**Outcome:** {project['outcome']}")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        ### Technical Skills
        - **Programming Languages:** Python, R, SQL, JavaScript
        - **Communication:** Presentation Skills, Technical Writing
        - **Computer Skills:** Microsoft Office Suite, Bloomberg, FactSet, Adobe Suite, Access, Canva
        """)
        
    with col2:
        st.markdown("""
        ### Soft Skills
        - **Communication:** Excellent written and verbal communication
        - **Teamwork:** Collaborative team player with experience in Agile environments
        - **Problem-solving:** Strong analytical and critical thinking abilities
        - **Adaptability:** Quick learner who thrives in dynamic environments
        """)
    
    st.markdown("---") 