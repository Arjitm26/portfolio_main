from pathlib import Path
import streamlit as st
from PIL import Image
from dotenv import load_dotenv
import streamlit as st 
from langchain_groq import ChatGroq
import os 
from PIL import Image
import json
from streamlit.components.v1 import html


# --- PATH SETTINGS ---
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "main.css"
resume_file = current_dir / "Arjit mishra resume.pdf"
profile_pic = current_dir / "Profile.png"

# --- GENERAL SETTINGS ---
PAGE_TITLE = "Arjit Mishra"
PAGE_ICON = "🤝"
LAYOUT = "wide"
NAME = "Arjit Mishra"
DESCRIPTION = """Aspiring Data Scientist with a B.Tech in AI/ML, skilled in Python, SQL, and machine learning.
Former AI Intern at Koncpt AI where I built healthcare recommendation systems using RAG with 87% accuracy.
Completed Gen AI internship at Google Cloud, developing an ATS Resume Analyzer with Gemini Pro 1.5. Proficient in frameworks
like TensorFlow, Langchain, Flutter and multimodal AI applications. Passionate about solving 
complex business challenges through AI-powered solutions, validated by certifications from DataCamp, Google, and AWS.
"""
EMAIL = "arjitmishra79@gmail.com"
SOCIAL_MEDIA = {
    "👋 Linkedin": "https://www.linkedin.com/in/arjit-mishra-learner/"
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

# ---Bot ---
# Inject custom HTML/CSS/JavaScript for the floating button and popup

load_dotenv()

model = ChatGroq(model="llama3-8b-8192")

with open('cv.json','r') as file:
    resume = json.load(file) 

def bot_response(user_query):
    context = f"""
    You are a chatbot designed to answer questions about my resume. Here are the details:
    {json.dumps(resume, indent=2)}
    """
    prompt = f"{context}\n\nUser: {user_query}\nChatbot:"
    response = model.invoke(prompt)
    return response.content

st.markdown("""
<style>
.stPopover {
    position: fixed;
    bottom: 10px;
    right: 10px;
    z-index: 1000 !important;
}
.streamlit-expanderContent {
    z-index: 999 !important;
}
</style>
""", unsafe_allow_html=True)

with st.popover("Ask anything about me !"):
    prompt = st.chat_input("Say something")
    if prompt:
        st.write(bot_response(prompt))

# --- SKILLS ---
st.write('\n')
st.subheader("Technical Skills")
info = {'skills':
            ['Python', 'SQL','Pyspark','Machine learning' , 'Deep learning',
             'Plotly', 'PowerBI', 'Langchain','GenAI','MS Excel']
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
st.write("💼", "**AI - Intern**")
st.write("Koncpt AI")
st.write("07/24 - 01/25")
st.write(
    """
    - ► Deployed a healthcare recommendation RAG, processing patient health metrics to provide personalized health
        insights with 87% accuracy and reduced response latency by 60% through efficient caching.
    - ► Developed a multi modal RAG system using GCP Vertex AI platform that seamlessly integrated medical imaging
        analysis with textual patient records.
    - ► Engineered monitoring and feedback loop systems for continuous model improvement, including recommendation
        quality tracking.
"""
)
st.write("\n")
# --- JOB 2
st.write("💼", "**Gen AI - Intern**")
st.write("Google cloud")
st.write("10/24 - 11/24")
st.write(
    """
    - ► Led the development of an ATS Resume Analyzer using Gemini Pro 1.5 model, successfully deploying it on Streamlit
        to provide automated resume screening and analysis capabilities.
    - ► Gained hands-on experience with Google’s generative AI models, focusing on prompt engineering and model fine tuning.
"""
)
st.write("\n")
# --- JOB 3
st.write("💼", "**Flutter developer - Intern**")
st.write("Phaico One")
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
st.markdown("✔️ Classification of Disaster Tweets")
st.markdown(""" Classified tweets as disaster-related or non using NLP techniques. The project
involved extensive data preprocessing, including text cleaning, tokenization, and feature extraction using techniques like
TF-IDF and word embeddings. Implemented and compared various classification algorithms such as Logistic Regression,
Random Forest, and XGBoost. Achieved an accuracy of 82% and optimized performance using hyperparameter tuning.""")
st.markdown("[Check out here !](https://github.com/Arjitm26/Disaster-tweets-Classification)")
            

st.markdown("✔️ ML-algorithm-for-stack-exchange")
st.markdown("""Machine learning model that accurately predicts various scores (e.g., question
quality, answer quality, user reputation) on Stack Exchange based on user intent.Using NLP ,Word embedding, Vectorization and Model training""")
st.markdown("[Check out here !](https://github.com/Arjitm26/ML-algorithm-for-stack-exchange)")

st.markdown("✔️ Smart Search Tool")
st.markdown("""Course discovery platform that leverages web scraping to aggregate free courses from Edtech
Platforms. Using RAG with FAISS vector database and prompt engineering, it delivers hyper-personalized course
recommendations based on semantic search and learner preferences. Built with Python, BeautifulSoup, LangChain, and
vector embeddings, this tool transforms the course search experience into an AI-powered educational journey.
""")
st.markdown("[Check out here !](https://huggingface.co/spaces/arzzit/analytics_vidhya_smart_search)")


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
st.markdown('Successfully led a team of 10+ volunteers to organise Coding competition 160 students '
            'Eagle coding club')
st.markdown("🤝 National Cadet Corps - A")

# --- CONTACT ---
with st.container():
    st.write("---")
    st.subheader("Contact Me")
    st.write("##")

    col1, col2, col3 = st.columns(3)
    with col2:
        contact_form = """
        <form action="https://formsubmit.co/arjitmishra79@gmail.com" method="POST">
            <input type="hidden" name="_captcha" value="true">
            <input type="text" name="name" placeholder="Your name" required>
            <input type="email" name="email" placeholder="Your email" required>
            <textarea name="message" placeholder="Your message" required></textarea>
            <div class="button-container">
                <button type="submit">Send</button>
            </div>
        </form>
        """
        st.markdown(contact_form, unsafe_allow_html=True)
