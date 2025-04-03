import streamlit as st
import random
import time

st.title("📝 Quiz Application")

# Define 20 quiz questions
questions = [
    {"question": "What is the capital of Pakistan?", "options": ["Lahore", "Karachi", "Islamabad", "Peshawar"], "answer": "Islamabad"},
    {"question": "Who is the founder of Pakistan?", "options": ["Allama Iqbal", "Liaquat Ali Khan", "Muhammad Ali Jinnah", "Benazir Bhutto"], "answer": "Muhammad Ali Jinnah"},
    {"question": "Which is the national language of Pakistan?", "options": ["Punjabi", "Urdu", "Sindhi", "Pashto"], "answer": "Urdu"},
    {"question": "What is the currency of Pakistan?", "options": ["Rupee", "Dollar", "Taka", "Riyal"], "answer": "Rupee"},
    {"question": "Which city is known as the City of Lights in Pakistan?", "options": ["Lahore", "Islamabad", "Faisalabad", "Karachi"], "answer": "Karachi"},
    {"question": "Which is the largest province of Pakistan by area?", "options": ["Punjab", "Sindh", "Balochistan", "KPK"], "answer": "Balochistan"},
    {"question": "Which river is the longest in Pakistan?", "options": ["Indus", "Jhelum", "Chenab", "Ravi"], "answer": "Indus"},
    {"question": "Who wrote the national anthem of Pakistan?", "options": ["Allama Iqbal", "Hafeez Jalandhari", "Faiz Ahmed Faiz", "Ahmed Faraz"], "answer": "Hafeez Jalandhari"},
    {"question": "Which sea borders Pakistan?", "options": ["Arabian Sea", "Red Sea", "Caspian Sea", "Black Sea"], "answer": "Arabian Sea"},
    {"question": "When did Pakistan become an Islamic Republic?", "options": ["1947", "1956", "1965", "1971"], "answer": "1956"},
    {"question": "What is the national flower of Pakistan?", "options": ["Rose", "Jasmine", "Tulip", "Sunflower"], "answer": "Jasmine"},
    {"question": "Who was the first Prime Minister of Pakistan?", "options": ["Liaquat Ali Khan", "Zulfikar Ali Bhutto", "Benazir Bhutto", "Imran Khan"], "answer": "Liaquat Ali Khan"},
    {"question": "Which mountain is the highest in Pakistan?", "options": ["Nanga Parbat", "Rakaposhi", "Broad Peak", "K2"], "answer": "K2"},
    {"question": "When did Pakistan conduct nuclear tests?", "options": ["1995", "1998", "2000", "2002"], "answer": "1998"},
    {"question": "Which city is known as the Manchester of Pakistan?", "options": ["Karachi", "Lahore", "Faisalabad", "Sialkot"], "answer": "Faisalabad"},
    {"question": "What is the national sport of Pakistan?", "options": ["Cricket", "Hockey", "Football", "Squash"], "answer": "Hockey"},
    {"question": "Which is the largest desert in Pakistan?", "options": ["Cholistan", "Thar", "Kharan", "Thal"], "answer": "Thar"},
    {"question": "What is the total number of provinces in Pakistan?", "options": ["2", "3", "4", "5"], "answer": "4"},
    {"question": "Who was the first President of Pakistan?", "options": ["Ayub Khan", "Iskander Mirza", "Zia-ul-Haq", "Pervez Musharraf"], "answer": "Iskander Mirza"},
]

# Initialize session state
if "quiz_questions" not in st.session_state:
    st.session_state.quiz_questions = random.sample(questions, min(20, len(questions)))
    st.session_state.current_index = 0
    st.session_state.score = 0
    st.session_state.mistakes = 0

# Check if quiz is complete
if st.session_state.current_index < len(st.session_state.quiz_questions):
    question = st.session_state.quiz_questions[st.session_state.current_index]
    st.subheader(f"Q{st.session_state.current_index + 1}: {question['question']}")
    selected_option = st.radio("Choose your answer", question["options"], key=f"answer{st.session_state.current_index}")
    
    if st.button("Submit Answer"):
        if selected_option == question["answer"]:
            st.success("✅ Correct!")
            st.session_state.score += 1
        else:
            st.error(f"❌ Incorrect! The correct answer is {question['answer']}")
            st.session_state.mistakes += 1
        
        time.sleep(2)
        st.session_state.current_index += 1
        st.rerun()

else:
    st.subheader("🎉 Quiz Completed!")
    st.write(f"✅ Your Score: {st.session_state.score}/20")
    st.write(f"❌ Mistakes: {st.session_state.mistakes}")
    
    if st.session_state.mistakes > 3:
        st.error("❌ You Failed! More than 3 mistakes.")
    else:
        st.success("🎊 Congratulations! You Passed! 🎊")
        
        if st.session_state.mistakes == 1:
            st.write("🥇 You secured First Position!")
            st.balloons()
        elif st.session_state.mistakes == 2:
            st.write("🥈 You secured Second Position!")
        else:
            st.write("🥉 You secured Third Position!")
    
    if st.button("Restart Quiz"):
        del st.session_state.quiz_questions
        del st.session_state.current_index
        del st.session_state.score
        del st.session_state.mistakes
        st.rerun()
