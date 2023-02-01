#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from wordcloud import WordCloud
import matplotlib.pyplot as plt

def computeTF(wordDict, bagOfWords):
    tfDict = {}
    bagOfWordsCount = len(bagOfWords)
    for word, count in wordDict.items():
        tfDict[word] = count / float(bagOfWordsCount)
    return tfDict
  
def computeIDF(documents):
    import math
    N = len(documents)
    
    idfDict = dict.fromkeys(documents[0].keys(), 0)
    for document in documents:
        for word, val in document.items():
            if val > 0:
                idfDict[word] += 1
    
    for word, val in idfDict.items():
        idfDict[word] = math.log(N / float(val))
    return idfDict

def computeTFIDF(tfBagOfWords, idfs):
    tfidf = {}
    for word, val in tfBagOfWords.items():
        tfidf[word] = val * idfs[word]
    return tfidf

def wordclouder(authorname, weight):
    # create a dummy string
    wast = weight[authorname].nlargest(100)
    text2 = ''
    for i in range(len(wast)):
        text2 = text2 +  (wast.index[i] + ' ') * int(wast[i]*10000)

    # Creating word_cloud with text as argument in .generate() method
    word_cloud2 = WordCloud(collocations = False, background_color = 'white').generate(text2)

    # Display the generated Word Cloud
    plt.imshow(word_cloud2, interpolation='bilinear')
    plt.axis("off")
    plt.show()

