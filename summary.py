

import requests
from bs4 import BeautifulSoup
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lsa import LsaSummarizer
from sumy.parsers.plaintext import PlaintextParser


def extract_text(url):
    """Extracts text from a given URL using Beautiful Soup.

    Args:
        url (str): The URL of the webpage to scrape.

    Returns:
        str: The extracted text from the webpage.
    """

    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    # Extract all text from the page (consider handling non-text content)
    text = soup.get_text(separator='\n')  # Preserve line breaks for better summarization

    # Remove extra whitespace and newlines (adjust based on your needs)
    text = ' '.join(text.split())

    return text


def summarize_text(text):
    """Summarizes the given text using Sumy's LSA summarizer.

    Args:
        text (str): The text to be summarized.

    Returns:
        list: A list of strings representing the summary sentences.
    """

    parser = PlaintextParser.from_string(text, Tokenizer("english"))
    summarizer = LsaSummarizer()
    summary = summarizer(parser.document, sentences_count=3)  # Adjust the number of sentences

    return [str(sentence) for sentence in summary]  # Convert summary objects to strings


if __name__ == "__main__":
    url = input("Enter the website URL: ")

    # Extract text from the URL
    extracted_text = extract_text(url)
    print("\nExtracted Text:\n")
    print(extracted_text)

    # Summarize the extracted text
    summary = summarize_text(extracted_text)
    print("\nSummary:\n")
    for sentence in summary:
        print(sentence)
