import streamlit as st
from gtts import gTTS

st.title("Text to Speech")

text = st.text_area("Enter text:")

uploaded_file = st.file_uploader("Or upload a text file", type=['txt'])

if st.button("Generate Speech"):
    input_text = ""
    if uploaded_file is not None:
        input_text = uploaded_file.read().decode('utf-8')
    else:
        input_text = text
    
    if input_text.strip():
        speech = gTTS(text=input_text, lang='en', slow=False)
        speech.save("voice.mp3")
        st.audio("voice.mp3")
        with open("voice.mp3", "rb") as f:
            st.download_button("Download MP3", f, "voice.mp3")
        st.success("Speech generated!")
    else:
        st.error("Please enter some text or upload a file.")