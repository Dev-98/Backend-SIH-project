import streamlit as st


user_responses = []
  
questions = {
    "1": "What subjects in school do you enjoy the most? Why?",
    "2": "Outside of school, what activities or hobbies do you find most engaging?",
    "3": "Is there something you'd like to get better at?",
    "4": "Is there a job or career that you've heard about and find interesting?",
    "5": "When faced with a problem, how do you like to approach it?"
}

options = {
    "1A": "Science",
    "1B": "Math",
    "1C": "English/Language Arts",
    "2A": "Leading or Organizing Group Activities",
    "2B": "Solving Puzzles or Brain Teasers",
    "2C": "Working with Computers or Technology",
    "3A": "Math",
    "3B": "Writing or Language Arts",
    "3C": "Science",
    "4A": "Doctor or Scientist",
    "4B": "Teacher or Counselor",
    "4C": "Engineer or IT Professional",
    "5A": "Analyzing Data and Facts",
    "5B": "Talking to Others and Getting Different Perspectives",
    "5C": "Using Technology or Tools to Find Solutions"
   
}

st.title("Career Counseling Questionnaire")

for question_key, question_text in questions.items():
    st.write(question_text)
    options_keys = [f"{question_key}{option_key}" for option_key in options.keys() if option_key.startswith(question_key)]
    option = st.selectbox(f"Select an option for Question {question_key}", options[ques])
    user_responses.append(option)

if st.button("Submit"):
    st.write("Career Recommendations:",user_responses)
