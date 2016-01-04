import requests

def random_word():
    word = requests.get('http://randomword.setgetgo.com/get.php')
    return word.text.replace('\n', '').replace('\r', '')

print(random_word())