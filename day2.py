from aiogram import types
from aiogram.types import FSInputFile, InlineKeyboardMarkup, InlineKeyboardButton


# День 2, Страница 1 - начало
async def send_day2_page1(message: types.Message):
    try:
        photo = FSInputFile("content/photos/day2_page1.jpg")
        await message.answer_photo(photo)
    except:
        pass

    try:
        voice = FSInputFile("content/voices/day2_page1.ogg")
        await message.answer_voice(voice)
    except:
        pass

    try:
        video = FSInputFile("content/videos/avelina.mov")
        await message.answer_video(video)
    except:
        pass


# День 2, Страница 1 - после ввода слова
async def send_day2_page1_done(message: types.Message):
    try:
        photo = FSInputFile("content/photos/day2_page1_done.jpg")
        await message.answer_photo(photo)
    except:
        pass

    try:
        voice = FSInputFile("content/voices/day2_page1_done.ogg")
        await message.answer_voice(voice)
    except:
        pass

    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="Открыть страницу 5", callback_data="day2_page2")]
    ])
    await message.answer("Нажми кнопку:", reply_markup=keyboard)


# День 2, Страница 2 - начало
async def send_day2_page2(message: types.Message):
    try:
        photo = FSInputFile("content/photos/day2_page2.jpg")
        await message.answer_photo(photo)
    except:
        pass

    try:
        voice = FSInputFile("content/voices/day2_page2.ogg")
        await message.answer_voice(voice)
    except:
        pass

    try:
        voice = FSInputFile("content/audio/song.mp3")
        await message.answer_audio(voice)
    except:
        pass


# День 2, Страница 2 - после первого слова
async def send_day2_page2_done(message: types.Message):
    try:
        photo = FSInputFile("content/photos/day2_page2_done.jpg")
        await message.answer_photo(photo)
    except:
        pass

    try:
        voice = FSInputFile("content/voices/day2_page2_done.ogg")
        await message.answer_voice(voice)
    except:
        pass

    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="Открыть страницу 6", callback_data="day2_page3")]
    ])
    await message.answer("Нажми кнопку:", reply_markup=keyboard)

# День 2, Страница 3 - начало
async def send_day2_page3(message: types.Message):
    try:
        photo = FSInputFile("content/photos/day3_page1.jpg")
        await message.answer_photo(photo)
    except:
        pass

    try:
        voice = FSInputFile("content/voices/day3_page1.ogg")
        await message.answer_voice(voice)
    except:
        pass

    try:
        photo = FSInputFile("content/videos/place1.MOV")
        await message.answer_video(photo)
    except:
        pass

    try:
        photo = FSInputFile("content/videos/place2.MOV")
        await message.answer_video(photo)
    except:
        pass

# День 2, Страница 3 - конец дня
async def send_day2_page3_done(message: types.Message):

    try:
        photo = FSInputFile("content/photos/day3_page1_done.jpg")
        await message.answer_photo(photo)
    except:
        pass

    try:
        voice = FSInputFile("content/voices/day3_page1_done.ogg")
        await message.answer_voice(voice)
    except:
        pass


    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="Открыть страницу 7", callback_data="complete_day2")]
    ])
    await message.answer("Нажми кнопку:", reply_markup=keyboard)