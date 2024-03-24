import pandas as pd
from langchain.llms import CTransformers 
from huggingface_hub import HuggingfaceEmbeddings
from langchain.vectorstores import FAISS
from langchain.prompts import PromptTemplate
from langchain.text_splitter import CharacterTextSplitter,RecursiveCharacterTextSplitter
import gradio as gd


def load_model(input,context):
    llm =CTransformers(model="llama-2-7b-chat.Q8_0.gguf",
                     model_type='llama',
                     config={
                         'max_new_tokens':256,
                         'temperature': 0.1})
    template= f"""You are a helpful AI assistant and you will summarize 
      the given data{input} based on the context{context}"""
    
    prompt=PromptTemplate(input_variables=['input','context'],
                          template=template)
    response=llm(prompt)
    print(response)
    return response


def embedding_data(data):
    text_splitter = CharacterTextSplitter(chunk_size=1000,chunk_overlap=100)
    chunk = text_splitter.split_text(data)
    embedding=HuggingfaceEmbeddings(model='llama') 
    db = FAISS.from_document(chunk)
    db.save_local("FAISS-Index")


def search(query):
    new_db=load

    