import streamlit as st
from groq import Groq

st.set_page_config(page_title='LLM', layout='centered')
st.title('AI Interview')
st.caption('Practice and Prepare for your placement')
try:
    client = Groq(api_key=st.secrets["GROQ_API_KEY"])
except (KeyError, FileNotFoundError):
    st.error("API key is missing. Add it in Advanced Settings.")
    st.stop()
role = st.selectbox("Job Title", ["Machine Learning Engineer", "Senior Software Engineering", "Full Stack Engineer", "Backend Engineer", "Others"])
if role =="Others":
    st.text_input("Enter your Job Title","XXXXXX")
model = st.selectbox(
    "Choose Your Model",
    [
        "openai/gpt-oss-120b",
        "openai/gpt-oss-20b"
    ]
)
level=st.selectbox(
    "Choose your level",
    [
        "Beginner", "Intermediate", "Advanced"
    ]
)
mode = st.radio("Activity",["Generate Question", "Generate Code Questions", "Evaluate Answers", "Improve Answer"])
if mode =="Generate Question" :
    count = st.slider("Number Of Questions",1,10,5)
elif mode =="Generate code Questions" :
    topic = st.selectbox( "Select Topic",
                         [ "Python", "C++", "C", "DSA", "Aptitude","Java"])
    count= st.slider("Number of Questions",1,10,5)
else:
    question = st.text_area("Enter Interview Question Here")
    answer = st.text_area("Enter Your Answer", height=160)
if st.button("Generate AI Response",type="primary"):
  if mode == (['Evaluate Answer', 'Improve Answer'] and (not question.strip() or not answer.strip()):
      st.warning("please enter a valid question and answer")
     st.stop()
topics = "Topics is" + topic + "Difficulty is" + level
if mode = "Generate Question":
   task = "Generate" + str(count) +  "Frequently asked Interview Question 3 theory and 2 logical Questions. Do not give answers , Give Hints" 
elif mode == "Generate Code Questions":
    task = "Generate "+str(count)+"Frequently asked coding question on topic "+topic+"and give hints to slove them.Be accurate."
elif mode == "Evaluate Answers":
    task = "Question:"+question+"My Answer:"+answer+" Evaluate my answer based on correctness, relevance, clarity, completeness. Give a score out of 10, identify mistakes,"
elif mode == "Improve Answer":
    task = "Question:"+question+"My Answer:"+answer+" Evaluate my original answer, correct technical mistakes, add missing information,provide a complete improved interview answer in natural English."
background = "Job role:" +role+ "Difficulti level "+level
with st.spinner ("Generate your answer......")
    try:
        response = client.chat.completion.create(
            model = gen_model,
            messages = [{"role":"system",
                         "content":"Act as a Senior Interviewer, both HR and Technical expert"}
                        {"role":"user",
                         "content" : background + task }],
            temperature = 0.7,
            max_tokens = 1000 )
            output = response.choices[0].message.content
            st.subheader("AI Response")
            st.markdown(output)
            st.download_button("Download Response", output , file_name = "Interview_Response.txt", mime = 'text/plain')
        )
except Exception as e:
    st.error ("API connection was unsuccessful : ", e)
    st.info("Please check your API key and rate limits")
st.caption("powered by streamlit.io And GitHub")
                         
    
