# import streamlit as st
# import newspaper
# import nltk
# nltk.download('tokenizers/punkt/english.pickle')


# st.title("Hello there ")
# url = st.text_input("Enter URL",placeholder="paste url here ")

# if url:
#     article = newspaper.Article(url)
#     article.download()

#     article.parse()

    
#     tags = article.tags
#     st.write(','.join(tags))


   
#     st.subheader("keywords")
#     key = article.keywords
#     st.write(','.join(key))


#     article.download('punkt')
#     article.nlp()


#     tab1, tab2 = st.tabs(['Full Article','Summary'])
#     with tab1:
#         st.write(article.text)
#     with tab2:
#         st.write(article.summary)


#......................................................

# working code

# import streamlit as st
# import newspaper
# import nltk
# from nltk.tokenize import word_tokenize

# # Define the custom split_sentences function
# def split_sentences(text):
#     sentences = []
#     for sentence in word_tokenize(text):
#         sentences.append(sentence)
#     return sentences

# # Monkey patch the split_sentences function in the newspaper library
# newspaper.nlp.split_sentences = split_sentences

# st.title("Hello there ")
# url = st.text_input("Enter URL", placeholder="paste url here ")

# if url:
#     article = newspaper.Article(url)
#     article.download()
#     article.parse()

#     tags = article.tags
#     st.write(','.join(tags))

#     st.subheader("keywords")
#     key = article.keywords
#     st.write(','.join(key))

#     article.nlp()

#     tab1, tab2 = st.tabs(['Full Article', 'Summary'])
#     with tab1:
#         st.write(article.text)
#     with tab2:
#         st.write(article.summary)


#..............................................................
# best work 
# import streamlit as st
# import newspaper
# from nltk.tokenize import word_tokenize

# # Define a custom summarization function (consider using a dedicated library)
# def summarize_article(article, max_sentences=50):
#     """
#     Generates a summary of the article using word tokenization and sentence selection.

#     Args:
#         article (newspaper.Article): The article object to summarize.
#         max_sentences (int, optional): The maximum number of sentences in the summary. Defaults to 5.

#     Returns:
#         str: The generated summary of the article.
#     """

#     sentences = word_tokenize(article.text)

#     # Implement your summarization logic here (e.g., sentence scoring, keyword extraction)
#     # Example (replace with a more sophisticated approach):
#     summary_sentences = sentences[:max_sentences]  # Take the first few sentences for now

#     return ' '.join(summary_sentences)

# st.title("Hello there!")
# url = st.text_input("Enter URL", placeholder="Paste URL here ")

# if url:
#     article = newspaper.Article(url)
#     article.download()
#     article.parse()

#     tags = article.tags
#     st.write(','.join(tags))

#     st.subheader("Keywords")
#     key = article.keywords
#     st.write(','.join(key))

#     summary = summarize_article(article)
#     st.subheader("Summary")
#     st.write(summary)

#     tab1, tab2 = st.tabs(['Full Article', 'Summary'])
#     with tab1:
#         st.write(article.text)
#     with tab2:
#         st.write(summary)  # Use the generated summary here

#...........................................................

import streamlit as st
import newspaper
from nltk.tokenize import word_tokenize
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize
from collections import defaultdict

nltk.download('punkt')
nltk.download('stopwords')

def calculate_sentence_scores(sentences, frequency_table):
    sentence_scores = defaultdict(int)
    for i, sentence in enumerate(sentences):
        for word, freq in frequency_table.items():
            if word in sentence.lower():
                sentence_scores[i] += freq
    return sentence_scores

def summarize_article(article, max_sentences=5):
    """
    Generates a summary of the article using sentence scoring.

    Args:
        article (newspaper.Article): The article object to summarize.
        max_sentences (int, optional): The maximum number of sentences in the summary. Defaults to 5.

    Returns:
        str: The generated summary of the article.
    """
    stop_words = set(stopwords.words('english'))
    sentences = sent_tokenize(article.text)
    word_sent = word_tokenize(article.text.lower())
    word_frequency = defaultdict(int)
    for word in word_sent:
        if word not in stop_words:
            word_frequency[word] += 1

    sentence_scores = calculate_sentence_scores(sentences, word_frequency)
    ranked_sentences = sorted(sentence_scores, key=sentence_scores.get, reverse=True)

    summary_sentences = [sentences[i] for i in ranked_sentences[:max_sentences]]
    return ' '.join(summary_sentences)


st.title("Hello there!")
url = st.text_input("Enter URL", placeholder="Paste URL here ")

if url:
    article = newspaper.Article(url)
    article.download()
    article.parse()

    tags = article.tags
    st.write(','.join(tags))

    st.subheader("Keywords")
    key = article.keywords
    st.write(','.join(key))

    summary = summarize_article(article)
    # st.subheader("Summary")
    # st.write(summary)

    tab1, tab2 = st.tabs(['Full Article', 'Summary'])
    with tab1:
        st.write(article.text)
    with tab2:
        st.write(summary)
