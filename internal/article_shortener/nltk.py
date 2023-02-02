import nltk
from nltk.tokenize import sent_tokenize
from nltk.probability import FreqDist
nltk.download('punkt')

def shorten_article_v1(article_text:str, num_sentences_ret: int) -> str:
    # Tokenize the text into sentences
    sentences = sent_tokenize(article_text)
    
    # Calculate the frequency of each word in the text
    words = [word.lower() for sentence in sentences for word in nltk.word_tokenize(sentence)]
    freq_dist = FreqDist(words)
    
    # Score each sentence based on the frequency of its words
    sentence_scores = [(sentence, sum([freq_dist[word.lower()] for word in nltk.word_tokenize(sentence)])) for sentence in sentences]
    
    # Select the highest-scoring sentences to form the summary
    sorted_sentences = sorted(sentence_scores, key=lambda x: x[1], reverse=True)
    summary_sentences = [sentence for sentence, score in sorted_sentences[:num_sentences_ret]]
    
    # Combine the selected sentences to form the final summary
    summary = ' '.join(summary_sentences)
    
    return summary

