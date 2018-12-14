# telegram-bot
A telegram bot to control your raspberry Pi

## Objective
Creating a telegram bot using telepot at raspberry pi side which can respond to few commands entered by user on telegram app.
This bot can reply to your commands by text messages, web information, photos from a link or camera, videos, audio files or you can even control GPIO pins.

## Creating a bot
Follow this link to create a telegram bot: [here](https://docs.microsoft.com/en-us/azure/bot-service/bot-service-channel-connect-telegram?view=azure-bot-service-4.0)

After succesful creation, copy the "access token" and paste in the code

```python
bot = telepot.Bot('access token')
```

## Installing telepot
```python
sudo pip install telepot
```

## A function for handling messages
```python
def handle(msg):
    chat_id = msg['chat']['id']
    command = msg['text']
```

## Replying with a text message

```python
if command == '/hi':
        telegram_bot.sendMessage (chat_id, str("Hi!"))
```

## For snapping image and sending it back

```python
camera=PiCamera()
        time.sleep(2)
        camera.capture('img_name.jpg')
        camera.close()
        bot.sendPhoto(chat_id, photo=open('path','rb') )
```

For other files like videos or audios etc, you can check here:[telepot documentation](https://telepot.readthedocs.io/en/latest/reference.html)

Similarly, you can use GPIOs according to the commands.
