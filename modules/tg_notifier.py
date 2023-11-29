
import telebot
import logging
import asyncio
import requests

class Telegram:

    def __init__(self, bot_token, channel_ids):
        self.logger = logging.getLogger(__name__)
        self.bot_token = bot_token
        self.channel_ids = channel_ids
        self.bot = telebot.TeleBot(bot_token)
    
    def create_message_content(self, _app, timestamp):
        content = f'<b>🔔 Обновление! 🔔</b>\n\n'
        content += f'🎮 <i>{_app.name}</i>\n'
        content += f'\n🕰 <i>{timestamp}</i>\n'
        return content, _app.pic_url

    def fire(self, updated_apps, timestamp):
        for _id in self.channel_ids:
            for app in updated_apps:
                content, pic_url = self.create_message_content(app, timestamp.strftime("%d.%m.%y %H:%M"))
                if pic_url:
                   self.bot.send_photo(_id, pic_url, caption=content,parse_mode='html')
                else:
                    self.bot.send_message(_id,text=content,parse_mode='html')
        