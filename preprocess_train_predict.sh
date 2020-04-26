#!/bin/bash
WORD=$1
EPOCH=$2
WORD_EMBEDDINGS_FLAG=$3
WORD_EMBEDDINGS_REAL_FLAG="use_word_embeddings"
echo Preprocessing dataset...
./preprocess.py $WORD train
./preprocess.py $WORD test
PROCESSED_TRAIN_DATA="datasets/${WORD}/${WORD}_train.txt"
PROCESSED_TEST_DATA="datasets/${WORD}/${WORD}_test.txt"
PREDICTED_LABELS="datasets/${WORD}/${WORD}_predicted"
MODEL_OUTPUT="datasets/${WORD}/model_${WORD}"
MODEL_NAME="datasets/${WORD}/model_${WORD}.bin"
# PRETRAINED_VECTORS="pretrained_vectors/glove.twitter.27B/glove.twitter.27B.50d.vec"
PRETRAINED_VECTORS="pretrained_vectors/cc.en.300.vec/cc.en.300.vec"

if [ "$WORD_EMBEDDINGS_FLAG" = "$WORD_EMBEDDINGS_REAL_FLAG" ]; then
./fastText/fasttext supervised -input $PROCESSED_TRAIN_DATA -output $MODEL_OUTPUT -epoch $EPOCH -pretrainedVectors $PRETRAINED_VECTORS -loss hs -dim 300
else
  ./fastText/fasttext supervised -input $PROCESSED_TRAIN_DATA -output $MODEL_OUTPUT -epoch $EPOCH
fi

./fastText/fasttext predict $MODEL_NAME $PROCESSED_TEST_DATA > $PREDICTED_LABELS
./sanitize_predicted_data.py $WORD
