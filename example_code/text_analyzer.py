import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from collections import Counter

nltk.download('punkt')
nltk.download('stopwords')

class TextAnalyzer:
    def __init__(self, text):
        self.text = text
        self.tokens = word_tokenize(self.text.lower())

    def remove_stopwords(self):
        stop_words = set(stopwords.words('english'))
        filtered_tokens = [word for word in self.tokens if word not in stop_words]
        return filtered_tokens

    def get_word_frequency(self):
        word_freq = Counter(self.tokens)
        return word_freq

    def get_most_common_words(self, n=5):
        word_freq = Counter(self.tokens)
        return word_freq.most_common(n)

# Exemple d'utilisation
text = "Natural Language Processing is a fascinating field of AI."
analyzer = TextAnalyzer(text)
print(analyzer.remove_stopwords())
print(analyzer.get_word_frequency())
print(analyzer.get_most_common_words(3))
