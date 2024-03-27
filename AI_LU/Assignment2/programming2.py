#--------------
# CS 481      |
# Section 01  |
# Nam Gyu Lee |
# Implement   |
#--------------

import function
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import sys

df = pd.read_csv("/Users/namgyulee/Downloads/archive/winemag-data_first150k.csv")
label = ['Chardonnay', 'Pinot Noir', 'Cabernet Sauvignon', 'Red Blend', 'Bordeaux-style Red Blend']
filtered_df = df[df['variety'].isin(label)]
filtered_df = filtered_df.reset_index(drop=True)

'''
if len(sys.argv) != 2:
        print("Usage: python cs481_P02_AXXXXXXXX.py TRAIN_SIZE")
        exit(1)

try:
    train_size = int(sys.argv[1])
    if train_size < 20 or train_size > 80:
        raise ValueError
except ValueError:
    print("TRAIN_SIZE must be a number between 20 and 80.")
    train_size = 80
'''
train_size = 80
test_size = int(len(filtered_df) * 0.2)
Train_size = int(len(filtered_df) * train_size / 100) # train_size/100
print(f"Training set size: {train_size}%\n")

train_df = filtered_df[:Train_size]
test_df = filtered_df[-test_size:]

train_des = train_df['description']
train_variety = train_df['variety']

test_des = test_df['description']
test_variety = test_df['variety']

preprocess = function.preprocess

train_des = [preprocess(doc) for doc in train_des]
test_des = [preprocess(doc) for doc in test_des]


classifier = function.naiveBayes()
classifier.train(train_des, train_variety)
print('Training classifier...')
pred_variety, pred_prob = classifier.predict(test_des)
print('Testing classifier...')


metrics = function.calculate_metrics(test_variety, pred_variety, label)

# Print metrics for each class
print('\nTest results / metrics:')
for class_label in label:
    TP = metrics[class_label]['tp']
    TN = metrics[class_label]['tn']
    FP = metrics[class_label]['fp']
    FN = metrics[class_label]['fn']
    sensitivity, specificity, precision, npv, accuracy, f_score = function.evaluate_classifier(TP, TN, FP, FN)
    
    
    print(f"\nClass {class_label}:")
    print(f"Number of true positives: {TP}")
    print(f"Number of true negative: {TN}")
    print(f"Number of false positive: {FP}")
    print(f"Number of false negative: {FN}\n")
    print(f"Sensitivity (recall): {sensitivity}")
    print(f"Specificity: {specificity}")
    print(f"Precision: {precision}")
    print(f"Negative predictive value: {npv}")
    print(f"Accuracy: {accuracy}")
    print(f"F-score: {f_score}\n")
    
    
    
macro_precision, macro_sensitivity, macro_specificity, macro_f1_score = function.macro_average(metrics)
print(f"Macro-averaged Precision: {macro_precision}")
print(f"Macro-averaged Sensitivity: {macro_sensitivity}")
print(f"Macro-averaged F1-score: {macro_f1_score}\n")
micro_precision, micro_sensitivity, micro_specificity, micro_f1_score = function.micro_average(metrics)
print(f"Micro-averaged Precision: {micro_precision}")
print(f"Micro-averaged Sensitivity: {micro_sensitivity}")
print(f"Micro-averaged F1-score: {micro_f1_score}")


# macro-ROC curve
plt.figure()
plt.plot([0, 1 - macro_specificity, 1], [0, macro_sensitivity, 1], marker='o')
plt.title(f'Macro-averaged ROC Curve with {train_size}%')
plt.xlabel('False Positive Rate')
plt.ylabel('True Positive Rate')
plt.grid(True)
plt.show()

# micro-ROC curve
plt.figure()
plt.plot([0, 1 - micro_specificity, 1], [0, micro_sensitivity, 1], marker='o')
plt.title(f'Micro-averaged ROC Curve with {train_size}%')
plt.xlabel('False Positive Rate')
plt.ylabel('True Positive Rate')
plt.grid(True)
plt.show()

# Interactive part
while True:
    sentence = input("\nEnter your sentence:\n\nSentence S:\n\n")
    pre_sentence = preprocess(sentence)
    predicted_labels, probabilities = classifier.predict([pre_sentence])
    class_label = predicted_labels[0]
    probability = probabilities[0][class_label]
    print(f"\nSentence '{sentence}' was classified as {class_label}.")
    print(f"P({class_label} | S) = {probability}")
    top_three = sorted(probabilities[0].items(), key=lambda x: x[1], reverse=True)[:4]
    for label, prob in top_three[1:]:
        print(f"P({label} | S) = {prob}")
    choice = input("\nDo you want to enter another sentence [Y/N]? ").strip().upper()
    if choice != 'Y':
        break

    




