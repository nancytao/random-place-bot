import requests, config


def random_word():
    wlength = {'len': '6'}
    return requests.get('http://randomword.setgetgo.com/get.php', params=wlength).text.strip()

three_words = [random_word(), random_word(), random_word()]
print(three_words)
