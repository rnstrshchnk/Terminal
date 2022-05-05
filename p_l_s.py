import random
import time
from datetime import datetime


file_path = r'D:/Hmw/git/Terminal/first.txt'

names = ['Alex',
         'Marina',
         'Victor',
         'Tommy',
         'Anna',
         'Vika',
         'Nika',
         'Elena',
         'Tonny',
         'Mke',
         'Glebb',
         'Stiven',
         'Jhonny',
         'Jimmy']


while True:

    with open(file_path, 'a+') as file_txt:
        now = datetime.now()

        name_id = random.randint(0, len(names) -1)


        user_name = names[name_id]

        dt_string = now.strftime("%d/%m/%Y %H:%M:%S")

        result_str = user_name + ' -- ' + str(dt_string) + '\n'

        file_txt.write(result_str)

        file_txt.close()

    time.sleep(0.5)
