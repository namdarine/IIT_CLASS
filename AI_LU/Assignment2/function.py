#--------------
# CS 481      |
# Section 01  |
# Nam Gyu Lee |
# Functions   |
#--------------

import sys
import re
import math

class naiveBayes:
    def __init__(self):
        self.class_counts = {}
        self.word_counts = {}
        self.total_documents = 0
        self.vocabulary = set()

    def train(self, x, y):
        self.total_documents = len(x)
        for doc, label in zip(x, y):
            if label not in self.word_counts:
                self.word_counts[label] = []
            self.class_counts[label] = self.class_counts.get(label, 0) + 1
            for word in doc.split():
                self.word_counts[(word, label)] = self.word_counts.get((word, label), 0) + 1
                self.vocabulary.add(word)
    
    def predict(self, x):
        scores = {}
        for label in self.class_counts.keys():
            score = math.log(self.class_counts[label] / self.total_documents)
            for word in x:
                count = self.word_counts.get((word, label), 0) + 1
                score += math.log(count / (self.class_counts[label] + len(self.vocabulary)))
            scores[label] = score
            
        max_log_score = max(scores.values())
        linear_scores = {label: math.exp(score - max_log_score) for label, score in scores.items()}
        return max(linear_scores, key=linear_scores.get), linear_scores
    

def preprocess(text):
    text = text.lower()
    text = re.sub(r'[^a-z0-9\s]', '', text)
    return text

def evaluate_classifier(TP, TN, FP, FN):
    sensitivity = 0 if (TP + FN) == 0 else TP / (TP + FN)
    specificity = 0 if (TN + FP) == 0 else TN / (TN + FP)
    precision = 0 if (TP + FP) == 0 else TP / (TP + FP)
    npv = 0 if (TN + FN) == 0 else TN / (TN + FN)
    accuracy = 0 if (TP + TN + FP + FN) == 0 else (TP + TN) / (TP + TN + FP + FN)
    f_score = 0 if (precision + sensitivity) == 0 else 2 * precision * sensitivity / (precision + sensitivity)
    return sensitivity, specificity, precision, npv, accuracy, f_score

def calculate_metrics(test_labels, pred_labels, label):
    metrics = {l: {'tp': 0, 'tn': 0, 'fp': 0, 'fn': 0} for l in label}
    for true_label, predicted_label in zip(test_labels, pred_labels):
        for l in label:
            if true_label == l:
                if predicted_label == true_label:
                    metrics[l]['tp'] += 1
                else:
                    metrics[l]['fn'] += 1
            else:
                if predicted_label == l:
                    metrics[l]['fp'] += 1
                else:
                    metrics[l]['tn'] += 1
    return metrics

