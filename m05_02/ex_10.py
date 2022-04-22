'''
Задача: Поиск url
'''

import re

text_url = "The main search site in the world is https://www.google.com The main social network for people in the " \
           "world is https://www.facebook.com But programmers have their own social network http://github.com There " \
           "they share their code. some url to check https://www..facebook.com www.facebook.com https://www.app.facebook.com My site: https://krabaton.info  https://api.io"


result = re.findall(r'https?://\w{3}\.?(?:\w+\.)*\w{2,5}', text_url)
print(result)

# admin@gmail.com
