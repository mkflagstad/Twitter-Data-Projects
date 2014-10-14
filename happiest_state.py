# Prints to standard out two letter abbreviation of state with highest average sentiment score
# for tweets found in the input twitter

# This file accepts two arguments: a sentiment file and a twitter data file.
# A sentiment file (AFINN-111.txt) and a twitter data file (test_twitter_data.json) have been provided
# in the git repository.
# Run file with:
# $python tweet_sentiment.py AFINN-111.txt test_twitter_data.json
import json
import sys


def get_sent_dict(a_sent_file):
    afinnfile = a_sent_file
    scores = {}
    for line in afinnfile:
        term, score  = line.split("\t")  # The file is tab-delimited. "\t" means "tab character"
        scores[term] = int(score)
    return scores

#Return a list of dictionaries containing tweet sentiment score and state (2 letter abbreviation)
def get_score_state_array(a_tweet_file, state_list, a_sent_dict):
    tweets = []
    for line in a_tweet_file:
        response = json.loads(str(line))
        if 'place' in response.keys() and response['place'] is not None:
            place = response['place']
            if place['country'] == 'United States':
                full_name = place['full_name']
                city , state = full_name.split(", ")
                if state in state_list:
                    tweets_dict = {}
                    tweets_dict['state'] = state
                    text = response['text']
                    tweet_score = 0
                    for word in text.split():
                        if word in a_sent_dict:
                            tweet_score += int(a_sent_dict[word])
                    tweets_dict['score'] = tweet_score
                    tweets.append(tweets_dict)
    return tweets


def print_happiest_state(a_score_state_array, a_state_list):
    highest_ave = 0
    for state in a_state_list:
        count = 0
        sentscore_tot = 0
        for tweet in a_score_state_array:
            if tweet["state"] == state:
                count += 1
                sentscore_tot += tweet["score"]
            if count > 0:
                ave = float(sentscore_tot) / float(count)
                if ave > highest_ave:
                    highest_ave = ave
                    highest_state = state
    print highest_state


def main():
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])
    states = [
        'AK',
        'AL',
        'AR',
        'AS',
        'AZ',
        'CA',
        'CO',
        'CT',
        'DC',
        'DE',
        'FL',
        'GA',
        'GU',
        'HI',
        'IA',
        'ID',
        'IL',
        'IN',
        'KS',
        'KY',
        'LA',
        'MA',
        'MD',
        'ME',
        'MI',
        'MN',
        'MO',
        'MP',
        'MS',
        'MT',
        'NA',
        'NC',
        'ND',
        'NE',
        'NH',
        'NJ',
        'NM',
        'NV',
        'NY',
        'OH',
        'OK',
        'OR',
        'PA',
        'PR',
        'RI',
        'SC',
        'SD',
        'TN',
        'TX',
        'UT',
        'VA',
        'VI',
        'VT',
        'WA',
        'WI',
        'WV',
        'WY'
    ]

    sent_dict = get_sent_dict(sent_file)
    score_state_array = get_score_state_array(tweet_file, states, sent_dict)
    print_happiest_state(score_state_array, states)

if __name__ == '__main__':
    main()
