#!/usr/bin/env python3
import argparse

def sanitize(word):
    f1 = open("datasets/" + word + "/" + word + "_predicted", "r")
    f2 = open("datasets/" + word + "/" + word + "_predicted_sanitized", "w")
    predicted_data_arr = f1.readlines()
    f1.close()

    for i, value in enumerate(predicted_data_arr):
        # sentence = "__label__" + value.split(" ")[0] + "\n"
        sentence = value.split("\n")[0][-1] + "\n"
        f2.write(sentence)

    f2.close()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Display confusion matrix.')
    parser.add_argument('word', help='word to process')
    args = parser.parse_args()
    sanitize(args.word)
