import streamlit as st
import newspaper
from nltk.tokenize import word_tokenize
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize
from collections import defaultdict
from googlesearch import search

nltk.download('punkt')
nltk.download('punkt_tab')
nltk.download('stopwords')

def calculate_sentence_scores(sentences, frequency_table):
    sentence_scores = defaultdict(int)
    for i, sentence in enumerate(sentences):
        for word, freq in frequency_table.items():
            if word in sentence.lower():
                sentence_scores[i] += freq
    return sentence_scores

def summarize_article(article, max_sentences=7):
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

def get_top_websites(topic, num_results=2):
    query = topic
    websites = []
    try:
        for url in search(query, num_results=num_results):
            websites.append(url)
    except Exception as e:
        print(f"An error occurred: {e}")
    return websites

st.title("Hello there!")
topic = st.text_input("Enter topic", placeholder="Enter topic here ")

if topic:
    websites = get_top_websites(topic)
    st.write("Top websites for the topic are:")
    for idx, site in enumerate(websites, 1):
        st.write(f"{idx}. {site}")

    if websites:  # Check if the list is not empty
        article_url = websites[0]  # Use the first website as the article URL
        article = newspaper.Article(article_url)
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

        images = list(article.images)
        st.subheader("Image")
        if images:
            st.image(images[0], use_column_width=True)

        
        tab1, tab2 = st.tabs(['Full Article', 'Summary'])
        with tab1:
            st.write(article.text)
        with tab2:
            st.write(summary)
    else:
        st.write("No websites found.")
