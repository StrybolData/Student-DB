import nltk
from nltk.corpus import names

#male_names = [name for name in names.words('male.txt')]
#male_names[:5]
#female_names = [name for name in names.words('female.txt')]
#female_names[:5]
#female_names.index('Alessia')

##Bayesian model
#first step identify training set
#second step define your features/columns
#analyse the data
#run the model
#test the model


model_names = [(name, 'male') for name in names.words('male.txt')]
model_names = model_names + [(name, 'female') for name in names.words('female.txt')]

import random
random.shuffle(model_names)

def gender_feature(word):
    return {'last_letter': word[-1]}


feature_sets = {(gender_feature(n), g) for (n,g) in model_names}
train_set, test_set = feature[500:], feature_sets[:500]
len(train_set), len(test_set)
classifier = nltk.NaiveBayesClassifier.train(train_set)

classifier.classify(gender_feature('Alessia'))
#naive model always follows dictionary data structure

