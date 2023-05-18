import asyncio
import logging
import os

from aiogram import Bot, Dispatcher, types, executor
from pytube import YouTube

TOKEN = "5469754814:AAGVX8Uq59SKTsdaWS8Q6dpD4cX9bD_ytE4"

logging.basicConfig(level=logging.INFO)
bot = Bot(token=TOKEN, parse_mode=types.ParseMode.HTML)
dp = Dispatcher(bot)


async def set_bot_command(dp):
    await dp.bot.set_my_commands([
        types.BotCommand('start', 'Botni ishga tushirish'),
        types.BotCommand('help', 'Qoshimcha kamandalar')
    ])


@dp.message_handler(commands=['start'])
async def start_bot_hendler(message: types.Message):
    await message.answer(f"Salom {message.chat.first_name}\n"
                         f"Menga youtubedagi video\n"   
                         f"linkini tashland")


@dp.message_handler(content_types=['text'])
async def video_hendler(message: types.Message):
    text = message.text
    print(text)
    if text.startswith("https://youtu.be.com"):
        await asyncio.sleep(3)
        await message.answer("Video yuklanmoqda!")

        url = text
        yt = YouTube(url)
        print("Downloading...")
        yt.streams.get_lowest_resolution().download(output_path="video\\", filename="result.mp4")
        i = types.InputFile("video\\result.mp4")
        await message.answer_video(video=i, caption=f"Sarlavha: {yt.title}")
        print("Download Successfully")
        os.remove("video\\result.mp4")
    elif text.startswith("https://youtu.be"):
        await asyncio.sleep(3)
        await message.answer("Video yuklanmoqda!")
        url = text
        yt = YouTube(url)
        print("Downloading...")
        yt.streams.get_lowest_resolution().download(output_path="video\\", filename="result.mp4")
        print("Download Successfully")
        i = types.InputFile("video\\result.mp4")
        await message.answer_video(video=i, caption=f"Sarlavha: {yt.title}")
        os.remove("video\\result.mp4")
    else:
        await message.answer("Uzur bu video youtube dan emas!")

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
