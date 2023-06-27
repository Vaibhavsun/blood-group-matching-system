import nltk
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

nltk.data.path.append('C:\\Users\\hp\\Desktop\\punkt')
tokenizer = nltk.data.load('english.pickle')

def read_data(filename):
    with open(filename, 'r') as file:
        data = file.read()
    return data

questions_data = read_data('questions.txt')
answers_data = read_data('answers.txt')

question_list = questions_data.split('\n')
answer_list = answers_data.split('\n')

def tokenize_data(data):
    tokenized_data = [tokenizer.tokenize(sentence.lower()) for sentence in data]
    return tokenized_data

question_tokens = tokenize_data(question_list)
answer_tokens = tokenize_data(answer_list)

def create_tfidf_vectorizer(data):
    tfidf_vectorizer = TfidfVectorizer(stop_words='english')
    tfidf_matrix = tfidf_vectorizer.fit_transform([' '.join(tokens) for tokens in data])
    return tfidf_vectorizer, tfidf_matrix

tfidf_vectorizer, tfidf_matrix = create_tfidf_vectorizer(answer_tokens)

def get_best_answer(user_input, tfidf_vectorizer, tfidf_matrix, answer_tokens):
    user_tokens = tokenizer.tokenize(user_input.lower())
    user_tfidf = tfidf_vectorizer.transform([' '.join(user_tokens)])
    similarity_scores = cosine_similarity(user_tfidf, tfidf_matrix)
    best_index = similarity_scores.argmax()
    best_answer = ' '.join(answer_tokens[best_index])
    if user_input.lower() == "what is blood":
        best_answer = "Blood is a vital fluid that circulates through our bodies and plays a crucial role in maintaining our overall health."
    return best_answer




