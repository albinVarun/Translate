from googletrans import Translator
import streamlit as st 

st.header("Machine Translator")

input_text=st.text_area('Enter text here.',value="")
opt=st.selectbox("To which language you wish to translate this text to",("Malayalam","Hindi","Tamil",))
if st.button("Translate"):
    translator=Translator()
    translation=translator.translate(input_text,dest=opt)
    st.write(translation.text)
    