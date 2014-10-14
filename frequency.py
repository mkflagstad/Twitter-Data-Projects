# Prints to standard out the frequency of each term found in twitter data.
# Frequency is defined as [# of occurrences of term in all tweets]/[# of occurrences of all terms in all tweets]
# This file accepts one argument, a twitter data file.
# A twitter data file (test_twitter_data.json) have been provided in the git repository.
# Run file with:
# $python tweet_sentiment.py test_twitter_data.json
import json
import sys

def get_tweet_text(a_tweet_file):
    tweets = []
    for line in a_tweet_file:
        response = json.loads(str(line))
        if 'lang' in response.keys() and response['lang'] == 'en':
            if 'text' in response:
                tweets.append(response['text'])
    return tweets

def get_term_count(a_tweet_array):
    term_count_dict = {}
    total_term_count = 0
    for tweet in a_tweet_array:
        for word in tweet.split():
            if word not in term_count_dict:
                term_count_dict[word] = 1
            else:
                term_count_dict[word] += 1
            total_term_count += 1
    return term_count_dict, total_term_count

def print_term_freq(term_count_dict, total_term_count):
    for term in term_count_dict:
        term_freq = float(term_count_dict[term])/float(total_term_count)
        print term + " " + str(term_freq)

def main():
    tweet_file = open(sys.argv[1])
    tweet_text_array = get_tweet_text(tweet_file)
    term_count_dict, total_term_count = get_term_count(tweet_text_array)
    print_term_freq(term_count_dict, total_term_count)





if __name__ == '__main__':
    main()
