import read_input_file as rd
import constants as c
import train
import runpy
import os

from utils import create_input_files, train_word2vec_model


if __name__ == '__main__':
    #train = rd.read_input_file(c.TRAIN_PATH, c.EMOTION_HEADER, c.ATTRIBUTES, c.CLEAN)
    #test = rd.read_input_file(c.TEST_PATH, c.EMOTION_HEADER, c.ATTRIBUTES, c.CLEAN)
    train = pd.read_csv("./data/nlp_train.csv")
    test = pd.read_csv("./data/nlp_test.csv")
    train = train.dropna()
    test = test.dropna()
    train_temp = train.loc[:, ['anger', 'body']]
    test_temp = test.loc[:, ['anger', 'body']]

    train_temp.to_csv('./data/train.csv', index=False, header=False)
    test_temp.to_csv('./data/test.csv', index=False, header=False)

    create_input_files(csv_folder='./data',
                       output_folder='./outdata',
                       # sentence_limit=15,
                       # word_limit=20,
                       # min_word_count=5)
                       sentence_limit=30,
                       word_limit=100,
                       min_word_count=10)

    train_word2vec_model(data_folder='./outdata', algorithm='skipgram')
    file1 = open("label.txt", "a")
    file2 = open("result.txt", "a")
    file2.close()

    for i in c.LABELS:
        print(i)
        file1.write(i)
        file1.write('\n')
        os.system('python3 train.py')
        os.system('python3 eval.py')

    file1.close()

