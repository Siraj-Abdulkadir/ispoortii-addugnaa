from telegram import Bot
from telegram.ext import Updater
from dotenv import load_dotenv
import scraper as SC
from telegram.constants import ParseMode
import os
import asyncio

load_dotenv()

bot_token = os.getenv("BOT_TOKEN")

bot = Bot(token=bot_token)

channel_id = "@IspoortiiAddugnaa"

async def Send_Message():
    image_path='image.jpg'
    title,content = SC.Scraper()
    await bot.send_photo(chat_id=channel_id,photo=open(image_path,'rb'),caption=f'<b>\n{title}</b>',parse_mode=ParseMode.HTML)
    await bot.send_message(chat_id=channel_id,text=content)

asyncio.run(Send_Message())    