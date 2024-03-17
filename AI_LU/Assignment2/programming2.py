#--------------
# CS 481      |
# Section 01  |
# Nam Gyu Lee |
# Implement   |
#--------------

import function
import pandas as pd
import sys

df = pd.read_csv("/Users/namgyulee/Downloads/archive/winemag-data_first150k.csv")

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

test_size = int(len(df) * 0.2)

print(f"Training set size: {train_size}%")

train_df = df[:train_size]
test_df = df[-test_size:]

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
pred_variety = classifier.predict(test_des)
print('Testing classifier...')

label = ['Chardonnay', 'Pinot Noir', 'Cabernet Sauvignon', 'Others']

metrics = function.calculate_metrics(test_variety, pred_variety, label)

# Print metrics for each class
for class_label in label:
    TP = metrics[class_label]['tp']
    TN = metrics[class_label]['tn']
    FP = metrics[class_label]['fp']
    FN = metrics[class_label]['fn']
    sensitivity, specificity, precision, npv, accuracy, f_score = function.evaluate_classifier(TP, TN, FP, FN)
    print(f"Class {class_label}:")
    print(f"True Positive: {TP}")
    print(f"True Negative: {TN}")
    print(f"False Positive: {FP}")
    print(f"False Negative: {FN}\n")
    print(f"Sensitivity: {sensitivity}")
    print(f"Specificity: {specificity}")
    print(f"Precision: {precision}")
    print(f"NPV: {npv}")
    print(f"Accuracy: {accuracy}")
    print(f"F-score: {f_score}\n")
    
    
# Interactive part
while True:
    sentence = input("\nEnter your sentence:\n\nSentence S:\n\n")
    pre_sentence = preprocess(sentence)
    class_label, probabilities = classifier.predict(pre_sentence)
    print(f"\nSentence '{sentence}' was classified as {class_label}.")
    print(f"P({class_label} | S) = {probabilities[class_label]}")
    top_three = sorted(probabilities.items(), key=lambda x: x[1], reverse=True)[:4]
    for label, prob in top_three[1:]:  # 첫 번째 클래스는 제외
        print(f"P({label} | S) = {prob}")
    choice = input("\nDo you want to enter another sentence [Y/N]? ").strip().upper()
    if choice != 'Y':
        break


    




