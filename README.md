

# PDF-Chat: Interact with Your PDFs in a Conversational Way

## Overview

PDF-Chat is a web application that allows users to upload PDF documents, ask questions, and receive answers directly from the document. The project integrates language models (LLMs) and vector stores to provide a conversational interface for interacting with PDF content.

## Features

- Upload PDFs: Users can upload PDF documents using the provided file uploader.
- Conversational Interface: Users can input prompts or questions in a text box to interact with the document.
- OpenAI Integration: The project utilizes the OpenAI language model to generate responses.
- Vector Store: PDF pages are processed and associated with embeddings in a vector store (Chroma), enabling efficient document retrieval.

## Getting Started

### Prerequisites

- Python 3.x
- Install dependencies

### Setup

1. Clone the repository: `git clone https://github.com/your-username/app.git`
2. Navigate to the project directory: `cd app`
3. Install dependencies

### Usage

1. Run the application: `streamlit run app.py`
2. Access the application in your web browser at `http://localhost:8501`

## Project Structure

- `app.py`: Main Streamlit application code.
- `langchain_openai.py`: Module for interacting with the OpenAI language model.
- `vectorstore_tools.py`: Module for vector store-related functionalities.
- ...

## Configuration

- Set your OpenAI API key in the environment variable: `export OPENAI_API_KEY=your_api_key`

## Contributing

If you would like to contribute to the project, please follow our [contribution guidelines](CONTRIBUTING.md).

## License

This project is licensed under the [MIT License](LICENSE).

 

---

Note: Be sure to replace placeholders like `your-username` and `your_api_key` with actual values. Additionally, include relevant sections such as "Deployment," "Testing," or "Troubleshooting" based on your project's needs.
