import pandas as pd 
import numpy as np
print(1)
from train_process import SentenceGetter 
print(2)
import matplotlib.pyplot as plt
from keras.preprocessing.text import Tokenizer
from keras.models import load_model
print(3)
from word_vec import embeddings
print(4)
from predicter import extract
print(5)
import os
from imagedownloader import downloader as Downloader
print(6)
cwd = os.getcwd()
embeds = embeddings(cwd+'/narration/datasets/glove.6B.50d.txt')
model2 = load_model(cwd+'/narration/saved_model/model.h5')
model2._make_predict_function()


def imager(text):
    print('imager started')
    keywords = np.array(extract(model2 , text , embeds))
    indexes = np.unique(keywords, return_index=True)[1]
    keywords = [keywords[index] for index in sorted(indexes)]
    print(keywords)
    downloader1  = Downloader()
    names = {}
    for i in keywords:
        names[i] = downloader1.download(i)
    print('imager over in main')
    return names