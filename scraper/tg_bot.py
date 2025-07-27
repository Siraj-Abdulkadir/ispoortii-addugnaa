from telegram import Bot
from telegram.ext import Updater
from dotenv import load_dotenv
import scraper as SC
from telegram.constants import ParseMode
from googletrans import Translator
import os
import asyncio

load_dotenv()

bot_token = os.getenv("BOT_TOKEN")

bot = Bot(token=bot_token)

channel_id = "@IspoortiiAddugnaa"

title,content = SC.Scraper()

async def translate_text():
     async with Translator() as translator:
         translated_title = await translator.translate(title,src='en', dest='om')
         translate_content = await translator.translate(content, src='en', dest='om')

         return translated_title.text,translate_content.text

     
translated_title,translated_content = asyncio.run(translate_text())

async def Send_Message():
    image_path='image.jpg'
    await bot.send_photo(chat_id=channel_id,photo=open(image_path,'rb'),caption=f'<b>\n{translated_title}</b>',parse_mode=ParseMode.HTML)
    await bot.send_message(chat_id=channel_id,text=translated_content)

asyncio.run(Send_Message())    