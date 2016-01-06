import requests
import random
import config
import tweepy


def random_word():
    wlength = {'len': random.randrange(3, 19)}
    return requests.get('http://randomword.setgetgo.com/get.php', params=wlength).text.strip()

CONSUMER_KEY = 'vNXrQnSpIDQecNmt2GWtotrxb'
ACCESS_KEY = '4704978270-fKtYR3DjbVy5agimR6vrUkaw7msmbMFqMCzVDsT'
auth = tweepy.OAuthHandler(CONSUMER_KEY, config.TWITTER_CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, config.TWITTER_ACCESS_SECRET)
api = tweepy.API(auth)

three_words = [random_word(), random_word(), random_word()]
print(three_words)
