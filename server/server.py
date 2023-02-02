from flask import Flask, request
from internal.article_shortener import nltk

app = Flask(__name__)

@app.route('/api/article/shorten/v1', methods=['POST'])
def shorten_article_v1():
    data = request.get_json()
    article = data["article"]
    num_of_sentences = data["number_of_sentences"]

    return nltk.shorten_article_v1(article_text=article, num_sentences_ret=num_of_sentences)


