import string
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import CountVectorizer
from nltk.corpus import stopwords
stopwords = stopwords.words('english')


# countvectorizer converts strings to numerical vectors
# stopwords removes most common words (I, the etc)

# have sentences in list form: = ['first sentence', 'next one']

def rm_punc_stopwords(text):
    text = text.translate(str.maketrans('', '', string.punctuation))
    text = text.lower
    text = ' '.join([word for word in text.split() if word not in stopwords])
    return text


def vectorizer(clean_text):
    vectorizer = CountVectorizer().fit_transform(clean_text)
    vectors = vectorizer.toarray()
    return vectors

csim = cosine_similarity(vectors)
