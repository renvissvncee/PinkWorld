from aiogram import types
from aiogram.types import FSInputFile, InlineKeyboardMarkup, InlineKeyboardButton


# День 3, Страница 1 - начало
async def send_day3_page1(message: types.Message):
    try:
        photo = FSInputFile("content/photos/day2_page3.jpg")
        await message.answer_photo(photo)
    except:
        pass

    try:
        voice = FSInputFile("content/voices/day2_page3.ogg")
        await message.answer_voice(voice)
    except:
        pass


# День 3, Страница 1 - после ввода слова
async def send_day3_page1_done(message: types.Message):
    try:
        photo = FSInputFile("content/photos/day2_completed.jpg")
        await message.answer_photo(photo)
    except:
        pass

    try:
        voice = FSInputFile("content/voices/day2_completed.ogg")
        await message.answer_voice(voice)
    except:
        pass

    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="Открыть страницу 8", callback_data="day3_page2")]
    ])
    await message.answer("Нажми кнопку:", reply_markup=keyboard)


# День 3, Страница 2 - начало
async def send_day3_page2(message: types.Message):
    try:
        photo = FSInputFile("content/photos/day3_page2.jpg")
        await message.answer_photo(photo)
    except:
        pass

    try:
        voice = FSInputFile("content/voices/day3_page2.ogg")
        await message.answer_voice(voice)
    except:
        pass

    try:
        photo = FSInputFile("content/photos/map.jpg")
        await message.answer_photo(photo)
    except:
        pass


# День 3, Страница 2 - после первого слова
async def send_day3_page2_done(message: types.Message):
    try:
        photo = FSInputFile("content/photos/day3_page2_done.jpg")
        await message.answer_photo(photo)
    except:
        pass

    try:
        voice = FSInputFile("content/voices/day3_page2_done.ogg")
        await message.answer_voice(voice)
    except:
        pass
    
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="Открыть страницу 9", callback_data="day3_page3")]
    ])
    await message.answer("Нажми кнопку:", reply_markup=keyboard)



# День 3, Страница 3 - начало
async def send_day3_page3(message: types.Message):
    try:
        photo = FSInputFile("content/photos/day3_page3.jpg")
        await message.answer_photo(photo)
    except:
        pass

    try:
        voice = FSInputFile("content/voices/day3_page3.ogg")
        await message.answer_voice(voice)
    except:
        pass


# День 3, Страница 3 - после первого слова
async def send_day3_page3_after_first_word(message: types.Message):
    try:
        photo = FSInputFile("content/photos/day3_done.jpg")
        await message.answer_photo(photo)
    except:
        pass

    try:
        voice = FSInputFile("content/voices/day3_done.ogg")
        await message.answer_voice(voice)
    except:
        pass


# День 3, Страница 3 - конец квеста
async def send_day3_page3_done(message: types.Message):
    await message.answer("🎊 Поздравляем! Весь квест завершен! 💕")

    try:
        photo = FSInputFile("content/photos/day3_completed.jpg")
        await message.answer_photo(photo)
    except:
        pass

    try:
        voice = FSInputFile("content/voices/day3_completed.ogg")
        await message.answer_voice(voice)
    except:
        pass

    await message.answer("Спасибо за игру! ❤️")