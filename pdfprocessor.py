
import os
import tempfile
from langchain_community.document_loaders import PyPDFLoader
from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import FAISS
from langchain.prompts import PromptTemplate
from langchain_openai import OpenAI
from langchain.chains import create_retrieval_chain
from langchain.chains.combine_documents import create_stuff_documents_chain

def create_docs(user_pdf_list, user_query):
    extracted_answers = []

    # Load API Key securely
    open_api_key = "sk-5poPYRkEZzZMn6L7UKjKwaJtMbkwzTPsP8MMTPWkS5T3BlbkFJk2JKZYk6oduRSufbZ-y0h6mjKGBpcio_udCW5FyssA"

    if not open_api_key:
        raise ValueError("OpenAI API key is missing! Set it in your .env file.")

    # Process each uploaded file
    for uploaded_file in user_pdf_list:
        print("Processing file:", uploaded_file.name)

        # Save the uploaded PDF temporarily
        with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as temp_pdf:
            temp_pdf.write(uploaded_file.read())
            temp_pdf_path = temp_pdf.name  # Get the temp file path

        try:
            # Load and split the PDF
            loader = PyPDFLoader(temp_pdf_path)
            pages = loader.load_and_split()

            # Create embeddings and store them in FAISS vector database
            embeddings = OpenAIEmbeddings(api_key=open_api_key)
            vector_store = FAISS.from_documents(pages, embeddings)

            # Define the retrieval prompt
            template = """You are an AI assistant that extracts relevant details from a user manual.
            Based on the given context, answer the following question:
            
            {input}
            
            Context:
            {context}
            
            Provide a detailed yet concise response.
            """

            prompt = PromptTemplate.from_template(template)

            # Initialize OpenAI LLM
            llm = OpenAI(model="gpt-3.5-turbo-instruct", api_key=open_api_key)

            # Create retriever and document processing chain
            retriever = vector_store.as_retriever()
            document_chain = create_stuff_documents_chain(llm, prompt)

            # Create a retrieval-augmented generation (RAG) pipeline
            retrieval_chain = create_retrieval_chain(retriever, document_chain)

            # Query the system (context is retrieved automatically)
            response = retrieval_chain.invoke({"input": user_query})

            # Extract the answer
            extracted_answer = response.get('answer', 'No data found')
            extracted_answers.append({"filename": uploaded_file.name, "answer": extracted_answer})

            print(f"Extracted Data from {uploaded_file.name}:", extracted_answer)

        finally:
            # Remove temporary file
            os.remove(temp_pdf_path)

    return extracted_answers  # Return all extracted data















        