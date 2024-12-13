import time
import streamlit as st
import io
from summarize import summarizer 
from sentiment import sentiment_analyzer
from translate import translator
from textgen import text_gen

with open('wave.css') as f:
    css = f.read()

logo = st.image('logo.jpeg', width=50)


st.markdown(f'<style>{css}</style>', unsafe_allow_html=True)

st.title("OfflineGPT")

image = st.sidebar.image("logo.jpeg", width=50)

st.sidebar.title("Sidebar Menu")

selection = st.sidebar.selectbox("Choose Model", ["Text Generation", "Summarize", "Translate", "Sentiment Analysis"])

if selection == "Text Generation":
    st.title("Text Generation")

    if "messages" not in st.session_state:
        st.session_state.messages = []
    
    for message in st.session_state.messages:
        if message["role"] == "user":
            st.text(f"You: {message['content']}")
        elif message["role"] == "assistant":
            st.write(f"ChatBot: {message['content']}")

    user_input = st.text_input("You:", "", key="user_input")

    

    col1, col2 = st.columns([11, 1])
    with col1:
        pass 
    with col2:
        if st.button("➡️", key="send_button"):
            st.session_state.messages.append({"role": "user", "content": user_input})

            simulated_response = text_gen(user_input)[0]["generated_text"]
            st.session_state.messages.append({"role": "assistant", "content": simulated_response})

# elif selection == "Summarize":
#     st.title("Summarize Page")
#     # upload pdf button
#     uploaded_file = st.file_uploader("Choose a PDF file", type="pdf")
#     if uploaded_file:
#         st.write("File uploaded successfully")

# Summarization
elif selection == "Summarize":
    st.title("Summarization")
    
    uploaded_file = st.file_uploader("Choose a PDF file", type="pdf")

    text = st.text_area("Enter text", "")
        
    if st.button("Summarize"):
        if uploaded_file:
            # Process uploaded file and generate summary (replace this with your actual processing)
            summary = "This is a simulated summary."
            response_text.empty()
            response_text.write(summary)

        else:
            response_text = summarizer(text)[0]["summary_text"]
            st.write("Summary: ", response_text)
            
elif selection == "Translate":
    st.title("Translation")

    uploaded_file = st.file_uploader("Upload the image", type="image")

    src_lang_dict = {"English": "en_XX", "Spanish": "es_XX", "French": "fr_XX"}  
    tgt_lang_dict = {"Hindi": "hi_IN", "Spanish": "es_XX", "French": "fr_XX"} 

    src_lang = st.selectbox("Choose Source Language", list(src_lang_dict.keys()))
    tgt_lang = st.selectbox("Choose Target Language", list(tgt_lang_dict.keys()))

    text = st.text_area("Enter text", "")

    if st.button("Translate", key="translate_button"):
            
        src_lang_code = src_lang_dict[src_lang]
        tgt_lang_code = tgt_lang_dict[tgt_lang]

        translated_text = translator(text, src_lang=src_lang_code, tgt_lang=tgt_lang_code)[0]['translation_text']
        st.text_area("Translated Text", value=translated_text)

elif selection == "Sentiment Analysis":
    st.title("Sentiment Analysis")
    
    text = st.text_area("Enter text", "")

    if st.button("Analyze", key="analyze_button"):

        sentiment_result = sentiment_analyzer(text)
        
        sentiment_label = sentiment_result[0]['label']
        sentiment_score = sentiment_result[0]['score']
        
        st.write(f"Sentiment: {sentiment_label}")
        st.write(f"Confidence Score: {sentiment_score}")
