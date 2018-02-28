from __future__ import (absolute_import, division,
                        print_function, unicode_literals)
import random
from time import sleep
import sys
import os
import tweepy  # for tweeting
try:
    import secrets  # shhhh
except ImportError:
    pass


def get_tweet(f_next, f_past):
    """Get a quote from the next quotes file,
    delete it and put it in the past quotes file"""
    with open(f_next, 'r+') as f:  # open in read / write mode
        quote = f.readline()  # read the first line
        data = f.read()  # read the rest
        f.seek(0)  # set the cursor to the top of the file
        f.write(data)  # write the data back
        f.truncate()  # set the file size to the current size
    with open(f_past, 'a') as f:  # open in append mode
        f.write(quote)  # write the quote to the file of past quotes
    return quote


def tweet(message):
    """Tweets the quote"""
    consumer_key = os.environ.get('TWITTER_CONSUMER_KEY')
    consumer_secret = os.environ.get('TWITTER_CONSUMER_SECRET')
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.secure = True
    access_token = os.environ.get('TWITTER_ACCESS_TOKEN')
    access_token_secret = os.environ.get('TWITTER_ACCESS_TOKEN_SECRET')
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth)  # API instance
    print("Posting message {}".format(message))
    api.update_status(status=str(message))
    return


if __name__ == "__main__":
    #scriptdir = os.path.dirname(os.path.realpath(sys.argv[0]))
    #f_next = os.path.join(scriptdir, "next_quotes.txt")
    #f_past = os.path.join(scriptdir, "past_quotes.txt")
    f_next = "next_quotes.txt"
    f_past = "past_quotes.txt"
    ODDS = 4
    die_roll = random.choice(range(ODDS))  # rolls a die
    if die_roll == 0:
        sleep(random.randint(1, 300))  # we make it sleep up to 5 minutes
        quote = get_tweet(f_next, f_past)
        old_stdout = sys.stdout
        log_file = open('all.log', 'a')
        sys.stdout = log_file
        tweet(quote)  # and finally tweets
        log_file.close()