import datetime
import random

import vk_api
from time import sleep

token = ''  # vkhost.github.io
name = 'ФИО'

str_1 = 'Запись на ИГРОВУЮ ТРЕНИРОВКУ 23'
str_2 = 'Уровень «любой»'

vkq = vk_api.VkApi(token=token)
owner = -202633307
count = 3

print(name + " hosted!")

while True:
    sleep(random.randint(10, 15))
    wall = vkq.method('wall.get', {'owner_id': owner, 'count': count})
    print(str(datetime.datetime.now()) + ' Wall getted!')

    for i in range(count):
        post = wall['items'][i]
        text = str(post['text'])

        if str_1 in text and str_2 in text:
            sleep(1)
            vkq.method('messages.send',
                       {'peer_id': owner, 'random_id': random.randint(111111, 999999), 'message': 'Секция ' + name})
            print(str(datetime.datetime.now()) + 'Entry catched!')
            exit()
