# Blog Generation and RAG Using llama-2

This repository contains the code for a blog generation application using the llama-2 model, with a user interface built in Streamlit, and a Retrieval-Augmented Generation (RAG) system.

## Overview

The project is divided into two main components:
- `app.py`: The Streamlit-based UI for users to interact with the blog generation model.
- `rag.py`: The script that implements the RAG system using the llama-2 model to augment the blog generation process with relevant information retrieval.

## Features

- **Interactive Blog Generation**: Use `app.py` to start an interactive session where you can input topics and get blog posts generated on-the-fly.
- **Retrieval-Augmented Generation**: Enhance the blog generation with the `rag.py` script, which retrieves information to provide contextually rich content.

## Getting Started

To run the blog generation application:

1. Clone the repository:
   ```bash
   git clone https://github.com/imanoop7/BlogGeneration_and_RAG_Using_llama-2.git
2. Install the required dependencies:
   ``` bash
   pip install -r requirements.txt
3. Start the Streamlit app:
   ``` bash
   streamlit run app.py
4. For RAG, run the rag.py script separately to augment the blog generation process.
Prerequisites
Python 3.6+
Streamlit
Llama-2 model access
## Contributing
Contributions are welcome! If you have ideas for improvements or new features, please fork the repository and create a pull request, or open an issue with your suggestions.

## License
This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgements
The developers of the llama-2 model for their contributions to the field of natural language processing.
The Streamlit community for providing an excellent platform for building interactive web applications.
## Support
If you find this project helpful, please consider giving it a star on GitHub. Your support helps us maintain and improve the project.
