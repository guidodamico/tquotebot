import json
#import pickle
import random

# Load the json of all quotes, which has the format {author: list_of_quotes}
dic_quotes = json.load(open('dict_quotes.json', 'r'))
#dic_quotes = pickle.load(open('brainyquote_quotes.pkl', 'rb'))

# Put things in the form of tweets: quote - author
all_tweets = []

for k, v in dic_quotes.items():
    for quote in v:
        tweet = str(quote) + " - " + str(k)
        all_tweets.append(tweet)

# Select those with <=140 characters
ok_tweets = [t for t in all_tweets if len(t) <= 140]
print(len(ok_tweets))

# For the moment being, let's just keep the ones <= 140, shuffling
random.shuffle(ok_tweets)
with open("all_quotes.txt", 'w') as f:
    for t in ok_tweets:
        f.write(t+'\n')
