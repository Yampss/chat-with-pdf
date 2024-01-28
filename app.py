import tempfile
# Import os to set API key
import os
# Import OpenAI as main LLM service
from langchain_openai import OpenAI
from langchain_community.document_loaders import PyPDFLoader
from langchain_openai import OpenAIEmbeddings
# from langchain_community.embeddings import OpenAIEmbedding
import streamlit as st
# Import PDF document loaders...there's other ones as well!
# from langchain_community.document_loaders import PyPDFLoader
# Import chroma as the vector store 
from langchain_community.vectorstores import Chroma
import chromadb 
# Import vector store stuff
from langchain.agents.agent_toolkits import (
    create_vectorstore_agent,
    VectorStoreToolkit,
    VectorStoreInfo
)

# Set the title and subtitle of the app
st.title('CHAT WITH YOUR PDF')
st.subheader('CONVERSE DIRECTLY WITH YOUR PDF')

# Loading the Pdf file and return a temporary path for it 
st.subheader('Upload your pdf')
uploaded_file = st.file_uploader('', type='pdf')

temp_file_path = os.getcwd()
while uploaded_file is None:
    x = 1
        
if uploaded_file is not None:
    # Save the uploaded file to a temporary location
    temp_dir = tempfile.TemporaryDirectory()
    temp_file_path = os.path.join(temp_dir.name, uploaded_file.name)
    with open(temp_file_path, "wb") as temp_file:
        temp_file.write(uploaded_file.read())

# Set APIkey for OpenAI Service
os.environ['OPENAI_API_KEY'] = 'apikey'

# Create instance of OpenAI LLM
llm = OpenAI(temperature=0.1, verbose=True)

embeddings = OpenAIEmbeddings()
# Create and load PDF Loader
loader = PyPDFLoader(temp_file_path)
# Split pages from pdf 
pages = loader.load_and_split()

# Load documents into vector database aka ChromaDB
store = Chroma.from_documents(pages, embeddings, collection_name='Pdf')

# Create vectorstore info object
vectorstore_info = VectorStoreInfo(
    name="Pdf",
    description=" A pdf file to answer your questions",
    vectorstore=store
)
# Convert the document store into a langchain toolkit
toolkit = VectorStoreToolkit(vectorstore_info=vectorstore_info)

# Add the toolkit to an end-to-end LC
agent_executor = create_vectorstore_agent(
    llm=llm,
    toolkit=toolkit,
    verbose=True
)
# Create a text input box for the user
prompt = st.text_input('Input your prompt here')
if prompt:
    # Then pass the prompt to the LLM
    response = agent_executor.run(prompt)
    # ...and write it out to the screen
    st.write(response)