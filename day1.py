from aiogram import types
from aiogram.types import FSInputFile, InlineKeyboardMarkup, InlineKeyboardButton


# День 1, Страница 1 - начало
async def send_day1_page1(message: types.Message):
    # Фото
    try:
        photo = FSInputFile("content/photos/day1_page1.jpg")
        await message.answer_photo(photo)
    except:
        pass

    # Голосовое
    try:
        voice = FSInputFile("content/voices/day1_page1.ogg")
        await message.answer_voice(voice)
    except:
        pass


# День 1, Страница 1 - после ввода слова
async def send_day1_page1_done(message: types.Message):
    # Фото
    try:
        photo = FSInputFile("content/photos/day1_page1_done.jpg")
        await message.answer_photo(photo)
    except:
        pass

    # Голосовое
    try:
        voice = FSInputFile("content/voices/day1_page1_done.ogg")
        await message.answer_voice(voice)
    except:
        pass

    # Кнопка для следующей страницы
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="Открыть страницу 2", callback_data="day1_page2")]
    ])
    await message.answer("Нажми кнопку:", reply_markup=keyboard)


# День 1, Страница 2 - начало
async def send_day1_page2(message: types.Message):
    # Фото
    try:
        photo = FSInputFile("content/photos/day1_page2.jpg")
        await message.answer_photo(photo)
    except:
        pass

    # Голосовое
    try:
        voice = FSInputFile("content/voices/day1_page2.ogg")
        await message.answer_voice(voice)
    except:
        pass


# День 1, Страница 2 - после первого слова
async def send_day1_page2_after_first_word(message: types.Message):
    # Фото
    try:
        photo = FSInputFile("content/photos/day1_page2_after1.jpg")
        await message.answer_photo(photo)
    except:
        pass

    # Голосовое
    try:
        voice = FSInputFile("content/voices/day1_page2_after1.ogg")
        await message.answer_voice(voice)
    except:
        pass


# День 1, Страница 2 - после второго слова
async def send_day1_page2_done(message: types.Message):
    # Фото
    try:
        photo = FSInputFile("content/photos/day1_page2_done.jpg")
        await message.answer_photo(photo)
    except:
        pass

    # Голосовое
    try:
        voice = FSInputFile("content/voices/day1_page2_done.ogg")
        await message.answer_voice(voice)
    except:
        pass

    # Кнопка для следующей страницы
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="Открыть страницу 3", callback_data="day1_page3")]
    ])
    await message.answer("Нажми кнопку:", reply_markup=keyboard)


# День 1, Страница 3 - начало
async def send_day1_page3(message: types.Message):
    # Фото
    try:
        photo = FSInputFile("content/photos/day1_page3.jpg")
        await message.answer_photo(photo)
    except:
        pass

    # Голосовое
    try:
        voice = FSInputFile("content/voices/day1_page3.ogg")
        await message.answer_voice(voice)
    except:
        pass


# День 1, Страница 3 - после первого слова
async def send_day1_page3_after_first_word(message: types.Message):
    # Фото
    try:
        photo = FSInputFile("content/photos/day1_page3_after1.jpg")
        await message.answer_photo(photo)
    except:
        pass

    # Голосовое
    try:
        voice = FSInputFile("content/voices/day1_page3_after1.ogg")
        await message.answer_voice(voice)
    except:
        pass


# День 1, Страница 3 - конец дня
async def send_day1_page3_done(message: types.Message):
    # Фото
    try:
        photo = FSInputFile("content/photos/day1_completed.jpg")
        await message.answer_photo(photo)
    except:
        pass

    # Голосовое
    try:
        voice = FSInputFile("content/voices/day1_completed.ogg")
        await message.answer_voice(voice)
    except:
        pass

    # Кнопка завершения дня
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="Открыть страницу 4", callback_data="complete_day1")]
    ])
    await message.answer("Нажми кнопку:", reply_markup=keyboard)