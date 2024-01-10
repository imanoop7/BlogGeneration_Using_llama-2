from langchain.prompts import PromptTemplate
import streamlit as st
from langchain.llms import CTransformers


#loading model
def load_llama(input_data):
    pipe = CTransformers(model="llama-2-7b-chat.Q8_0.gguf",
                     model_type='llama',
                     config={
                         'max_new_tokens':256,
                         'temperature': 0.1})
 

    template="""write a blog for topic {input_data}."""
    prompt=PromptTemplate(input_variables=['input_data'],
                          template=template)
    response=pipe(prompt.format(input_data=input_data))
    print(response)
    return response
    





st.set_page_config(page_title="Blog",
                   page_icon='',
                   layout="centered",
                   initial_sidebar_state='collapsed')

st.header("Generate Bolgs")

input_data = st.text_input("Enter name of the Topic")

submit=st.button("Generate")

if submit:
    st.write(load_llama(input_data))




