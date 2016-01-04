import json, requests

random_word = requests.get('http://randomword.setgetgo.com/get.php')
random_word = random_word.text.replace('\n', '').replace('\r', '')

print(random_word)