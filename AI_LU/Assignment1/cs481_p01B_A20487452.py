import nltk
from nltk.corpus import brown, stopwords

def bigram_prob(sentence):
    stop_words = stopwords.words('english')
    sentence = sentence.lower()
    
    brown_words = [word for word in brown.words() if word.lower() not in stop_words]
    frequencyDistribution = nltk.FreqDist(word.lower() for word in brown_words)
    total_freq = sum(frequencyDistribution.values())
    
    start_prob = 0.25
    total_prob = 1.00
    bigram_word_prob = []
    bigram = list(nltk.ngrams(sentence.split(), 2))
    
    for i in range(0, len(bigram)):
        sentence_freq = frequencyDistribution[bigram[i]]
        
        
        if sentence_freq:
            bigram_prob = sentence_freq / total_freq
        
        else:
            if i == 1:
                bigram_prob = start_prob
            
            else:
                bigram_prob = start_prob
        
        total_prob *= bigram_prob
        bigram_word_prob.append((bigram[i], bigram_prob))
    
    return sentence, bigram_word_prob, total_prob
        
    

s = input("Type your sentence:")
bigram = bigram_prob(s)

print("\nYour sentence is: ", bigram[0])
print("\nBigrams and Probability")
#print(bigram[1])
for word, prob in bigram[1]:
    print(f"{word} : {prob:.6f}")

print("\nP(s) = ", bigram[2])
