from aiogram import types, Dispatcher
from create_bot import dp, bot
from keyboards import kb_client, kb_client_subjects, kb_client_hometask, kb_client_links, kb_client_schedule, kb_client_foru
from pathlib import *

current_dir = Path.cwd()
#работа с путями


# @dp.message_handler(commands=['start','help'])
async def command_start(message: types.Message):
    try:
        await bot.send_message(message.from_user.id, 'Добро пожаловать', reply_markup=kb_client)
        await message.delete()
    except:
        await message.reply('Общение с ботом через ЛС \n https://t.me/PKTK_bot')


# ГЛАВНАЯ КЛАВИАТУРА
async def student_foru(message: types.Message):
    await bot.send_message(message.from_user.id, 'Подменю "Для тебя"', reply_markup=kb_client_foru)


async def student_mark(message: types.Message):
    await bot.send_message(message.from_user.id, 'Вы отметились', )


async def student_teachers(message: types.Message):
    await bot.send_message(message.from_user.id, '''Список ссылок''', )


async def news(message: types.Message):
    await bot.send_message(message.from_user.id, 'https://vk.com/ptzkoopteh')


# ДЛЯ ТЕБЯ КЛАВИАТУРА

async def foru_subjects(message: types.Message):
    await bot.send_message(message.from_user.id, 'Предметы', reply_markup=kb_client_subjects)
    # Предметы КЛАВИАТУРА
async def foru_subjects_lecture(message: types.Message):
    await bot.send_message(message.from_user.id, "вывод лекций")
async def foru_subjects_practical(message: types.Message):
    await  bot.send_message(message.from_user.id, "вывод практических")


async def foru_schedule(message: types.Message):
    await bot.send_message(message.from_user.id, 'Расписания', reply_markup=kb_client_schedule)
    # КЛАВИАТУРА РАСПИСАНИЙ
async def foru_schedule_timing(message: types.Message):
    timings_img = Path.read_bytes(current_dir.joinpath(r'handlers\data\timings.jpg'))
    await bot.send_photo(message.from_user.id, photo=timings_img)
    timings_img.close()
    #await  bot.send_message(message.from_user.id, "Фотки не отправляются")a
async def foru_schedule_lessons(message: types.Message):
    await bot.send_message(message.from_user.id, "https://koopteh.onego.ru/student/lessons/")


async def foru_hometasks(message: types.Message):
    await bot.send_message(message.from_user.id, 'Меню ДЗ', reply_markup=kb_client_hometask)
#КЛАВИАТУРА ДЗ
async def foru_hometasks_group(message: types.Message):
    await bot.send_message(message.from_user.id, "Выбери группу")


async def foru_links(message: types.Message):
    await bot.send_message(message.from_user.id, 'Ссылки', reply_markup=kb_client_links)
async def foru_links_chat(message: types.Message):
    await bot.send_message(message.from_user.id, 'Список ссылок чатов', reply_markup=kb_client_links)


async def foru_diploma(message: types.Message):
    await bot.send_message(message.from_user.id, 'Что-то про диплом', )


async def goback(mesage: types.Message):
    await bot.send_message(mesage.from_user.id, 'Главное меню', reply_markup=kb_client)


def register_handlers_client(dp: Dispatcher):
    dp.register_message_handler(command_start, commands=['start', 'help'])
    dp.register_message_handler(student_foru, commands=['Для_тебя'])
    dp.register_message_handler(student_mark, commands=['Отметиться'])
    dp.register_message_handler(student_teachers, commands=['Преподаватели'])
    dp.register_message_handler(news, commands=['Новости'])
    # Для тебя
    dp.register_message_handler(foru_subjects, commands=['Предметы'])
    # предметы-----------------------------------------------------------------
    dp.register_message_handler(foru_subjects_lecture, commands=['Лекции'])
    dp.register_message_handler(foru_subjects_practical, commands=['Практические'])

    dp.register_message_handler(foru_schedule, commands=['Расписание'])
    # Расписание---------------------------------------------------------------
    dp.register_message_handler(foru_schedule_timing, commands=['Звонки'])
    dp.register_message_handler(foru_schedule_lessons, commands=['Пары'])

    dp.register_message_handler(foru_hometasks, commands=['ДЗ'])
    #ДЗ---------------------------------------------------------------
    dp.register_message_handler(foru_hometasks_group, commands=['Группа'])


    dp.register_message_handler(foru_links, commands=['Ссылки'])
    # Ссылки---------------------------------------------------------------
    dp.register_message_handler(foru_links_chat, commands=['Чат'])

    dp.register_message_handler(foru_diploma, commands=['Диплом'])


    dp.register_message_handler(goback, commands=['Назад'])