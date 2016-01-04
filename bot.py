import requests


def random_word():
    return requests.get('http://randomword.setgetgo.com/get.php').text.strip()

print(random_word())
