import streamlit as st
from dotenv import load_dotenv
import pdfprocessor as iu
import io


def main():
    load_dotenv()

    # Streamlit setup
    st.set_page_config(page_title="Invoice Extraction Bot")
    st.title("PDF Comunication Bot")
    st.subheader("I can help you in extracting data")
    
    # Upload the invoices (PDF files)
    user_query = st.text_area("Enter your query (e.g., 'Extract Summary')", "")

    pdf_files = st.file_uploader("Upload Data here, only PDF files allowed", type=["pdf"], accept_multiple_files=True)

    submit = st.button("Extract Data")
    if submit:
        if not pdf_files:
            st.warning("Please upload at least one PDF file.")
        elif not user_query.strip():
            st.warning("Please enter a query.")
        else:
            with st.spinner('Processing...'):
                extracted_data = iu.create_docs(pdf_files, user_query)
                st.write(extracted_data)

            st.success("Extraction completed successfully!")
    
if __name__ == '__main__':
    main()
