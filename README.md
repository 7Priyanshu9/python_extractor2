# Article Summarizer and Information Retriever

## Overview

This project provides a web application built with Streamlit that allows users to enter a topic and receive a summary of a relevant article, as well as images related to the topic. It uses various libraries to search for articles, process and summarize them, and fetch images from Wikipedia.

## Features

- **Search for Relevant Websites**: Fetches top websites related to a given topic using Google search.
- **Article Extraction**: Downloads and parses the article from the first website in the search results.
- **Article Summary**: Summarizes the article content into a brief summary using NLTK for natural language processing.
- **Wikipedia Images**: Retrieves and displays an image related to the topic from Wikipedia, if available.

## Libraries Used

- `streamlit`: For creating the web application interface.
- `newspaper3k`: For extracting and parsing the article content.
- `nltk`: For natural language processing tasks such as tokenization and stopword removal.
- `googlesearch-python`: For performing Google searches.
- `wikipedia`: For fetching images from Wikipedia.

## Installation

To run this application, you need to have Python installed on your system. You can install the required libraries using pip:

# Bash commands
pip install streamlit newspaper3k nltk googlesearch-python wikipedia

# Install these initially to avoid any errors while deployment 
import nltk
nltk.download('punkt')
nltk.download('stopwords')

# Usage
Run the Streamlit App:
Open a terminal and run the following command in the directory where your script is located:

# bash
Copy code
streamlit run app.py
Enter a Topic:

Open the web application in your browser (usually at http://localhost:8501).
Enter a topic in the input box and press Enter.
View Results:

Top Websites: View a list of top websites related to the entered topic.
Article Content: Read the full text of the article from the first website.
Article Summary: View a summarized version of the article.
Wikipedia Image: See an image related to the topic retrieved from Wikipedia, if available.
Code Explanation
Imports: The necessary libraries are imported for various functionalities.
calculate_sentence_scores: Calculates the score for each sentence based on word frequencies.
summarize_article: Summarizes the article content by selecting the most important sentences.
get_top_websites: Retrieves the top websites related to the topic.
get_wikipedia_image: Fetches an image related to the topic from Wikipedia.
Streamlit App:
Takes user input for the topic.
Displays top websites and their content.
Shows the summary of the article.
Displays an image from Wikipedia.
Contributing
Feel free to fork the repository and submit pull requests. Issues and feature requests are also welcome.
