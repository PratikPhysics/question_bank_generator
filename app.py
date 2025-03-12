import streamlit as st
import google.generativeai as genai

# Configure Gemini API
genai.configure(api_key=st.secrets["GOOGLE_API_KEY"])

def generate_mcqs(topic, num_questions, course):
    model = genai.GenerativeModel('gemini-2.0-flash')
    if course == "Data Science and AI":
        prompt = f"""Generate {num_questions} scenario based multiple-choice questions (MCQs) which also contains designations related to Data Science and AI on the topic of "{topic}".
        Each question should have fundamental interrogative such as 'what','why' and 'how' making the question thought provoking,
        Each question should have 4 options (a, b, c, d) and the correct answer should be clearly marked.

        Format:
        Question: [Question text]

        a) [Option a]
        b) [Option b]
        c) [Option c]
        d) [Option d]

        Answer: [Correct option]
        """
    elif course == "AWS, DevOps":
        prompt = f"""Generate {num_questions} scenario based multiple-choice questions (MCQs) which also contains designations related to Devops,AWS on the topic of "{topic}".
        Each question should have fundamental interrogative such as 'what','why' and 'how' making the question thought provoking,
        Each question should have 4 options (a, b, c, d) and the correct answer should be clearly marked.

        Format:
        Question: [Question text]

        a) [Option a]
        b) [Option b]
        c) [Option c]
        d) [Option d]

        Answer: [Correct option]
        """
    elif course == "FullStack Development":
        prompt = f"""Generate {num_questions} scenario based multiple-choice questions (MCQs) which also contains designations related to FullStack Development on the topic of "{topic}".
        Each question should have fundamental interrogative such as 'what','why' and 'how' making the question thought provoking,
        Each question should have 4 options (a, b, c, d) and the correct answer should be clearly marked.

        Format:
        Question: [Question text]

        a) [Option a]
        b) [Option b]
        c) [Option c]
        d) [Option d]

        Answer: [Correct option]
        """
    else:
        prompt = f"""Generate {num_questions} scenario based multiple-choice questions (MCQs) on the topic of "{topic}".
        Each question should have fundamental interrogative such as 'what','why' and 'how' making the question thought provoking,
        Each question should have 4 options (a, b, c, d) and the correct answer should be clearly marked.

        Format:
        Question: [Question text]

        a) [Option a]
        b) [Option b]
        c) [Option c]
        d) [Option d]

        Answer: [Correct option]
        """

    try:
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return f"An error occurred: {e}"

def main():
    st.image('logo.webp')
    st.title("MCQ Generator with gemimi 😎❤️")

    course = st.radio("Select Course:", ("Data Science and AI", "AWS, DevOps", "FullStack Development", "General"))

    topic = st.text_input("Enter the topic for MCQs:")
    num_questions = st.number_input("Enter the number of questions:", min_value=1, step=1)

    if st.button("Generate MCQs"):
        if topic and num_questions:
            with st.spinner("Generating MCQs..."):
                mcqs = generate_mcqs(topic, num_questions, course)
                st.markdown(mcqs)
        else:
            st.warning("Please enter both topic and number of questions.")

with st.sidebar:
    st.write('Just create MCQs and eat well!')
    #st.image('cutie-cat.gif')
    st.write('My LinkedIn : www.linkedin.com/in/pratik-ramteke-21573317a')
    st.write('My GitHub : https://github.com/PratikPhysics')
    st.write('Just call me : +91 7588399515')

if __name__ == "__main__":
    main()
