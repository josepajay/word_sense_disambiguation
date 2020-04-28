import argparse
import numpy as np
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score, precision_recall_fscore_support
from sklearn.metrics import mean_squared_error
from math import sqrt

def parse_labels(path):
    f1= open(path,"r")
    data = f1.read().splitlines()
    return np.array(data, dtype=np.float64)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Display confusion matrix.')
    parser.add_argument('word', help='word results to analyse')
    args = parser.parse_args()
    test_file = "datasets/" + args.word + "/test.gold.txt"
    prediction_file = "datasets/" + args.word + "/" + args.word + "_predicted_sanitized"
    test_labels = parse_labels(test_file)
    pred_labels = parse_labels(prediction_file)
    print(confusion_matrix(test_labels, pred_labels))
    accuracy = accuracy_score(test_labels, pred_labels)
    precision, recall, fscore, support = precision_recall_fscore_support(test_labels, pred_labels, average='macro')
    rmse = sqrt(mean_squared_error(test_labels, pred_labels))
    print("Accuracy:", accuracy)
    print("Precision:", precision)
    print("Recall:", recall)
    print("fscore:", fscore)
    print("RMSE:", rmse)
