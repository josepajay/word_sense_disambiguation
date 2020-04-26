#!/usr/bin/env python3
import argparse

def preprocess(word, data_type):
    f1 = open("datasets/" + word + "/" + data_type + ".data.txt", "r")
    f2 = open("datasets/" + word + "/" + data_type + ".gold.txt", "r")

    f3 = open("datasets/" + word + "/" + word + "_" + data_type + ".txt", "w")

    train_data_arr = f1.readlines()
    train_label_data_arr = f2.readlines()

    f1.close()
    f2.close()
    for i, value in enumerate(train_data_arr):
        sentence = value.split("\t")[1]
        constructed_sentence = "__label__" + train_label_data_arr[i].split("\n")[0] + " " + sentence
        f3.write(constructed_sentence)

    f3.close()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Display confusion matrix.')
    parser.add_argument('word', help='word to process')
    parser.add_argument('data_type', help='type of data file (train or test)')
    args = parser.parse_args()
    preprocess(args.word, args.data_type)
