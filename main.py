import random
import vk_api
from time import sleep

token = ''
name = 'ФИО'

owner = -202633307
str_1 = 'Запись на ИГРОВУЮ ТРЕНИРОВКУ 23'
str_2 = 'Уровень «любой»'

vkq = vk_api.VkApi(token=token)

print(name + " hosted!")

while True:
    sleep(random.randint(35, 65))
    wall = vkq.method('wall.get', {'owner_id': owner, 'count': 2})
    print('Wall getted!')
    post = wall['items'][0]
    text = str(post['text'])

    if str_1 in text and str_2 in text:
        sleep(2)
        vkq.method('messages.send',
                   {'peer_id': owner, 'random_id': random.randint(111111, 999999), 'message': 'Секция ' + name})
        print('Entry catched!')
        exit()
