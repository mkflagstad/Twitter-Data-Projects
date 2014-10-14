#Prints to standard output then top ten hashtags found in input twitter data.

import json
import sys

#Creates a dictionary of form "hashtag":frequency
def get_hashtag_freq(a_tweet_file):
    hashtag_freq_dict = {}
    for line in a_tweet_file:
        response = json.loads(str(line))
        if 'entities' in response.keys() and 'lang' in response.keys() and response['lang'] == 'en':
            entities = response["entities"]
            if 'hashtags' in entities.keys() and entities['hashtags'] != []:
                for i in entities['hashtags']:
                    hashtag = i['text']
                    if hashtag not in hashtag_freq_dict:
                        hashtag_freq_dict[hashtag] = 1
                    else:
                        hashtag_freq_dict[hashtag] += 1
    return hashtag_freq_dict


def print_top_ten(a_hash_tag_freq_dict):
    top_freqs = [0] * 10
    top_terms = [" "] * 10
    for i in a_hash_tag_freq_dict:
        if a_hash_tag_freq_dict[i] >= top_freqs[0]:
            top_freqs.insert(0, a_hash_tag_freq_dict[i])
            top_freqs.pop()
            top_terms[0] = i
        elif a_hash_tag_freq_dict[i] >= top_freqs[1] and a_hash_tag_freq_dict[i] < top_freqs[0]:
            top_freqs.insert(1, a_hash_tag_freq_dict[i])
            top_freqs.pop()
            top_terms[1] = i
        elif a_hash_tag_freq_dict[i] >= top_freqs[2] and a_hash_tag_freq_dict[i] < top_freqs[1]:
            top_freqs.insert(2, a_hash_tag_freq_dict[i])
            top_freqs.pop()
            top_terms[2] = i
        elif a_hash_tag_freq_dict[i] >= top_freqs[3] and a_hash_tag_freq_dict[i] < top_freqs[2]:
            top_freqs.insert(3, a_hash_tag_freq_dict[i])
            top_freqs.pop()
            top_terms[3] = i
        elif a_hash_tag_freq_dict[i] >= top_freqs[4] and a_hash_tag_freq_dict[i] < top_freqs[3]:
            top_freqs.insert(4, a_hash_tag_freq_dict[i])
            top_freqs.pop()
            top_terms[4] = i
        elif a_hash_tag_freq_dict[i] >= top_freqs[5] and a_hash_tag_freq_dict[i] < top_freqs[4]:
            top_freqs.insert(5, a_hash_tag_freq_dict[i])
            top_freqs.pop()
            top_terms[5] = i
        elif a_hash_tag_freq_dict[i] >= top_freqs[6] and a_hash_tag_freq_dict[i] < top_freqs[5]:
            top_freqs.insert(6, a_hash_tag_freq_dict[i])
            top_freqs.pop()
            top_terms[6] = i
        elif a_hash_tag_freq_dict[i] >= top_freqs[7] and a_hash_tag_freq_dict[i] < top_freqs[6]:
            top_freqs.insert(7, a_hash_tag_freq_dict[i])
            top_freqs.pop()
            top_terms[7] = i
        elif a_hash_tag_freq_dict[i] >= top_freqs[8] and a_hash_tag_freq_dict[i] < top_freqs[7]:
            top_freqs.insert(8, a_hash_tag_freq_dict[i])
            top_freqs.pop()
            top_terms[8] = i
        elif a_hash_tag_freq_dict[i] >= top_freqs[9] and a_hash_tag_freq_dict[i] < top_freqs[8]:
            top_freqs.insert(9, a_hash_tag_freq_dict[i])
            top_freqs.pop()
            top_terms[9] = i

    for i in range(10):
        print top_terms[i] + " " + str(top_freqs[i])


def main():
    tweet_file = open(sys.argv[1])
    hashtag_freq_dict = get_hashtag_freq(tweet_file)
    print_top_ten(hashtag_freq_dict)




if __name__ == '__main__':
    main()
