import time
import random
import datetime
import telepot
from telepot.loop import MessageLoop
from picamera import PiCamera

def handle(msg):
    chat_id = msg['chat']['id']
    command = msg['text']

    print 'Got command: %s' % command

    if command == '/start':
        camera = PiCamera()
        camera.resolution = (640, 480)
        camera.start_recording('video.h264')
        time.sleep(5)
        camera.stop_recording()
        time.sleep(5)
        camera.close()
        bot.sendVideo(chat_id, video=open('/home/pi/video.h264','rb'))

    elif command == '/snap':
        camera=PiCamera()
        time.sleep(2)
        camera.capture('foo.jpg')
        camera.close()
        bot.sendPhoto(chat_id, photo=open('/home/pi/foo.jpg','rb') )

    elif command == '/time':
        bot.sendMessage(chat_id, str(datetime.datetime.now()))

bot = telepot.Bot('570195923:AAHkrMfD5b9itqzIHKTc1ybuB........')

MessageLoop(bot, handle).run_as_thread()
print (bot.getMe())
print 'I am listening ...'

while 1:
    time.sleep(10)