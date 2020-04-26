# Word Sense Disambiguation dataset

Each folder corresponds to an ambiguous word (e.g. apple). Their different senses are mapped in the classes_map.txt file (each sense corresponds to a Wikipedia page). Then, each data file (tab-separated) contains the position of the ambiguous word in the sentence and the sentence. Finally, the gold files correspond to the correct sense according to the class map file.

Note: All sentences have been already preprocessed (lowercased and tokenized).

# FastText
fastText is a library for efficient learning of word representations and sentence classification.
fastText command line tool has been build and is included in this project. FastText contents can be seen in folder `fastText/`

# Requirements / Assumptions
* This codebase expects contents of this zip folder to be in datasets folder. For example folder apple should be available at `datasets/`. Same the case for all other words.
* Scripts run in this project are performance intensive and expects to have a system with atleast 8 gigabytes of memory.
* If using pretrained vectors option, the word embeddings should be downloaded from https://dl.fbaipublicfiles.com/fasttext/vectors-crawl/cc.en.300.vec.gz and placed at path
`pretrained_vectors/cc.en.300.vec/cc.en.300.vec`
* Users are free to use different word embeddings according to their requirements. Please tweak code in `preprocess_train_predict.sh` accordingly


# Usage
* Update the permissions of files `preprocess_train_predict.sh` , `sanitize_predicted_data.py`, `preprocess.py` and any other files which causes insufficient permissions to execute by command
`chmod +x`

* To train a model using training dataset without using pretrained vectors use command
  ` ./preprocess_train_predict.sh <word> <epoch_value> `
example `./preprocess_train_predict.sh apple 25`

* To train a model using training dataset along with pretrained vectors use command
`./preprocess_train_predict.sh <word> <epoch> use_word_embeddings`
example `./preprocess_train_predict.sh apple 25 use_word_embeddings`

* Once the data is preprocessed, model is trained and predictions are done, run command
`pipenv run python analyse_predictions.py <word>` to view the various metrics of the predicted labels for the test data.
example `pipenv run python analyse_predictions.py apple`

# Output example

[[619  15]  
 [ 23 375]]  
Accuracy: 0.9631782945736435  
Precision: 0.962856458183561  
Recall: 0.9592758746413456  
fscore: 0.9609980427414351  
