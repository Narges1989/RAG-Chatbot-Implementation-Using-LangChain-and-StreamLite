# Retrieval-Augmented Generation (RAG) for PDF Processing

## Overview
Retrieval-Augmented Generation (RAG) is a powerful approach that combines the strengths of information retrieval and generative AI models to enhance response accuracy and contextual understanding. Unlike traditional language models that rely solely on pre-trained knowledge, RAG dynamically retrieves relevant information from external sources, such as databases, documents, or APIs, before generating a response.

This method is particularly useful in scenarios where up-to-date, domain-specific, or factual accuracy is required, such as customer support, research assistance, and knowledge-based applications. By integrating retrieval with generation, RAG enables AI systems to provide more informed, context-aware, and precise answers, reducing hallucinations and improving reliability.

This repository includes two Python files:
- **`pdfprocessor.py`** – Handles PDF processing and integrates OpenAI's API for intelligent retrieval.
- **`ui_rag.py`** – Provides a user interface for document-based question-answering using Streamlit.

## Prerequisites

Before setting up the project, ensure you have the following:

- Python installed (recommended version: 3.8+)
- OpenAI API key (requires an account at [OpenAI](https://openai.com/))
- Required dependencies installed

## Setup Instructions

### 1. Obtain an OpenAI API Key
- Sign up at [OpenAI](https://openai.com/) and generate an API key.
- A **$5 subscription** is sufficient for student use cases and provides access for a year.

### 2. Configure the API Key
- Open the `pdfprocessor.py` file.
- Add your OpenAI API key in the designated section.

### 3. Install Dependencies
Ensure you have all necessary packages installed by running:

```bash
pip install -r requirements.txt

To start the Streamlit app, execute the following command in your terminal:
**streamlit run .\ui_rag.py**

Once executed, the application will launch automatically. Open the following URL in your browser:

**http://localhost:8501/**



