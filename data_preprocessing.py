import re
import string
# 1st data preprocessing
def data_preprocessing_1():
    input_file = r"./data/tran_cong_trung.txt"
    output_file = "./data/tran_cong_trung_1.txt"

    with open(input_file, 'r', encoding='utf-8') as f:
        data = f.read()

    sentences = data.split('.')
    sentences = [s.strip() + '.' for s in sentences if s.strip()]
    sentences = [s[:-1] for s in sentences]
    sentences = [s.translate(str.maketrans('', '', string.punctuation)) for s in sentences]
    

    with open(output_file, 'w', encoding='utf-8') as f:
        for sentence in sentences:
            sentence = sentence.strip() # Loại bỏ khoảng trắng thừa
            if sentence != '':
                f.write(sentence + '\n')

    print("Tiền xử lý dữ liệu lưu vào file mới:", output_file)



# 2nd data preprocessing
def data_preprocessing_2():
    input_file = "./data/tran_cong_trung_1.txt"
    output_file = "./data/tran_cong_trung_2.txt"
    with open(input_file, 'r', encoding='utf-8') as f:
        data = f.read()

    words = data.split()

    with open(output_file, 'w', encoding='utf-8') as f:
        for word in words:
            f.write(word + '\n')

    print("Bộ từ vựng lưu vào file mới thành công:", output_file)

data_preprocessing_1()
data_preprocessing_2()