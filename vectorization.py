from sklearn.feature_extraction.text import CountVectorizer
import numpy as np

def vectorize_sentences(sentence1, sentence2):
    vectorizer = CountVectorizer()

    # Gộp hai câu nhập vào thành một list
    sentences = [sentence1, sentence2]

    vectorized_sentences = vectorizer.fit_transform(sentences)

    vectorized_sentences = vectorized_sentences.toarray()

    return vectorized_sentences[0], vectorized_sentences[1]

# Gọi hàm vectorize_sentences để vector hóa hai câu nhập
# sentence1 = "Tôi cần tìm thông tin về thời tiết ngày hôm nay"
# sentence2 = "Tôi cần tìm bản tin về thời tiết ngày mai"
sentence1 = input("Nhập vào câu thứ nhất: ")
sentence2 = input("Nhập vào câu thứ hai: ")
vector1, vector2 = vectorize_sentences(sentence1, sentence2)

print("Vector hóa của câu 1:", vector1)
print("Vector hóa của câu 2:", vector2)


def cosine_similarity(vector1, vector2):
    # Tính độ dài của các vector hóa
    norm_vector1 = np.linalg.norm(vector1)
    norm_vector2 = np.linalg.norm(vector2)

    # Tính tích vô hướng của hai vector hóa
    dot_product = np.dot(vector1, vector2)

    # Tính độ tương đồng giữa hai vector hóa sử dụng độ đo cosin
    cosine_sim = dot_product / (norm_vector1 * norm_vector2)

    return cosine_sim

# Gọi hàm cosine_similarity để tính độ tương đồng giữa hai vector hóa
similarity = cosine_similarity(vector1, vector2)

# In ra độ tương đồng giữa hai câu nhập
print("Độ tương đồng giữa hai câu là:", similarity)
