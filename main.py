import time
import os

minutes = 30
tmer = minutes * 60


def timer(seconds):
    while seconds:
        mins, secs = divmod(seconds, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(timer, end="\r") 
        time.sleep(1)
        seconds -= 1
    print("Время вышло!")


def stoper():
   photo_path = "/укажи/свой/путь/photo.png" #вот тут указывай путь до фото
   os.system(f"eog --fullscreen {photo_path}")
   print("ХВАТИТ ЗАДРОТИТЬ!!!")


while True:
   timer(tmer)
   stoper()
