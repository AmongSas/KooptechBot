from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove

key1 = KeyboardButton('/Для_тебя')
key2 = KeyboardButton('/Отметиться') #Вывести сообщение отмечен
key3 = KeyboardButton('/Преподаватели') #Вывести сообщение с сылками
key4 = KeyboardButton('/Новости') #Ссылка на группу вк

kb_client = ReplyKeyboardMarkup(resize_keyboard=True)

kb_client.row(key1,key2)
kb_client.row(key3,key4)


#Клавиатура "для тебя"
keyforu1 = KeyboardButton('/Предметы')
keyforu2 = KeyboardButton('/Расписание')
keyforu3 = KeyboardButton('/ДЗ')
keyforu4 = KeyboardButton('/Ссылки')
keyforu5 = KeyboardButton('/Диплом')
keyforu6= KeyboardButton ('/Назад')
kb_client_foru = ReplyKeyboardMarkup(resize_keyboard=True)
kb_client_foru.row(keyforu1,keyforu2,keyforu3)
kb_client_foru.row(keyforu4, keyforu5, keyforu6)

    # Клавиатура предметы
keysubjects1 = KeyboardButton('/Лекции')
keysubjects2 = KeyboardButton('/Практические')
keysubjects3 = KeyboardButton('/Назад')
kb_client_subjects = ReplyKeyboardMarkup(resize_keyboard=True)
kb_client_subjects.row(keysubjects1,keysubjects2)
kb_client_subjects.row(keysubjects3)

    #Клавиатура Расписание
keyschedule1 = KeyboardButton('/Пары')
keyschedule2 = KeyboardButton('/Звонки')
keyschedule3 = KeyboardButton('/Назад')
kb_client_schedule = ReplyKeyboardMarkup(resize_keyboard=True)
kb_client_schedule.row(keyschedule1,keyschedule2)
kb_client_schedule.row(keyschedule3)

    #Клавиатура ДЗ
keyhometask1 = KeyboardButton('/Группа')
keyhometask2 = KeyboardButton('/Назад')
kb_client_hometask = ReplyKeyboardMarkup(resize_keyboard=True)
kb_client_hometask.row(keyhometask1,keyhometask2)

    #Клавиатура Ссылки
keylinks1 = KeyboardButton('/Чат')
keylinks2 = KeyboardButton('/Назад')
kb_client_links = ReplyKeyboardMarkup(resize_keyboard=True)
kb_client_links.row(keylinks1,keylinks2)
