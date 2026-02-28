import streamlit as st
from deep_translator import GoogleTranslator

# UI Heading
st.title("CodeAlpha Language Translation Tool")
st.write("Reliable translation using Python 3.13 compatibility.")

# 1. Text Input Field
user_text = st.text_area("Enter text to translate:", placeholder="Type here...", height=150)

# 2. Language Selection
# Get list of supported languages
langs_dict = GoogleTranslator().get_supported_languages(as_dict=True)
lang_names = list(langs_dict.keys())

col1, col2 = st.columns(2)
with col1:
    source_lang = st.selectbox("From (Source Language):", ["auto"] + lang_names)
with col2:
    target_lang = st.selectbox("To (Target Language):", lang_names, index=lang_names.index("english"))

# 3. Processing and API Call
if st.button("Translate"):
    if user_text.strip():
        try:
            # Initialize translator
            translated = GoogleTranslator(source=source_lang, target=target_lang).translate(user_text)
            
            # 4. Display Translated Text
            st.success(f"Translation ({target_lang}):")
            st.write(translated)
            
            # Optional: Copy Button (Markdown/Code block)
            st.info("Copy the translation below:")
            st.code(translated, language=None)
            
        except Exception as e:
            st.error(f"Error: {e}. Check your internet connection.")
    else:
        st.warning("Please enter text first.")
        

        