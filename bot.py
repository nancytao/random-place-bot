import config
import json
import random
import requests
import tweepy
import urllib


def get_position(words="clashes.crib.purses"):  # default is Georgia Tech college of computing
    if isinstance(words, list):
        words = "%s.%s.%s" % (words[0], words[1], words[2])

    params = {
        'string': words,
        'key': config.W3W_KEY,
    }
    encparams = urllib.urlencode(params)
    response = urllib.urlopen("http://api.what3words.com/w3w", encparams).read()
    return json.loads(response)


def random_word():
    wlength = {'len': 5}
    return requests.get('http://randomword.setgetgo.com/get.php', params=wlength).text.strip()

# CONSUMER_KEY = 'vNXrQnSpIDQecNmt2GWtotrxb'
# ACCESS_KEY = '4704978270-fKtYR3DjbVy5agimR6vrUkaw7msmbMFqMCzVDsT'
# auth = tweepy.OAuthHandler(CONSUMER_KEY, config.TWITTER_CONSUMER_SECRET)
# auth.set_access_token(ACCESS_KEY, config.TWITTER_ACCESS_SECRET)
# api = tweepy.API(auth)

three_words = [random_word(), random_word(), random_word()]

print three_words
position = get_position(three_words)

while True:
    try:
        throw_away = position['error']
        three_words = [random_word(), random_word(), random_word()]
        print three_words
        position = get_position(three_words)
    except KeyError:
        break

print get_position(three_words)
