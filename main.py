import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from aiogram.types import FSInputFile, InlineKeyboardMarkup, InlineKeyboardButton
from datetime import datetime

# Токен бота (замени на свой)
BOT_TOKEN = "8677048593:AAHjszFJcHE6NGxMY3-k0hQubVqyNhjkFBw"

# Хранение состояния пользователей (простой словарь)
user_state = {}

# Создаем бота и диспетчер
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()


# Проверяем, разрешен ли пользователь (только один человек)
def is_allowed(user_id):
    return user_id == 794364046 or user_id == 829573384  # Замени на реальный ID пользователя


# Обработчик команды /start
@dp.message(Command("start"))
async def handle_start(message: types.Message):
    if not is_allowed(message.from_user.id):
        await message.answer("Доступ запрещен")
        return

    user_id = message.from_user.id

    # Отправляем вступление
    try:
        video = FSInputFile("content/videos/intro.gif")
        await message.answer_video(video)
    except:
        pass

    try:
        voice = FSInputFile("content/voices/intro.ogg")
        await message.answer_voice(voice)
    except:
        pass

    # Кнопка для начала
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="Открыть страницу 1", callback_data="start_page1")]
    ])
    await message.answer("Нажми кнопку, чтобы начать:", reply_markup=keyboard)


# Обработчик команды /day2 (для тестирования)
@dp.message(Command("day2"))
async def handle_day2_test(message: types.Message):
    if not is_allowed(message.from_user.id):
        await message.answer("Доступ запрещен")
        return

    user_id = message.from_user.id
    user_state[user_id] = "day2_page1_wait"
    from day2 import send_day2_page1
    await send_day2_page1(message)


# Обработчик команды /day3 (для тестирования)
@dp.message(Command("day3"))
async def handle_day3_test(message: types.Message):
    if not is_allowed(message.from_user.id):
        await message.answer("Доступ запрещен")
        return

    user_id = message.from_user.id
    user_state[user_id] = "day3_page1_wait"
    from day3 import send_day3_page1
    await send_day3_page1(message)


# Обработчик callback-кнопок
@dp.callback_query()
async def handle_callback(callback: types.CallbackQuery):
    if not is_allowed(callback.from_user.id):
        await callback.answer("Доступ запрещен")
        return

    user_id = callback.from_user.id
    data = callback.data

    if data == "start_page1":
        user_state[user_id] = "day1_page1_wait"
        from day1 import send_day1_page1
        await send_day1_page1(callback.message)
        await callback.answer()

    elif data == "day1_page2":
        user_state[user_id] = "day1_page2_wait1"
        from day1 import send_day1_page2
        await send_day1_page2(callback.message)
        await callback.answer()

    elif data == "day1_page3":
        user_state[user_id] = "day1_page3_wait1"
        from day1 import send_day1_page3
        await send_day1_page3(callback.message)
        await callback.answer()

    elif data == "complete_day1":
        user_state[user_id] = "day1_completed"
        await callback.message.answer("")
        # Проверка даты для открытия дня 2
        current_time = datetime.now()
        if current_time >= datetime(2026, 5, 13, 9, 0):
            user_state[user_id] = "day2_page1_wait"
            from day2 import send_day2_page1
            await send_day2_page1(callback.message)
        await callback.answer()

    elif data == "day2_page2":
        user_state[user_id] = "day2_page2_wait1"
        from day2 import send_day2_page2
        await send_day2_page2(callback.message)
        await callback.answer()

    elif data == "day2_page3":
        user_state[user_id] = "day2_page3_wait1"
        from day2 import send_day2_page3
        await send_day2_page3(callback.message)
        await callback.answer()

    elif data == "complete_day2":
        user_state[user_id] = "day2_completed"
        await callback.message.answer("")
        # Проверка даты для открытия дня 3
        current_time = datetime.now()
        if current_time >= datetime(2026, 5, 14, 9, 0):
            user_state[user_id] = "day3_page1_wait"
            from day3 import send_day3_page1
            await send_day3_page1(callback.message)
        await callback.answer()

    elif data == "day3_page2":
        user_state[user_id] = "day3_page2_wait1"
        from day3 import send_day3_page2
        await send_day3_page2(callback.message)
        await callback.answer()

    elif data == "day3_page3":
        user_state[user_id] = "day3_page3_wait1"
        from day3 import send_day3_page3
        await send_day3_page3(callback.message)
        await callback.answer()
        


