from __future__ import (absolute_import, division,
                        print_function, unicode_literals)
import random
import time
<<<<<<< HEAD
# import sys
=======
import sys
>>>>>>> 452c38f18d31631d159a2bf095f59ae3e40935b3
import os
#import tweepy  # for tweeting
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


def main():
<<<<<<< HEAD
    thepath = os.environ.get('FILES_PATH')
    f_next = os.path.join(thepath, "next_quotes.txt")
    f_past = os.path.join(thepath, "past_quotes.txt")
    quote = get_tweet(f_next, f_past)
    # old_stdout = sys.stdout
    # log_file = open('all.log', 'a')
    # log_file.write('quote')
    tweet(quote)  # and finally tweets
    # log_file.close()
=======
    f_next = "next_quotes.txt"
    f_past = "past_quotes.txt"
    quote = get_tweet(f_next, f_past)
    # old_stdout = sys.stdout
    log_file = open('all.log', 'a')
    log_file.write(quote)
    #tweet(quote)  # and finally tweets
    log_file.close()
>>>>>>> 452c38f18d31631d159a2bf095f59ae3e40935b3


if __name__ == "__main__":
    ODDS = 4
    while True:
<<<<<<< HEAD
        time.sleep(random.randint(3300, 3900))  # we make it sleep up to 5 minutes
        die_roll = random.choice(range(ODDS))  # rolls a die
        if die_roll == 0:
=======
        time.sleep(random.randint(1, 5))  # we make it sleep up to 5 minutes
        die_roll = random.choice(range(ODDS))  # rolls a die
        if die_roll == 0:
            print("We're tweeting!")
>>>>>>> 452c38f18d31631d159a2bf095f59ae3e40935b3
            main()
