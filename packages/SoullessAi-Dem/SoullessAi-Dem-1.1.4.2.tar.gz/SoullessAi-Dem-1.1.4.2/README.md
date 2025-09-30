# SoullessAi-Dem
![](images/welcome.jpg)


Библиотека от создателей **Soulless Materia** для генерации демотиваторов. Совместима с **aiogram**, **telebot** и другими библиотеками для Telegram, а также с **ВКонтакте API**.

## Использование с aiogram

```bash
from aiogram import Bot, Dispatcher, types
from soulless_ai_dem import create_demotivator
import os

bot = Bot(token="your_token")
dp = Dispatcher(bot)

@dp.message_handler(content_types=types.ContentType.PHOTO)
async def handle_photo(message: types.Message):
    photo = message.photo[-1]
    file_id = photo.file_id
    file = await bot.get_file(file_id)
    input_path = f"temp_{file_id}.jpg"
    output_path = f"dem_{file_id}.jpg"

    await file.download(input_path)

    text_lines = ["Верхний текст", "Нижний текст"]
    create_demotivator(input_path, output_path, text_lines)

    with open(output_path, 'rb') as photo:
        await message.answer_photo(photo)

    os.remove(input_path)
    os.remove(output_path)
```

## Использование с telebot

```bash
import telebot
from soulless_ai_dem import create_demotivator
import os

bot = telebot.TeleBot("your_token")

@bot.message_handler(content_types=['photo'])
def handle_photo(message):
    file_id = message.photo[-1].file_id
    file_info = bot.get_file(file_id)
    downloaded_file = bot.download_file(file_info.file_path)

    input_path = f"temp_{file_id}.jpg"
    output_path = f"dem_{file_id}.jpg"

    with open(input_path, 'wb') as new_file:
        new_file.write(downloaded_file)

    text_lines = ["Верхний текст", "Нижний текст"]
    create_demotivator(input_path, output_path, text_lines)

    with open(output_path, 'rb') as photo:
        bot.send_photo(message.chat.id, photo)

    os.remove(input_path)
    os.remove(output_path)
```

**Параметры:**
- `input_path`: Путь к исходному изображению
- `output_path`: Путь для сохранения результата
- `text_lines`: Список строк текста (максимум 3 строки)
- `small`: Уменьшенный формат (предназначено для групп)

### get_random_text()
Возвращает случайный текст для демотиватора.

```bash
from soulless_ai_dem import get_random_text

text_lines = get_random_text()
```

## Установка

```bash
pip install SoullessAi-Dem