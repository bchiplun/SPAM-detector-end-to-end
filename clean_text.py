import nltk
import re
from nltk.corpus import stopwords
nltk.download('stopwords')
from nltk.stem.porter import PorterStemmer

def clean_mesaage(message):

    message = re.sub(pattern='[^A-Za-z]', repl=' ',  string=message.lower())

    words = message.split()

    words = [word for word in words if word not in set(stopwords.words('english'))]

    ps = PorterStemmer()

    words = [ps.stem(word) for word in words]

    # Joining the stemmed words
    message = ' '.join(words)

    return message