# Обработчик всех сообщений
@dp.message()
async def handle_message(message: types.Message):
    if not is_allowed(message.from_user.id):
        await message.answer("Доступ запрещен")
        return

    user_id = message.from_user.id
    text = message.text.lower().strip()

    # День 1
    if user_state.get(user_id) == "day1_page1_wait":
        if "цветы" in text:
            user_state[user_id] = "day1_page1_done"
            from day1 import send_day1_page1_done
            await send_day1_page1_done(message)
        else:
            pass

    elif user_state.get(user_id) == "day1_page2_wait1":
        if "сладости" in text:
            user_state[user_id] = "day1_page2_wait2"
            from day1 import send_day1_page2_after_first_word
            await send_day1_page2_after_first_word(message)
        else:
            pass
    elif user_state.get(user_id) == "day1_page2_wait2":
        if "розовость" in text:
            user_state[user_id] = "day1_page2_done"
            from day1 import send_day1_page2_done
            await send_day1_page2_done(message)
        else:
            pass

    elif user_state.get(user_id) == "day1_page3_wait1":
        if "спутник" in text:  # Замени на нужное слово
            user_state[user_id] = "day1_page3_wait2"
            from day1 import send_day1_page3_after_first_word
            await send_day1_page3_after_first_word(message)
        else:
            pass

    elif user_state.get(user_id) == "day1_page3_wait2":
        if "отблеск" in text:  # Замени на нужное слово
            user_state[user_id] = "day1_page3_done"
            from day1 import send_day1_page3_done
            await send_day1_page3_done(message)
        else:
            pass

    # Заглушка для тестирования: после дня 1 ввести "testday2" чтобы открыть день 2
    elif user_state.get(user_id) == "day1_completed":
        if text == "testday2":
            user_state[user_id] = "day2_page1_wait"
            from day2 import send_day2_page1
            await send_day2_page1(message)
        else:
            pass

    # День 2
    elif user_state.get(user_id) == "day2_page1_wait":
        if "хранительница" in text:
            user_state[user_id] = "day2_page1_done"
            from day2 import send_day2_page1_done
            await send_day2_page1_done(message)
        else:
            pass

    elif user_state.get(user_id) == "day2_page2_wait1":
        if "окунуться" in text:
            user_state[user_id] = "day2_page2_done"
            from day2 import send_day2_page2_done
            await send_day2_page2_done(message)
        else:
            pass


    elif user_state.get(user_id) == "day2_page3_wait1":
        if "совпадение" in text:
            user_state[user_id] = "day2_page3_done"
            from day2 import send_day2_page3_done
            await send_day2_page3_done(message) 
        else:
            pass

    # Заглушка для тестирования: после дня 2 ввести "testday3" чтобы открыть день 3
    elif user_state.get(user_id) == "day2_completed":
        if text == "testday3":
            user_state[user_id] = "day3_page1_wait"
            from day3 import send_day3_page1
            await send_day3_page1(message)
        else:
            pass

    # День 3
    elif user_state.get(user_id) == "day3_page1_wait":
        if "рапунцель" in text:
            user_state[user_id] = "day3_page1_done"
            from day3 import send_day3_page1_done
            await send_day3_page1_done(message)
        else:
            pass


    elif user_state.get(user_id) == "day3_page2_wait1":
        if "12" in text:
            user_state[user_id] = "day3_page2_done"
            from day3 import send_day3_page2_done
            await send_day3_page2_done(message)
        else:
            pass

    elif user_state.get(user_id) == "day3_page3_wait1":
        if "оля" in text:
            user_state[user_id] = "day3_page3_wait2"
            from day3 import send_day3_page3_after_first_word
            await send_day3_page3_after_first_word(message)
        else:
            pass

    # Дни 2 и 3 - аналогично...


# Запуск бота
async def main():
    await bot.delete_webhook(drop_pending_updates=True)
    print("🤖 Бот запущен!")
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())