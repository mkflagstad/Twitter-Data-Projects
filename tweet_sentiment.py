# Prints to standard out the text and sentiment score of each tweet.

# This file accepts two arguments: a sentiment file and a twitter data file.
# A sentiment file (AFINN-111.txt) and a twitter data file (test_twitter_data.json) have been provided
# in the git repository.
# Run file with:
# $python tweet_sentiment.py AFINN-111.txt test_twitter_data.json

import json
import sys

#Creates dictionary of form <term>:<score> from sentiment file
def get_sent_dict(a_sent_file):
    afinnfile = a_sent_file
    scores = {}
    for line in afinnfile:
        term, score  = line.split("\t")  # The file is tab-delimited. "\t" means "tab character"
        scores[term] = int(score)
    return scores

def get_tweet_text(a_tweet_file):
    tweets = []
    for line in a_tweet_file:
       response = json.loads(str(line))
       if 'lang' in response.keys() and response['lang'] == 'en':
           if 'text' in response:
               tweets.append(response['text'])
    return tweets

def print_tweet_sentiment_score(a_tweet_array, a_sent_dict):
    for tweet in a_tweet_array:
        tweet_score = 0
        for word in tweet.split():
            if word in a_sent_dict:
                tweet_score += int(a_sent_dict[word])
        print tweet_score


def main():
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])
    sent_dict = get_sent_dict(sent_file)
    tweet_text_array = get_tweet_text(tweet_file)
    print_tweet_sentiment_score(tweet_text_array, sent_dict)

if __name__ == '__main__':
    main()
