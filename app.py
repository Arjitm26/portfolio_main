from pathlib import Path

import streamlit as st
from PIL import Image

# --- PATH SETTINGS ---
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "main.css"
resume_file = current_dir / "CV.pdf"
profile_pic = current_dir / "Profile.png"

# --- GENERAL SETTINGS ---
PAGE_TITLE = "Arjit Mishra"
PAGE_ICON = "🤝"
LAYOUT = "wide"
NAME = "Arjit Mishra"
DESCRIPTION = """I'm a data-driven professional with 6 months of experience as a app developer intern. 
I'm passionate about leveraging data to solve complex problems and drive actionable insights. 
My background in Artificial Intelligence and Machine learning has equipped me with a strong foundation in 
problem-solving, critical thinking, data analysis. I'm proficient in programming languages : Python, R and have a 
keen interest in exploring the world of machine learning, data mining, and statistical modeling.
"""
EMAIL = "arjitmishra72@gmail.com"
SOCIAL_MEDIA = {
    "👋 LinkedIn": "https://www.linkedin.com/in/arjit-mishra-learner/"
}

st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON, layout=LAYOUT)

# --- LOAD CSS, PDF & PROFILE PIC ---
with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)
with open(resume_file, "rb") as pdf_file:
    PDFbyte = pdf_file.read()
profile_pic = Image.open(profile_pic)

# --- HERO SECTION ---
col1, col2 = st.columns(2, gap="small")
with col1:
    st.image(profile_pic, width=350)

with col2:
    st.title(NAME)
    st.write(DESCRIPTION)
    st.download_button(
        label=" 📄 Download Resume",
        data=PDFbyte,
        file_name=resume_file.name,
        mime="application/octet-stream",
    )
    st.write("📍 MP,India 📞 +91 7441183675")
    for index, (platform, link) in enumerate(SOCIAL_MEDIA.items()):
        st.write(f"[{platform}]({link})")
    st.write("✉️", EMAIL)

# --- SKILLS ---
st.write('\n')
st.subheader("Technical Skills")
info = {'skills':
            ['Python', 'Data Science', 'SQL',
             'Plotly', 'PowerBI', 'MS Excel', 'Amazon SageMaker','GenAI']
        }
skill_col_size = 6


def skill_tab():
    rows, cols = len(info['skills']) // skill_col_size, skill_col_size
    skills = iter(info['skills'])
    if len(info['skills']) % skill_col_size != 0:
        rows += 1
    for x in range(rows):
        columns = st.columns(skill_col_size)
        for index_ in range(skill_col_size):
            try:
                columns[index_].button(next(skills))
            except:
                break


with st.spinner(text="Loading section..."):
    skill_tab()

# --- WORK HISTORY ---
st.write('\n')
st.subheader("Work Experience")
st.write("---")

# --- JOB 1
st.write("💼", "**Flutter developer - Intern**")
st.write("03/22 - 08/22")
st.write(
    """
    - ► Worked as a front-end flutter developers and managed data workflows using Apache Airflow 
    - ►  Worked with team for 3 client projects such as School Bus management system , Woocommerce application for
        retailers and online consulting application 
    - ► Added video chat feature in consulting application along with UI/UX Building and API integration for 3 mobile
        applications both ios and android
"""
)

# --- Projects ---
st.write('\n')
st.subheader("Projects")
st.write("---")
st.markdown("✔️ YOURBOT")
st.markdown(""" This project aims to develop a versatile AI chatbot that adapts to various roles and contexts, leveraging
            OpenAI’s language models and Python’s Flask framework. The chatbot will process user input, generate relevant
            responses, and simulate different personas""")
st.markdown("[Check out here !](https://github.com/Arjitm26/YOURBOT)")
            

st.markdown("✔️ Avito-demand-prediction-Model")
st.markdown("""Developed a machine learning model to predict the probability of a deal being
closed for Avito advertisements. This model will enable Avito to provide valuable insights to sellers, optimize resource
allocation, and enhance user experience""")
st.markdown("[Check out here !](https://github.com/Arjitm26/Avito-demand-prediction-Model)")

st.markdown("✔️ ML-algorithm-for-stack-exchange")
st.markdown("""Machine learning model that accurately predicts various scores (e.g., question
quality, answer quality, user reputation) on Stack Exchange based on user intent. This model will improve the overall
user experience on the platform by identifying high-quality content and promoting community engagement""")
st.markdown("[Check out here !](https://github.com/Arjitm26/ML-algorithm-for-stack-exchange)")


# --- Certifications ---
st.write('\n')
st.subheader("Certifications")
st.write("---")
st.markdown("[🎯 Associate Data Scientist : Datacamp](https://www.datacamp.com/certificate/DSA0010623634126)")
st.markdown("[🎯 Google Data Analytics specialization](https://www.coursera.org/account/accomplishments/specialization/WPXKJEJ5X8QB)")
st.markdown("[🎯 AWS Academy Graduate - AWS Academy Machine Learning Foundations](https://www.credly.com/badges/52e2539a-91bc-47bd-9bd8-44ea73d56504/public_url)")

# --- Positions of Responsibility ---
st.write('\n')
st.subheader("Positions of Responsibility")
st.write("---")
st.markdown("🤝 CSR - Team Contributor")
st.markdown('Successfully led a team of 20+ volunteers to organise Coding competition 160 students '
            'eagle coding club')
st.markdown("🤝 National Cadet Corps - A")

# --- CONTACT ---
with st.container():
    st.write("---")
    st.subheader("Contact Me")
    st.write("##")

    col1, col2, col3 = st.columns(3)
    with col2:
        contact_form = """
        <form action="https://formsubmit.co/arjitmishra72@email.com" method="POST">
            <input type="hidden" name="_captcha" value="true">
            <input type="text" name="name" placeholder="Your name" required>
            <input type="email" name="email" placeholder="Your email" required>
            <textarea name="message" placeholder="Your message" required></textarea>
            <button type="submit">Send</button>
        </form>
        """
        st.markdown(contact_form, unsafe_allow_html=True)
