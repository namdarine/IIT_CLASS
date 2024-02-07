import nltk
from nltk.corpus import brown, reuters, stopwords
import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator

stop_words = stopwords.words('english')

# 1. Obtain the word frequency distribution 
# BROWN corpora
brown_words = [word for word in brown.words() if word.lower() not in stop_words]
brown_frequencyDistribution = nltk.FreqDist(word.lower() for word in brown_words)
brown_frequenciesAndWords = dict()

for word in brown_words:
    brown_frequenciesAndWords[word] = brown_frequencyDistribution[word]

# REUTERS corpora
reuters_words = [word for word in reuters.words() if word.lower() not in stop_words]
reuters_frequencyDistribution = nltk.FreqDist(word.lower() for word in reuters_words)
reuters_frequenciesAndWords = dict()

for word in reuters_words:
    reuters_frequenciesAndWords[word] = reuters_frequencyDistribution[word]

# 2. Print top 10 words of both corpora
# BROWN corpora
brown_frequenciesAndWords = list(brown_frequenciesAndWords.items())
brown_frequenciesAndWords.sort(key = lambda a: a[1])
brown_frequenciesAndWords.reverse()

brown_labels, brown_frequencies = map(list, zip(*brown_frequenciesAndWords))

print("2. Print top 10 words for both corpora")
print("brown corpus Top 10: \n")
for index in range(10):
    print(f"{index+1:2d}. ", brown_labels[index], ' ', brown_frequencies[index])


# REUTERS corpus
reuters_frequenciesAndWords = list(reuters_frequenciesAndWords.items())
reuters_frequenciesAndWords.sort(key = lambda a: a[1])
reuters_frequenciesAndWords.reverse()

reuters_labels, reuters_frequencies = map(list, zip(*reuters_frequenciesAndWords))

print("\nreuters corpus Top 10: \n")
for index in range(10):
    print(f"{index+1:2d}. ", reuters_labels[index], ' ', reuters_frequencies[index])


# 3. Generate log(rank) vs log(frequency) plots for the first 1000 words
print("\n\n3. Generate log(rank) vs log(frequency) plots for both corpora")
# BROWN corpus
brown_labels2 = brown_labels[:1000]
brown_frequencies2 = brown_frequencies[:1000]
brown_fig, brown_ax = plt.subplots()
brown_xs = range(len(brown_labels))
brown_labels2 = range(len(brown_labels))


def format_fn(tick_val, tick_pos):
    if int(tick_val) in brown_xs:
        return brown_labels2[int(tick_val)]
    else:
        return ''


# A FuncFormatter is created automatically.
brown_ax.xaxis.set_major_formatter(format_fn)
brown_ax.xaxis.set_major_locator(MaxNLocator(integer=True))
#ax.set_yscale('log')
brown_ax.plot(brown_xs, brown_frequencies)
brown_ax.set_title('Token frequency counts in "brown" corpus ranked')
brown_ax.set_xscale('log')
brown_ax.set_yscale('log')
plt.xlabel('log(Rank)')
plt.ylabel('log(Frequency count)')
plt.show()

# REUTERS corpus
reuters_labels2 = reuters_labels[:1000]
reuters_frequencies2 = reuters_frequencies[:1000]
reuters_fig, reuters_ax = plt.subplots()
reuters_xs = range(len(reuters_labels))
reuters_labels2 = range(len(reuters_labels))


def format_fn(tick_val, tick_pos):
    if int(tick_val) in reuters_xs:
        return reuters_labels2[int(tick_val)]
    else:
        return ''


# A FuncFormatter is created automatically.
reuters_ax.xaxis.set_major_formatter(format_fn)
reuters_ax.xaxis.set_major_locator(MaxNLocator(integer=True))
#ax.set_yscale('log')
reuters_ax.plot(reuters_xs, reuters_frequencies)
reuters_ax.set_title('Token frequency counts in "reuters" corpus ranked')
reuters_ax.set_xscale('log')
reuters_ax.set_yscale('log')
plt.xlabel('log(Rank)')
plt.ylabel('log(Frequency count)')
plt.show()


# 4. Claculate the probability
# Technical word: quantum, non-technical word: fine
technical_word = 'quantum'
non_technical_word = 'fine'
# Brown
total_brown = sum(brown_frequencyDistribution.values())
brown_tech_word_count = brown_frequencyDistribution[technical_word]
brown_nonTech_word_count = brown_frequencyDistribution[non_technical_word]
brown_tech_prob = brown_tech_word_count / total_brown
brown_non_tech_prob = brown_nonTech_word_count / total_brown

print("\n", f"BROWN CORPUS:")
print(f"{technical_word} - Count: {brown_tech_word_count}, Probability: {brown_tech_prob:.7f}")
print(f"{non_technical_word} - Count: {brown_nonTech_word_count}, Probability: {brown_non_tech_prob:.7f}\n")

# REUTERS corpus
total_reuters = sum(reuters_frequencyDistribution.values())
reuter_tech_word_count = reuters_frequencyDistribution[technical_word]
reuter_nonTech_word_count = reuters_frequencyDistribution[non_technical_word]
reuter_tech_prob = reuter_tech_word_count / total_reuters
reuter_non_tech_prob = reuter_nonTech_word_count / total_reuters

print("\n", f"REUTERS CORPUS:")
print(f"{technical_word} - Count: {reuter_tech_word_count}, Probability: {reuter_tech_prob:.7f}")
print(f"{non_technical_word} - Count: {reuter_nonTech_word_count}, Probability: {reuter_non_tech_prob:.7f}\n")




