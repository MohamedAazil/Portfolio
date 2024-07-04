import streamlit as st
import google.generativeai as genai
api_key = st.secrets["GOOGLE_API_KEY"]
genai.configure(api_key=api_key)
model = genai.GenerativeModel('gemini-1.5-flash')

persona = """ 
    You are Mohamed Aazil AI bot. You help people answer questions about your self (i.e Mohamed Aazil) Answer as if you are responding . dont answer in second or third person.
    If you don't know they answer you simply say "That's a secret"
    Here is more info about Murtaza:
    20 year old 3rd year student doing btech artificial intelligence and data science at Rathinam Technical Campus in Coimbatore, India 
    Ambition : Data Scientist
"""


col1,col2 = st.columns(2)
with col1:
    st.subheader("Hello!!:wink::wave:")
    st.title("I am Mohamed Aazil")
    #st.page_link(label="LinkedIn",url="https://www.linkedin.com/in/mohamed-aazil/")
    if st.button("LinkedIn"):
        st.write("[Go to LinkedIn](https://www.linkedin.com/in/mohamed-aazil/)")
    
with col2:
    st.image("Images/Aazil.jpg")

st.title("")

st.title("Aazil's AI Navigator")
st.subheader("I'm here to guide you")
qn = st.text_input("Ask anything about me")


if st.button("Ask",use_container_width=10):
    st.header(model.generate_content(persona + "Here is the question" + qn).text)

st.title("")
col1,col2 = st.columns(2)

st.title("Projects")
col1,col2 = st.columns(2)
with col1:
    st.subheader("- Drowsiness Detection")
    st.subheader("- Chatbot Using Langchain")
    st.subheader('- "Linkberry" Course Cohort')
    st.subheader("- Whatsapp Sentiment Analysis")
    st.subheader("- Rock Paper Scissors Game")
with col2:
    if st.button("Github"):
        st.write("https://github.com/MohamedAazil/Projects/tree/main/Projects/Python/Drowsiness_detection")

st.title("Academics")
st.subheader("3rd Year")
st.slider("",1,4,3)
