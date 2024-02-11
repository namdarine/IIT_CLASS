import nltk
from nltk.corpus import brown
from nltk.tokenize import word_tokenize
from nltk import bigrams

def bigram_prob(sentence):

    words = list(word_tokenize(sentence.lower()))
    words = ["<s>"] + words + ["<s>"]
    
    bigram = list(nltk.ngrams(words, 2))

    brown_words = [word.lower() for word in brown.words()]
    frequencyDistribution = nltk.FreqDist(word.lower() for word in brown_words)
    
    start_prob = 0.25
    total_prob = 1.00
    bigram_word_prob = []
    
    for i in range(0, len(bigram)):
        
        bigram_freq = list(bigrams(brown_words)).count(bigram[i])
        word_freq = frequencyDistribution[bigram[i][0]]
        
        if bigram_freq:
            bigram_prob = bigram_freq / word_freq
        
        else:
            if i == 0:
                bigram_prob = start_prob
                
            elif i == (len(bigram) - 1):
                bigram_prob = start_prob
            
            else:
                bigram_prob = bigram_freq / word_freq
        
        total_prob *= bigram_prob
        bigram_word_prob.append((bigram[i], bigram_prob))
    
    return sentence, bigram_word_prob, total_prob
        
    

s = input("Type your sentence:")
bigram = bigram_prob(s)

print("\nYour sentence is: ", bigram[0])
print("\nBigrams and Probability")

for word, prob in bigram[1]:
    print(f"{word} : {prob:.8f}")

print("\nP(s) = ", bigram[2])
