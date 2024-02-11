import nltk
from nltk.corpus import brown, stopwords
from nltk import bigrams

stop_words = stopwords.words('english')
brown_words = [word.lower() for word in brown.words() if word.lower() not in stop_words]

def next_words(W1):
    
    bigrams_list = list(bigrams(brown_words))
    user_bigrams = [(prev, predict) for prev, predict in bigrams_list if prev == W1]
    user_bigrams = nltk.FreqDist(user_bigrams)
    user_freq = dict()
    
    for word in user_bigrams:
        user_freq[word] = user_bigrams[word]
    
    user_freq = list(user_freq.items())
    user_freq.sort(key = lambda x: (-x[1], x[0]))
    #user_freq.reverse()
    
    top3_bigrams = user_freq[:3]
    
    word_freq = nltk.FreqDist(brown_words)
    W1_freq = word_freq[W1]
    
    bigram_freq = {(bigram[0][0], bigram[0][1]): bigram[1] / W1_freq for bigram in top3_bigrams}
    bigram_freq = list(bigram_freq.items())
    
    return bigram_freq


def make_sentence():
    
    W1 = input("Enter your word: ")
    W1 = W1.lower()
    
    q = False

    
    while W1 not in brown_words:
        print("Word not found, please: ")
        print("1. Try again")
        print("2. Quit")
        new = input("\nEnter your choice: ")
        if new == "1":
            W1 = input("\nEnter your new word: ")
            next_words(W1)
        elif new == "2":
            q = True
            return "User chose to quit."
            break
        else:
            print("Invalid choice.")
    

    sentence = [W1]
    while q == False:
            
        words = next_words(W1)
    
        print(f"\n{sentence}")
        print(f"{W1} ... ")
        print("Which word should follow: ")
        for i, (word, prob) in enumerate(words):
            print(f"{i+1}) {word[1]}   P({W1} {word[1]}) = {prob: .5f}")
        print("4) QUIT")
    
        choice = int(input("\nEnter your choice: "))
    
        if choice == 4:
            " ".join(sentence)
            
            break
    
        try:
            if 1 <= choice <= 3:
                next_word = words[choice - 1][0][1]
                sentence.append(next_word)
                W1 = next_word
                next_words(W1)
            elif choice > 4:
                print("You pick a number other than 1, 2, 3, so assume your choice is 1.")
                next_word = words[0][0][1]
                sentence.append(next_word)
                W1 = next_word
                next_words(W1)

        except ValueError:
            print("Invalid choice. Please choose again.")
    return " ".join(sentence)


sen = make_sentence()
print(f"\nGenerated sentence: {sen}")

            
        
