import vk_api
import time
import random
import json

vk = vk_api.VkApi(token='827c8d56e7ad3fc958acb4d7f681505a3baccd8b1dbac88d1d341c30847aed8da45d8cf9562dfb4c6f664')

users = {}

def get_button(label, color, payload=""):
 return {
     "action": {
         "type": "text",
         "payload": json.dumps(payload),
         "label": label
     },
     "color": color
 }
def main_keyboard():
    keyboard = {
        "one_time": False,
        "buttons": [

            [get_button(label="📰 Медиа 📰", color="primary")],
            [get_button(label="🎲 Игры 🎲", color="primary")],

        ]
    }
    keyboard = json.dumps(keyboard, ensure_ascii=False)
    return keyboard
def trend_keyboard():
 keyboard3tren = {
     "one_time": False,
     "buttons": [[get_button(label="Назад к выбору инструмента", color="negative")],
                 [get_button(label="В начало", color="negative")]
                 ]
 }
 keyboard3tren = json.dumps(keyboard3tren, ensure_ascii=False)
 return keyboard3tren

def rand():
 keyboard3tren = {
     "one_time": False,
     "buttons": [[get_button(label="Еще", color="primary")],
                 [get_button(label="Назад к выбору инструмента", color="negative")],
                 [get_button(label="В начало", color="negative")]
                 ]
 }
 keyboard3tren = json.dumps(keyboard3tren, ensure_ascii=False)
 return keyboard3tren



def write_msg(id, message, keyboard=main_keyboard()):
    vk.method('messages.send', {'user_id': id, 'message': message, 'random_id': random.randint(1, 100000), 'keyboard': keyboard})

def partner_keyboard():
    keyboard3par = {
         "one_time": False,
         "buttons": [
             [get_button(label="🌐 IT", color="primary")],
             [get_button(label="🎚️ Для Производства", color="primary")],
             [get_button(label="🍾 Для Услуги", color="primary")],
             [get_button(label="📄 Юристы", color="primary")],
             [get_button(label="Назад к выбору инструмента", color="negative")],
             [get_button(label="В начало", color="negative")]

         ]
    }
    keyboard3par = json.dumps(keyboard3par, ensure_ascii=False)
    return keyboard3par
def instr_keyboard():
    keyboard3 = {
         "one_time": False,
         "buttons": [

             [get_button(label="🤝 Партнёры", color="primary")],
             [get_button(label="🕶️ Тренды", color="primary")],
             [get_button(label="назад", color="negative")],
             [get_button(label="В начало", color="negative")]

         ]
    }
    keyboard3 = json.dumps(keyboard3, ensure_ascii=False)
    return keyboard3

def categ1_keyboard():
    keyboard3_par_categ1 = {
         "one_time": False,
         "buttons": [
             [get_button(label="Назад к выбору категории", color="negative")],
             [get_button(label="В начало", color="negative")]

         ]
    }
    keyboard3_par_categ1 = json.dumps(keyboard3_par_categ1, ensure_ascii=False)
    return keyboard3_par_categ1


def categ2_keyboard():
    keyboard3_par_categ2 = {
         "one_time": False,
         "buttons": [
             [get_button(label="Назад к выбору категории", color="negative")],
             [get_button(label="В начало", color="negative")]

         ]
    }
    keyboard3_par_categ2 = json.dumps(keyboard3_par_categ2, ensure_ascii=False)
    return keyboard3_par_categ2


def categ3_keyboard():
    keyboard3_par_categ3 = {
         "one_time": False,
         "buttons": [
             [get_button(label="Назад к выбору категории", color="negative")],
             [get_button(label="В начало", color="negative")]

         ]
    }
    keyboard3_par_categ3 = json.dumps(keyboard3_par_categ3, ensure_ascii=False)
    return keyboard3_par_categ3

def categ4_keyboard():
    keyboard3_par_categ4 = {
         "one_time": False,
         "buttons": [
             [get_button(label="Назад к выбору категории", color="negative")],
             [get_button(label="В начало", color="negative")]

         ]
    }
    keyboard3_par_categ4 = json.dumps(keyboard3_par_categ4, ensure_ascii=False)
    return keyboard3_par_categ4

def rost_licn_keyboard():
    keyboard2rod = {
         "one_time": False,
         "buttons": [
             [get_button(label="Назад к выбору категорий", color="negative")],
             [get_button(label="В начало", color="negative")]

         ]
    }
    keyboard2rod = json.dumps(keyboard2rod, ensure_ascii=False)
    return keyboard2rod


def media_keyboard():
    keyboard2 = {
         "one_time": False,
         "buttons": [
             [get_button(label="📈 Саморазвитие!", color="primary")],
             [get_button(label="🚀 Как тебе такое Илон Маск", color="primary")],
             [get_button(label="👶 Воспитание", color="primary")],
             [get_button(label="🌟 Мотивация и карьера!", color="primary")],
             [get_button(label="Рандом", color="primary")],
             [get_button(label="назад", color="negative")],
             [get_button(label="В начало", color="negative")]

         ]
    }
    keyboard2 = json.dumps(keyboard2, ensure_ascii=False)
    return keyboard2

def kon_test():
    keyboard2 = {
         "one_time": False,
         "buttons": [
             [get_button(label="К персонажу", color="primary")],
             [get_button(label="К играм", color="primary")],
             [get_button(label="В начало", color="negative")]

         ]
    }
    keyboard2 = json.dumps(keyboard2, ensure_ascii=False)
    return keyboard2

def samoreal_keyboard():
    keyboard2sam = {
         "one_time": False,
         "buttons": [
             [get_button(label="Назад к выбору категорий", color="negative")],
             [get_button(label="В начало", color="negative")]

         ]
    }
    keyboard2sam = json.dumps(keyboard2sam, ensure_ascii=False)
    return keyboard2sam


def vospit_keyboard():
    keyboard2bos = {
         "one_time": False,
         "buttons": [
             [get_button(label="Назад к выбору категорий", color="negative")],
             [get_button(label="В начало", color="negative")]

         ]
    }
    keyboard2bos = json.dumps(keyboard2bos, ensure_ascii=False)
    return keyboard2bos

def elon_mask_keyboard():
    keyboard2kak = {
         "one_time": False,
         "buttons": [
             [get_button(label="Назад к выбору категорий", color="negative")],
             [get_button(label="В начало", color="negative")]

         ]
    }
    keyboard2kak = json.dumps(keyboard2kak, ensure_ascii=False)
    return keyboard2kak
def opisanie_kto_keyboard():
    keyboard_opisanie = {
         "one_time": False,
         "buttons": [


             [get_button(label="назад к игре", color="negative")],
             [get_button(label="В начало", color="negative")]

         ]
    }
    keyboard_opisanie = json.dumps(keyboard_opisanie, ensure_ascii=False)
    return keyboard_opisanie
def igri_keyboard():
    keyboard1 = {
         "one_time": False,
         "buttons": [

             [get_button(label="💀 Виселица 💀", color="positive")],
             [get_button(label="📊 Кто вы в бизнесе 📊", color="positive")],
             [get_button(label="назад", color="negative")],
             [get_button(label="В начало", color="negative")]

         ]
    }
    keyboard1 = json.dumps(keyboard1, ensure_ascii=False)
    return keyboard1

def visel_keyboard():
    keyboard11 = {
         "one_time": False,
         "buttons": [

             [get_button(label="играть", color="positive")],
             [get_button(label="описание ", color="primary")],
             [get_button(label="назад к выбору игры", color="negative")],
             [get_button(label="В начало", color="negative")]

         ]
    }
    keyboard11 = json.dumps(keyboard11, ensure_ascii=False)
    return keyboard11


def opis_visel():
    keyboard_opis_visel = {
        "one_time": False,
        "buttons": [
            [get_button(label="назад к игре виселица", color="negative")],
            [get_button(label="В начало", color="negative")]

        ]
    }
    keyboard_opis_visel = json.dumps(keyboard_opis_visel, ensure_ascii=False)
    return keyboard_opis_visel

def kto_vi_keyboard():
    keyboard12 = {
         "one_time": False,
         "buttons": [

             [get_button(label="играть в игру", color="positive")],
             [get_button(label="описание игры", color="primary")],
             [get_button(label="назад к играм", color="negative")],
             [get_button(label="В начало", color="negative")]

         ]
    }
    keyboard12 = json.dumps(keyboard12, ensure_ascii=False)
    return keyboard12
def rukovod_keyboard():
    keyboard1211 = {
         "one_time": False,
         "buttons": [

             [get_button(label="да", color="positive")],
             [get_button(label="нет", color="primary")],
             [get_button(label="назад к выбору персонажа", color="negative")],
             [get_button(label="В начало", color="negative")]

         ]
    }
    keyboard1211 = json.dumps(keyboard1211, ensure_ascii=False)
    return keyboard1211

def igrat_bis_keyboard():
    keyboard121 = {
         "one_time": False,
         "buttons": [

             [get_button(label="руководитель", color="positive")],
             [get_button(label="бугалтер", color="positive")],
             [get_button(label="сотрудник", color="positive")],
             [get_button(label="назад к игре", color="negative")],
             [get_button(label="В начало", color="negative")]

         ]
    }
    keyboard121 = json.dumps(keyboard121, ensure_ascii=False)
    return keyboard121

while True:
    bos1 = ["""Финансовые услуги 0+: как управлять деньгами с детства 

    https://rb.ru/story/fintech-children/"""],["""
    Культ домашней работы: так ли полезно для обучения домашнее задание? 

    https://rb.ru/story/homework-cult/ """],["""
    Исследование: подростки считаю чиновников жадными, учителей – требовательными, а себя - ленивыми

    https://rb.ru/news/what-teens-think/"""],["""
    Как родители кидфлюенсеров показывают жизнь своих детей в Instagram
    
    https://rb.ru/story/parents-of-kidfluencers/"""],["""
    О чем лучше спросить ребенка вместо «Кем ты хочешь стать, когда вырастешь?» 
    https://rb.ru/story/kem-stanesh/"""]

    sam1 = ["""Даже миллениалы могут рано выйти на пенсию – и вот как” 
             
    https://rb.ru/story/how-to-retire-early/"""],["""
    5 российских вузов вошли в топ-100 международного рейтинга RUR” 
    
    https://rb.ru/news/5-uni-rur/"""],["""
    Как финхакинг поможет тебе обрести финансовую независимость и начать свое дело” 
    
    https://rb.ru/opinion/finhaking-starts-here/"""],["""
    Учеба за рубежом: 10 ресурсов, где ты найдешь классные стажировки, стипендии и гранты
    
    https://rb.ru/list/study-abroad-10/"""],["""
    Не надо ждать от учеников, чтобы они восхищались тобой». Как студенту превратиться в хорошего репетитора
    
    https://rb.ru/opinion/how-to-become-a-good-one/"""]

    kak1 = ["""Как тебе такое Илон Маск:
    "Как 14-летний школьник создал бизнес с выручкой в миллион"
    
    https://rb.ru/longread/youngrussians/"""],["""
    От первого беспилотника до конференции Microsoft: Как школьница из Краснодара заразилась космосом и спроектировала спутник

    https://rb.ru/interview/schoolgirl-makes-sputnik/"""],[""""
    17-летний сотрудник «ВКонтакте» Кирилл Аверьянов – об IT-индустрии, soft skills и попадании в рейтинг Forbes

    https://rb.ru/interview/interview-kirill-averyanov/"""],["""
    Как я в 16 лет сам научился программировать и поехал в американский офис Microsoft

    https://rb.ru/opinion/self-made-in-16/"""],["""
    Сейчас я уже не ем "Доширак". Как сделать два успешных стартапа к 24 годам"

    https://rb.ru/longread/dbrain/"""]

    rod1 = ["""“Учусь и работаю: 10 приложений для тайм-менеджмента” 
    
    https://rb.ru/list/study-work-10-apps/"""],["""
    Десять книг, которые не дадут скучать на летних каникулах
    https://rb.ru/list/leto-leto/"""],["""
    Как финхакинг поможет тебе обрести финансовую независимость и начать свое дело 
    
    https://rb.ru/opinion/finhaking-starts-here/"""],["""
    Спор помог мне найти свое дело. Как превратить хобби в бизнес и карьеру
    
    https://rb.ru/opinion/hobby-and-career"""],["""
    Как спланировать свою карьеру и не облажаться в процессе
    
    https://rb.ru/opinion/how-to-plan-career/"""]
    
    ran = ["""Финансовые услуги 0+: как управлять деньгами с детства 

    https://rb.ru/story/fintech-children/"""],["""
    Культ домашней работы: так ли полезно для обучения домашнее задание? 

    https://rb.ru/story/homework-cult/ """],["""
    Исследование: подростки считаю чиновников жадными, учителей – требовательными, а себя - ленивыми

    https://rb.ru/news/what-teens-think/"""],["""
    Как родители кидфлюенсеров показывают жизнь своих детей в Instagram
    
    https://rb.ru/story/parents-of-kidfluencers/"""],["""
    О чем лучше спросить ребенка вместо «Кем ты хочешь стать, когда вырастешь?» 
    https://rb.ru/story/kem-stanesh/"""],["""Даже миллениалы могут рано выйти на пенсию – и вот как” 
             
    https://rb.ru/story/how-to-retire-early/"""],["""
    5 российских вузов вошли в топ-100 международного рейтинга RUR” 
    
    https://rb.ru/news/5-uni-rur/"""],["""
    Как финхакинг поможет тебе обрести финансовую независимость и начать свое дело” 
    
    https://rb.ru/opinion/finhaking-starts-here/"""],["""
    Учеба за рубежом: 10 ресурсов, где ты найдешь классные стажировки, стипендии и гранты
    
    https://rb.ru/list/study-abroad-10/"""],["""
    Не надо ждать от учеников, чтобы они восхищались тобой». Как студенту превратиться в хорошего репетитора
    
    https://rb.ru/opinion/how-to-become-a-good-one/"""],["""Как тебе такое Илон Маск:
    "Как 14-летний школьник создал бизнес с выручкой в миллион"
    
    https://rb.ru/longread/youngrussians/"""],["""
    От первого беспилотника до конференции Microsoft: Как школьница из Краснодара заразилась космосом и спроектировала спутник

    https://rb.ru/interview/schoolgirl-makes-sputnik/"""],[""""
    17-летний сотрудник «ВКонтакте» Кирилл Аверьянов – об IT-индустрии, soft skills и попадании в рейтинг Forbes

    https://rb.ru/interview/interview-kirill-averyanov/"""],["""
    Как я в 16 лет сам научился программировать и поехал в американский офис Microsoft

    https://rb.ru/opinion/self-made-in-16/"""],["""
    Сейчас я уже не ем "Доширак". Как сделать два успешных стартапа к 24 годам"

    https://rb.ru/longread/dbrain/"""],["""“Учусь и работаю: 10 приложений для тайм-менеджмента” 
    
    https://rb.ru/list/study-work-10-apps/"""],["""
    Десять книг, которые не дадут скучать на летних каникулах
    https://rb.ru/list/leto-leto/"""],["""
    Как финхакинг поможет тебе обрести финансовую независимость и начать свое дело 
    
    https://rb.ru/opinion/finhaking-starts-here/"""],["""
    Спор помог мне найти свое дело. Как превратить хобби в бизнес и карьеру
    
    https://rb.ru/opinion/hobby-and-career"""],["""
    Как спланировать свою карьеру и не облажаться в процессе
    
    https://rb.ru/opinion/how-to-plan-career/"""]

    kat1 = ["""сделать сайт - 
    1. https://www.divier.ru/ 
    2. https://ru.wix.com/ 
    организовать корпоративную базу данных - 
    1. https://kwork.ru/categories/information-bases 
    2. https://www.bkc.su/bazy_dannyh/ 
    """
            ]

    kat2 = ["""
    дерево - http://www.plasma24.ru/proizvodstvo-izdelij-iz-dereva 
    металл - https://www.metobr-expo.ru/ru/articles/2016/proizvods..
    текстиль - https://www.tdl-textile.ru/ 
    """
            ]

    kat3 = ["""помещение - https://profi.ru/raznoe/realtor/ 
    франшиза - https://topfranchise.ru/catalog/ 
    """
            ]

    kat4 = [""" 
    https://pravoved.ru/lawyers/city/moscow/ 
    https://profi.ru/buhgaltery_i_yuristy/jurist/
    """
            ]
    ludi = ["""Тренды:
                <товар 1>
                <товар 2>
                <товар 3>
                <товар 4>"""
            ]
    messages = vk.method("messages.getConversations", {"offset": 0, "count": 20, "filter": "unanswered"})
    if messages["count"] >= 1:
        id = messages["items"][0]["last_message"]["from_id"]
        body = messages["items"][0]["last_message"]["text"]

        if id not in users:
            users[id] = {"name": body, "state": 1}
            write_msg(id, "Привет! Я Бот с которым ты можешь:поиграть в игры, найти интересные статьи, воспользоваться моими бизнес инструментами. Для начала работы нажмите кнопку", keyboard=main_keyboard())

        else:
            state = users[id]['state']


            if body == "📰 Медиа 📰":
                users[id]['state'] = 2
                write_msg(id, 'Media - это раздел в котором ты можешь быстро и в удобной форме найти статью по интересующей тебя теме 😉', keyboard=media_keyboard())
            elif body == "🔧 Инструменты 🔧":
                users[id]['state'] = 3
                write_msg(id, "Наши инструменты помогут начинающим предпринимателям в поиске партнёров для запуска проекта или актуальных товаров для реализации", keyboard=instr_keyboard())
            elif body == "Рандом":
             users[id]['state'] = 96
             write_msg(id, ran[random.randint(0,len(ran))], keyboard=rand())
            elif body == "Еще":
             users[id]['state'] = 97
             write_msg(id, ran[random.randint(0,len(ran))], keyboard=rand())
            elif body == "🕶️ Тренды":
                users[id]['state'] = 5
                write_msg(id, ludi, keyboard=trend_keyboard())
            elif body == "🤝 Партнёры":
                users[id]['state'] = 6
                write_msg(id, "По категориям отобраны надёжные партнёры которые помогут вам при запуске проекта", keyboard=partner_keyboard())
            elif body == "Назад к выбору инструмента":
                users[id]['state'] = 3
                write_msg(id, "Наши инструменты помогут начинающим предпринимателям в поиске партнёров для запуска проекта или актуальных товаров для реализации", keyboard=instr_keyboard())
            elif body == "назад":
                users[id]['state'] = 1
                write_msg(id, "Выбирай одну из 2 категорий", keyboard=main_keyboard())
            elif body == "🌐 IT":
                users[id]['state'] = 7
                write_msg(id, kat1, keyboard=categ1_keyboard())
            elif body == "🎚️ Для Производства":
                users[id]['state'] = 8
                write_msg(id, kat2, keyboard=categ2_keyboard())
            elif body == "🍾 Для Услуги":
                users[id]['state'] = 9
                write_msg(id, kat3, keyboard=categ3_keyboard())
            elif body == "📄 Юристы":
                users[id]['state'] = 10
                write_msg(id, kat4, keyboard=categ4_keyboard())
            elif body == "Назад к выбору категории":
                users[id]['state'] = 11
                write_msg(id, "По категориям отобраны надёжные партнёры которые помогут вам при запуске проекта", keyboard=partner_keyboard())
            elif body == "📈 Саморазвитие!":
                users[id]['state'] = 12
                for i in range(0,5):
                 write_msg(id, rod1[i], keyboard=rost_licn_keyboard())
            elif body == "Назад к выбору категорий":
                users[id]['state'] = 13
                write_msg(id, 'Медиа - это раздел в котором ты можешь быстро и в удобной форме найти статью по интересующей тебя теме 😉', keyboard=media_keyboard())
            elif body == "К персонажу":
             users[id]['state'] = 94
             write_msg(id, 'Выбери персонажа за которого ты будешь играть', keyboard=igrat_bis_keyboard())
            elif body == "К играм":
             users[id]['state'] = 95
             write_msg(id, 'Выбери во что ты будешь играть', keyboard=igri_keyboard())
            elif body == "🌟 Мотивация и карьера!":
                users[id]['state'] = 14
                for i in range(0,5):
                 write_msg(id, sam1[i], keyboard=vospit_keyboard())
            elif body == "👶 Воспитание":
                users[id]['state'] = 15
                for i in range(0,5):
                 write_msg(id, bos1[i], keyboard=vospit_keyboard())
            elif body == "🚀 Как тебе такое Илон Маск":
                users[id]['state'] = 16
                for i in range(0,5):
                 write_msg(id, kak1[i], keyboard=elon_mask_keyboard())
            elif body == "🎲 Игры 🎲":
                users[id]['state'] = 17
                write_msg(id, 'Игры - раздел в котором ты можешь отвлечься от рутины и сыграть в одну из моих мини-игр 🎲', keyboard=igri_keyboard())
            elif body == "💀 Виселица 💀":
                users[id]['state'] = 18
                write_msg(id, 'Испытай свою удачу, догадливость и смекалку в игре  "Виселица".', keyboard=visel_keyboard())
            elif body == "назад к выбору игры":
                users[id]['state'] = 19
                write_msg(id, 'Игры - раздел в котором ты можешь отвлечься от рутины и сыграть в одну из моих мини-игр 🎲', keyboard=igri_keyboard())
            elif body == "описание":
                users[id]['state'] = 20
                write_msg(id, "Правила просты: тебе будет загадано слово и обозначена категория. Пиши маленькими буквами по 1 букве в чат и попытайся угадать слово за наименьшее колличество попыток.", keyboard=opis_visel())
            elif body == "описание игры":
                users[id]['state'] = 89
                write_msg(id, 'Выберите персонажа и правильно отвечаете на вопросы. Удачи!', keyboard=opisanie_kto_keyboard())
            elif body == "назад к играм":
                users[id]['state'] = 90
                write_msg(id, 'Игры - раздел в котором ты можешь отвлечься от рутины и сыграть в одну из моих мини-игр 🎲', keyboard=igri_keyboard())
            elif body == "назад к игре":
                users[id]['state'] = 91
                write_msg(id, 'Хотите узнать кто вы в бизнесе? Попробуйте свои силы играя за одного из 3 персонажей и результат не заставит себя ждать!', keyboard=kto_vi_keyboard())
            elif body =="назад к выбору персонажа":
                users[id]['state'] = 92
                write_msg(id, 'Выбирай персонажа', keyboard=igrat_bis_keyboard())
            elif body == "назад к игре виселица":
                users[id]['state'] = 21
                write_msg(id, 'Испытай свою удачу, догадливость и смекалку в игре  "Виселица". Все слова разгадываются с маленькой буква', keyboard=visel_keyboard())
            elif body == "📊 Кто вы в бизнесе 📊":
                users[id]['state'] = 22
                users[id]['text'] = ''
                users[id]['text1'] = ""
                write_msg(id, "Хотите узнать кто вы в бизнесе? Попробуйте свои силы играя за одного из 3 персонажей и результат не заставит себя ждать!", keyboard=kto_vi_keyboard())
            elif body == "играть в игру":
                users[id]['state'] = 24
                write_msg(id, "Выбирай персонажа", keyboard=igrat_bis_keyboard())
            elif body == "руководитель":
             users[id]['state'] = 26
             users[id]['ch_vop'] = 1
             users[id]['ch_bal'] = 0
             write_msg(id, "Можно оплатить заправку личного автомобиля бизнес-картой?", keyboard=rukovod_keyboard())
            elif body == 'нет' and users[id]['ch_vop'] == 1:
             users[id]['state'] = 27
             users[id]['ch_vop'] += 1
             users[id]['ch_bal'] += 1
             write_msg(id, "Правильно.Следующий вопрос:Можно оформить сразу 5 бизнес-карт на одну компанию?", keyboard=rukovod_keyboard())
            elif body == 'да' and users[id]['ch_vop'] == 1:
             users[id]['state'] = 28
             users[id]['ch_vop'] += 1
             write_msg(id, "Неправильно.Следующий вопрос:Можно оформить сразу 5 бизнес-карт на одну компанию?", keyboard=rukovod_keyboard())
            elif body == 'да' and users[id]['ch_vop'] == 2:
             users[id]['state'] = 29
             users[id]['ch_vop'] += 1
             users[id]['ch_bal'] += 1
             write_msg(id, "Правильно.Следующий вопрос:Можно установить лимит на расходы по бизнес-карте сотрудника?", keyboard=rukovod_keyboard())
            elif body == 'нет' and users[id]['ch_vop'] == 2:
             users[id]['state'] = 30
             users[id]['ch_vop'] += 1
             write_msg(id, "Неправильно.Следующий вопрос:Можно установить лимит на расходы по бизнес-карте сотрудника?", keyboard=rukovod_keyboard())
            elif body == 'да' and users[id]['ch_vop'] == 3:
             users[id]['state'] = 31
             users[id]['ch_vop'] += 1
             users[id]['ch_bal'] += 1
             write_msg(id, "Правильно.Следующий вопрос:Можно оплатить бизнес-картой деловой ужин с партнером?", keyboard=rukovod_keyboard())
            elif body == 'нет' and users[id]['ch_vop'] == 3:
             users[id]['state'] = 32
             users[id]['ch_vop'] += 1
             write_msg(id, "Неправильно.Следующий вопрос:Можно оплатить бизнес-картой деловой ужин с партнером?", keyboard=rukovod_keyboard())
            elif body == 'да' and users[id]['ch_vop'] == 4:
             users[id]['state'] = 33
             users[id]['ch_vop'] += 1
             users[id]['ch_bal'] += 1
             write_msg(id, "Правильно.Следующий вопрос:Можно оплатить бизнес-картой гостиницу в командировке за границей?", keyboard=rukovod_keyboard())
            elif body == 'нет' and users[id]['ch_vop'] == 4:
             users[id]['state'] = 34
             users[id]['ch_vop'] += 1
             write_msg(id, "Неправильно.Следующий вопрос:Можно оплатить бизнес-картой гостиницу в командировке за границей?", keyboard=rukovod_keyboard())
            elif body == 'да' and users[id]['ch_vop'] == 5:
             users[id]['state'] = 35
             users[id]['ch_vop'] += 1
             users[id]['ch_bal'] += 1
             write_msg(id, "Правильно.Следующий вопрос:Можно оплатить услуги бизнес-картой стилиста для подготовки к встрече с партнерами?", keyboard=rukovod_keyboard())
            elif body == 'нет' and users[id]['ch_vop'] == 5:
             users[id]['state'] = 36
             users[id]['ch_vop'] += 1
             write_msg(id, "Неправильно.Следующий вопрос:Можно оплатить услуги бизнес-картой стилиста для подготовки к встрече с партнерами?", keyboard=rukovod_keyboard())
            elif body == 'нет' and users[id]['ch_vop'] == 6:
             users[id]['state'] = 37
             users[id]['ch_vop'] += 1
             users[id]['ch_bal'] += 1
             write_msg(id, "Правильно.Следующий вопрос:Можно оплатить бизнес-картой корпоративное такси?", keyboard=rukovod_keyboard())
            elif body == 'да' and users[id]['ch_vop'] == 6:
             users[id]['state'] = 38
             users[id]['ch_vop'] += 1
             write_msg(id, "Неправильно.Следующий вопрос:Можно оплатить бизнес-картой корпоративное такси?", keyboard=rukovod_keyboard())
            elif body == 'да' and users[id]['ch_vop'] == 7:
             users[id]['state'] = 39
             users[id]['ch_vop'] += 1
             users[id]['ch_bal'] += 1
             write_msg(id, "Правильно.Следующий вопрос:Можно ли использовать бесконтактную оплату при совершении покупок по бизнес-карте?", keyboard=rukovod_keyboard())
            elif body == 'нет' and users[id]['ch_vop'] == 7:
             users[id]['state'] = 40
             users[id]['ch_vop'] += 1
             write_msg(id, "Неправильно.Следующий вопрос:Можно ли использовать бесконтактную оплату при совершении покупок по бизнес-карте?", keyboard=rukovod_keyboard())
            elif body == 'да' and users[id]['ch_vop'] == 8:
             users[id]['state'] = 41
             users[id]['ch_vop'] += 1
             users[id]['ch_bal'] += 1
             write_msg(id, "Правильно.Следующий вопрос:Можно дать сотруднику свою бизнес-карту, чтобы он оплатил покупки для компании?", keyboard=rukovod_keyboard())
            elif body == 'нет' and users[id]['ch_vop'] == 8:
             users[id]['state'] = 42
             users[id]['ch_vop'] += 1
             write_msg(id, "Неправильно.Следующий вопрос:Можно дать сотруднику свою бизнес-карту, чтобы он оплатил покупки для компании?", keyboard=rukovod_keyboard())
            elif body == 'нет' and users[id]['ch_vop'] == 9:
             users[id]['state'] = 43
             users[id]['ch_vop'] += 1
             users[id]['ch_bal'] += 1
             write_msg(id, "Правильно.Следующий вопрос:Можно оплатить бизнес-картой доставку компьютерной техники через интернет?", keyboard=rukovod_keyboard())
            elif body == 'да' and users[id]['ch_vop'] == 9:
             users[id]['state'] = 44
             users[id]['ch_vop'] += 1
             write_msg(id, "Неправильно.Следующий вопрос:Можно оплатить бизнес-картой доставку компьютерной техники через интернет?", keyboard=rukovod_keyboard())
            elif body == 'да' and users[id]['ch_vop'] == 10:
             users[id]['state'] = 45
             users[id]['ch_vop'] += 1
             users[id]['ch_bal'] += 1
             if users[id]['ch_bal'] == 0 or users[id]['ch_bal'] == 1 or users[id]['ch_bal'] == 2:
              write_msg(id, "Правильно.Ты заработал: "+ str(users[id]['ch_bal']) + ' из 10. Твой ранг: малек', keyboard=kon_test())
             elif users[id]['ch_bal'] == 3 or users[id]['ch_bal'] == 4:
              write_msg(id, "Правильно.Ты заработал: "+ str(users[id]['ch_bal']) + ' из 10. Твой ранг: сельд в бизнесе', keyboard=kon_test())
             elif users[id]['ch_bal'] == 5 or users[id]['ch_bal'] == 6:
              write_msg(id, "Правильно.Ты заработал: "+ str(users[id]['ch_bal']) + ' из 10. Твой ранг: уверенный карась', keyboard=kon_test())
             elif users[id]['ch_bal'] == 7 or users[id]['ch_bal'] == 8:
              write_msg(id, "Правильно.Ты заработал: "+ str(users[id]['ch_bal']) + ' из 10. Твой ранг: акула бизнеса', keyboard=kon_test())
             elif users[id]['ch_bal'] == 9 or users[id]['ch_bal'] == 10:
              write_msg(id, "Правильно.Ты заработал: "+ str(users[id]['ch_bal']) + ' из 10. Твой ранг: кит предпринимательства', keyboard=kon_test())
            elif body == 'нет' and users[id]['ch_vop'] == 10:
             users[id]['state'] = 46
             users[id]['ch_vop'] += 1
             if users[id]['ch_bal'] == 0 or users[id]['ch_bal'] == 1 or users[id]['ch_bal'] == 2:
              write_msg(id, "Неправильно.Ты заработал: " + str(users[id]['ch_bal']) + ' из 10. Твой ранг: малек', keyboard=kon_test())
             elif users[id]['ch_bal'] == 3 or users[id]['ch_bal'] == 4:
              write_msg(id, "Неправильно.Ты заработал: " + str(users[id]['ch_bal']) + ' из 10. Твой ранг: сельд в бизнесе', keyboard=kon_test())
             elif users[id]['ch_bal'] == 5 or users[id]['ch_bal'] == 6:
              write_msg(id, "Неправильно.Ты заработал: " + str(users[id]['ch_bal']) + ' из 10. Твой ранг: уверенный карась', keyboard=kon_test())
             elif users[id]['ch_bal'] == 7 or users[id]['ch_bal'] == 8:
              write_msg(id, "Неправильно.Ты заработал: " + str(users[id]['ch_bal']) + ' из 10. Твой ранг: акула бизнеса', keyboard=kon_test())
             elif users[id]['ch_bal'] == 9 or users[id]['ch_bal'] == 10:
              write_msg(id, "Неправильно.Ты заработал: " + str(users[id]['ch_bal']) + ' из 10. Твой ранг: кит предпринимательства', keyboard=kon_test())
            elif body == "бугалтер":
             users[id]['state'] = 47
             users[id]['ch_vop'] = 1
             users[id]['ch_bal'] = 0
             write_msg(id, "Может ли сотрудник компании оплатить гостиницу в командировке бизнес-картой?", keyboard=rukovod_keyboard())
            elif body == 'да' and users[id]['ch_vop'] == 1:
             users[id]['state'] = 48
             users[id]['ch_vop'] += 1
             users[id]['ch_bal'] += 1
             write_msg(id, "Правильно.Следующий вопрос:Можно зачислить зарплату на бизнес-карту сотрудника?", keyboard=rukovod_keyboard())
            elif body == 'нет' and users[id]['ch_vop'] == 1:
             users[id]['state'] = 49
             users[id]['ch_vop'] += 1
             write_msg(id, "Неправильно.Следующий вопрос:Можно зачислить зарплату на бизнес-карту сотрудника?", keyboard=rukovod_keyboard())
            elif body == 'да' and users[id]['ch_vop'] == 2:
             users[id]['state'] = 50
             users[id]['ch_vop'] += 1
             users[id]['ch_bal'] += 1
             write_msg(id, "Правильно.Следующий вопрос:Можно контролировать траты сотрудников через интернет-банк и менять лимиты?", keyboard=rukovod_keyboard())
            elif body == 'нет' and users[id]['ch_vop'] == 2:
             users[id]['state'] = 51
             users[id]['ch_vop'] += 1
             write_msg(id, "Неправильно.Следующий вопрос:Можно контролировать траты сотрудников через интернет-банк и менять лимиты?", keyboard=rukovod_keyboard())
            elif body == 'да' and users[id]['ch_vop'] == 3:
             users[id]['state'] = 52
             users[id]['ch_vop'] += 1
             users[id]['ch_bal'] += 1
             write_msg(id, "Правильно.Следующий вопрос:Можно оплачивать бизнес-картой покупки в интернете?", keyboard=rukovod_keyboard())
            elif body == 'нет' and users[id]['ch_vop'] == 3:
             users[id]['state'] = 53
             users[id]['ch_vop'] += 1
             write_msg(id, "Неправильно.Следующий вопрос:Можно оплачивать бизнес-картой покупки в интернете?", keyboard=rukovod_keyboard())
            elif body == 'да' and users[id]['ch_vop'] == 4:
             users[id]['state'] = 54
             users[id]['ch_vop'] += 1
             users[id]['ch_bal'] += 1
             write_msg(id, "Правильно.Следующий вопрос:Могут несколько сотрудников пользоваться одной бизнес-картой компании?", keyboard=rukovod_keyboard())
            elif body == 'нет' and users[id]['ch_vop'] == 4:
             users[id]['state'] = 55
             users[id]['ch_vop'] += 1
             write_msg(id, "Неправильно.Следующий вопрос:Могут несколько сотрудников пользоваться одной бизнес-картой компании?", keyboard=rukovod_keyboard())
            elif body == 'нет' and users[id]['ch_vop'] == 5:
             users[id]['state'] = 56
             users[id]['ch_vop'] += 1
             users[id]['ch_bal'] += 1
             write_msg(id, "Правильно.Следующий вопрос:Можно снимать наличные со счета компании в банкомате с помощью бизнес-карты?", keyboard=rukovod_keyboard())
            elif body == 'да' and users[id]['ch_vop'] == 5:
             users[id]['state'] = 57
             users[id]['ch_vop'] += 1
             write_msg(id, "Неправильно.Следующий вопрос:Можно снимать наличные со счета компании в банкомате с помощью бизнес-карты?", keyboard=rukovod_keyboard())
            elif body == 'да' and users[id]['ch_vop'] == 6:
             users[id]['state'] = 58
             users[id]['ch_vop'] += 1
             users[id]['ch_bal'] += 1
             write_msg(id, "Правильно.Следующий вопрос:Можно оплатить бизнес-картой представительские расходы?", keyboard=rukovod_keyboard())
            elif body == 'да' and users[id]['ch_vop'] == 6:
             users[id]['state'] = 59
             users[id]['ch_vop'] += 1
             write_msg(id, "Неправильно.Следующий вопрос:Можно оплатить бизнес-картой представительские расходы?", keyboard=rukovod_keyboard())
            elif body == 'да' and users[id]['ch_vop'] == 7:
             users[id]['state'] = 60
             users[id]['ch_vop'] += 1
             users[id]['ch_bal'] += 1
             write_msg(id, "Правильно.Следующий вопрос:Можно оформить бизнес-карту водителю директора компании для заправки на АЗС?", keyboard=rukovod_keyboard())
            elif body == 'нет' and users[id]['ch_vop'] == 7:
             users[id]['state'] = 61
             users[id]['ch_vop'] += 1
             write_msg(id, "Неправильно.Следующий вопрос:Можно оформить бизнес-карту водителю директора компании для заправки на АЗС?", keyboard=rukovod_keyboard())
            elif body == 'да' and users[id]['ch_vop'] == 8:
             users[id]['state'] = 62
             users[id]['ch_vop'] += 1
             users[id]['ch_bal'] += 1
             write_msg(id, "Правильно.Следующий вопрос:Можно оплатить бизнес-картой авиабилеты для поездки в командировку?", keyboard=rukovod_keyboard())
            elif body == 'нет' and users[id]['ch_vop'] == 8:
             users[id]['state'] = 63
             users[id]['ch_vop'] += 1
             write_msg(id, "Неправильно.Следующий вопрос:Можно оплатить бизнес-картой авиабилеты для поездки в командировку?", keyboard=rukovod_keyboard())
            elif body == 'нет' and users[id]['ch_vop'] == 9:
             users[id]['state'] = 64
             users[id]['ch_vop'] += 1
             users[id]['ch_bal'] += 1
             write_msg(id, "Правильно.Следующий вопрос:Можно оплатить услуги уборки офиса клининговой компании с помощью бизнес-карты?", keyboard=rukovod_keyboard())
            elif body == 'да' and users[id]['ch_vop'] == 9:
             users[id]['state'] = 65
             users[id]['ch_vop'] += 1
             write_msg(id, "Неправильно.Следующий вопрос:Можно оплатить услуги уборки офиса клининговой компании с помощью бизнес-карты?", keyboard=rukovod_keyboard())
            elif body == 'да' and users[id]['ch_vop'] == 10:
             users[id]['state'] = 66
             users[id]['ch_vop'] += 1
             users[id]['ch_bal'] += 1
             if users[id]['ch_bal'] == 0 or users[id]['ch_bal'] == 1 or users[id]['ch_bal'] == 2:
              write_msg(id, "Правильно.Ты заработал: "+ str(users[id]['ch_bal']) + ' из 10. Твой ранг: малек', keyboard=kon_test())
             elif users[id]['ch_bal'] == 3 or users[id]['ch_bal'] == 4:
              write_msg(id, "Правильно.Ты заработал: "+ str(users[id]['ch_bal']) + ' из 10. Твой ранг: сельд в бизнесе', keyboard=kon_test())
             elif users[id]['ch_bal'] == 5 or users[id]['ch_bal'] == 6:
              write_msg(id, "Правильно.Ты заработал: "+ str(users[id]['ch_bal']) + ' из 10. Твой ранг: уверенный карась', keyboard=kon_test())
             elif users[id]['ch_bal'] == 7 or users[id]['ch_bal'] == 8:
              write_msg(id, "Правильно.Ты заработал: "+ str(users[id]['ch_bal']) + ' из 10. Твой ранг: акула бизнеса', keyboard=kon_test())
             elif users[id]['ch_bal'] == 9 or users[id]['ch_bal'] == 10:
              write_msg(id, "Правильно.Ты заработал: "+ str(users[id]['ch_bal']) + ' из 10. Твой ранг: кит предпринимательства', keyboard=kon_test())
            elif body == 'нет' and users[id]['ch_vop'] == 10:
             users[id]['state'] = 67
             users[id]['ch_vop'] += 1
             if users[id]['ch_bal'] == 0 or users[id]['ch_bal'] == 1 or users[id]['ch_bal'] == 2:
              write_msg(id, "Неправильно.Ты заработал: " + str(users[id]['ch_bal']) + ' из 10. Твой ранг: малек', keyboard=kon_test())
             elif users[id]['ch_bal'] == 3 or users[id]['ch_bal'] == 4:
              write_msg(id, "Неправильно.Ты заработал: " + str(users[id]['ch_bal']) + ' из 10. Твой ранг: сельд в бизнесе', keyboard=kon_test())
             elif users[id]['ch_bal'] == 5 or users[id]['ch_bal'] == 6:
              write_msg(id, "Неправильно.Ты заработал: " + str(users[id]['ch_bal']) + ' из 10. Твой ранг: уверенный карась', keyboard=kon_test())
             elif users[id]['ch_bal'] == 7 or users[id]['ch_bal'] == 8:
              write_msg(id, "Неправильно.Ты заработал: " + str(users[id]['ch_bal']) + ' из 10. Твой ранг: акула бизнеса', keyboard=kon_test())
             elif users[id]['ch_bal'] == 9 or users[id]['ch_bal'] == 10:
              write_msg(id, "Неправильно.Ты заработал: " + str(users[id]['ch_bal']) + ' из 10. Твой ранг: кит предпринимательства', keyboard=kon_test())
            elif body == "сотрудник":
             users[id]['state'] = 68
             users[id]['ch_vop'] = 1
             users[id]['ch_bal'] = 0
             write_msg(id, "Можно оплатить бизнес-картой счет в ресторане на встрече с партнерами?", keyboard=rukovod_keyboard())
            elif body == 'да' and users[id]['ch_vop'] == 1:
             users[id]['state'] = 69
             users[id]['ch_vop'] += 1
             users[id]['ch_bal'] += 1
             write_msg(id, "Правильно.Следующий вопрос:Можно одолжить бизнес-карту коллеге?", keyboard=rukovod_keyboard())
            elif body == 'нет' and users[id]['ch_vop'] == 1:
             users[id]['state'] = 70
             users[id]['ch_vop'] += 1
             write_msg(id, "Неправильно.Следующий вопрос:Можно одолжить бизнес-карту коллеге?", keyboard=rukovod_keyboard())
            elif body == 'нет' and users[id]['ch_vop'] == 2:
             users[id]['state'] = 71
             users[id]['ch_vop'] += 1
             users[id]['ch_bal'] += 1
             write_msg(id, "Правильно.Следующий вопрос:Можно оплатить бизнес-картой доставку воды в офис через сайт?", keyboard=rukovod_keyboard())
            elif body == 'да' and users[id]['ch_vop'] == 2:
             users[id]['state'] = 72
             users[id]['ch_vop'] += 1
             write_msg(id, "Неправильно.Следующий вопрос:Можно оплатить бизнес-картой доставку воды в офис через сайт?", keyboard=rukovod_keyboard())
            elif body == 'да' and users[id]['ch_vop'] == 3:
             users[id]['state'] = 73
             users[id]['ch_vop'] += 1
             users[id]['ch_bal'] += 1
             write_msg(id, "Правильно.Следующий вопрос:Можно снять премию с бизнес-карты, чтобы не ждать бухгалтера?", keyboard=rukovod_keyboard())
            elif body == 'нет' and users[id]['ch_vop'] == 3:
             users[id]['state'] = 74
             users[id]['ch_vop'] += 1
             write_msg(id, "Неправильно.Следующий вопрос:Можно снять премию с бизнес-карты, чтобы не ждать бухгалтера?", keyboard=rukovod_keyboard())
            elif body == 'нет' and users[id]['ch_vop'] == 4:
             users[id]['state'] = 75
             users[id]['ch_vop'] += 1
             users[id]['ch_bal'] += 1
             write_msg(id, "Правильно.Следующий вопрос:Можно передать пароль от бизнес-карты руководителю компании?", keyboard=rukovod_keyboard())
            elif body == 'да' and users[id]['ch_vop'] == 4:
             users[id]['state'] = 76
             users[id]['ch_vop'] += 1
             write_msg(id, "Неправильно.Следующий вопрос:Можно передать пароль от бизнес-карты руководителю компании?", keyboard=rukovod_keyboard())
            elif body == 'нет' and users[id]['ch_vop'] == 5:
             users[id]['state'] = 77
             users[id]['ch_vop'] += 1
             users[id]['ch_bal'] += 1
             write_msg(id, "Правильно.Следующий вопрос:Можно оплатить бизнес-картой гостиницу в командировке?", keyboard=rukovod_keyboard())
            elif body == 'да' and users[id]['ch_vop'] == 5:
             users[id]['state'] = 78
             users[id]['ch_vop'] += 1
             write_msg(id, "Неправильно.Следующий вопрос:Можно оплатить бизнес-картой гостиницу в командировке?", keyboard=rukovod_keyboard())
            elif body == 'да' and users[id]['ch_vop'] == 6:
             users[id]['state'] = 79
             users[id]['ch_vop'] += 1
             users[id]['ch_bal'] += 1
             write_msg(id, "Правильно.Следующий вопрос:Можно купить принтер в офис с помощью бизнес-карты?", keyboard=rukovod_keyboard())
            elif body == 'нет' and users[id]['ch_vop'] == 6:
             users[id]['state'] = 80
             users[id]['ch_vop'] += 1
             write_msg(id, "Неправильно.Следующий вопрос:Можно купить принтер в офис с помощью бизнес-карты?", keyboard=rukovod_keyboard())
            elif body == 'да' and users[id]['ch_vop'] == 7:
             users[id]['state'] = 81
             users[id]['ch_vop'] += 1
             users[id]['ch_bal'] += 1
             write_msg(id, "Правильно.Следующий вопрос:Можно оплатить бизнес-картой корпоративное такси?", keyboard=rukovod_keyboard())
            elif body == 'нет' and users[id]['ch_vop'] == 7:
             users[id]['state'] = 82
             users[id]['ch_vop'] += 1
             write_msg(id, "Неправильно.Следующий вопрос:Можно оплатить бизнес-картой корпоративное такси?", keyboard=rukovod_keyboard())
            elif body == 'да' and users[id]['ch_vop'] == 8:
             users[id]['state'] = 83
             users[id]['ch_vop'] += 1
             users[id]['ch_bal'] += 1
             write_msg(id, "Правильно.Следующий вопрос:Можно оплатить бизнес-картой пошив делового костюма?", keyboard=rukovod_keyboard())
            elif body == 'нет' and users[id]['ch_vop'] == 8:
             users[id]['state'] = 84
             users[id]['ch_vop'] += 1
             write_msg(id, "Неправильно.Следующий вопрос:Можно оплатить бизнес-картой пошив делового костюма?", keyboard=rukovod_keyboard())
            elif body == 'нет' and users[id]['ch_vop'] == 9:
             users[id]['state'] = 85
             users[id]['ch_vop'] += 1
             users[id]['ch_bal'] += 1
             write_msg(id, "Правильно.Следующий вопрос:Можно закупить товар на оптовой базе с помощью бизнес-карты?", keyboard=rukovod_keyboard())
            elif body == 'да' and users[id]['ch_vop'] == 9:
             users[id]['state'] = 86
             users[id]['ch_vop'] += 1
             write_msg(id, "Неправильно.Следующий вопрос:Можно закупить товар на оптовой базе с помощью бизнес-карты?", keyboard=rukovod_keyboard())
            elif body == 'да' and users[id]['ch_vop'] == 10:
             users[id]['state'] = 87
             users[id]['ch_vop'] += 1
             users[id]['ch_bal'] += 1
             if users[id]['ch_bal'] == 0 or users[id]['ch_bal'] == 1 or users[id]['ch_bal'] == 2:
              write_msg(id, "Правильно.Ты заработал: "+ str(users[id]['ch_bal']) + ' из 10. Твой ранг: малек', keyboard=kon_test())
             elif users[id]['ch_bal'] == 3 or users[id]['ch_bal'] == 4:
              write_msg(id, "Правильно.Ты заработал: "+ str(users[id]['ch_bal']) + ' из 10. Твой ранг: сельд в бизнесе', keyboard=kon_test())
             elif users[id]['ch_bal'] == 5 or users[id]['ch_bal'] == 6:
              write_msg(id, "Правильно.Ты заработал: "+ str(users[id]['ch_bal']) + ' из 10. Твой ранг: уверенный карась', keyboard=kon_test())
             elif users[id]['ch_bal'] == 7 or users[id]['ch_bal'] == 8:
              write_msg(id, "Правильно.Ты заработал: "+ str(users[id]['ch_bal']) + ' из 10. Твой ранг: акула бизнеса', keyboard=kon_test())
             elif users[id]['ch_bal'] == 9 or users[id]['ch_bal'] == 10:
              write_msg(id, "Правильно.Ты заработал: "+ str(users[id]['ch_bal']) + ' из 10. Твой ранг: кит предпринимательства', keyboard=kon_test())
            elif body == 'нет' and users[id]['ch_vop'] == 10:
             users[id]['state'] = 88
             users[id]['ch_vop'] += 1
             if users[id]['ch_bal'] == 0 or users[id]['ch_bal'] == 1 or users[id]['ch_bal'] == 2:
              write_msg(id, "Неправильно.Ты заработал: " + str(users[id]['ch_bal']) + ' из 10. Твой ранг: малек', keyboard=kon_test())
             elif users[id]['ch_bal'] == 3 or users[id]['ch_bal'] == 4:
              write_msg(id, "Неправильно.Ты заработал: " + str(users[id]['ch_bal']) + ' из 10. Твой ранг: сельд в бизнесе', keyboard=kon_test())
             elif users[id]['ch_bal'] == 5 or users[id]['ch_bal'] == 6:
              write_msg(id, "Неправильно.Ты заработал: " + str(users[id]['ch_bal']) + ' из 10. Твой ранг: уверенный карась', keyboard=kon_test())
             elif users[id]['ch_bal'] == 7 or users[id]['ch_bal'] == 8:
              write_msg(id, "Неправильно.Ты заработал: " + str(users[id]['ch_bal']) + ' из 10. Твой ранг: акула бизнеса', keyboard=kon_test())
             elif users[id]['ch_bal'] == 9 or users[id]['ch_bal'] == 10:
              write_msg(id, "Неправильно.Ты заработал: " + str(users[id]['ch_bal']) + ' из 10. Твой ранг: кит предпринимательства', keyboard=kon_test())
            elif body == "В начало":
             write_msg(id, "Выбирай одну из 2 категорий", keyboard=main_keyboard())
            elif body == "играть":
             users[id]['state'] = 25
             s = ['деньги','финхакинг','предприниматель','акселератор','программирование','бизнес','руководитель','компания','учеба','тор','паук','локи','веном','старк','грут','халк','мстители','наташа','баки','клинт','гарри','гермиона','волондеморт','рон','малфой','добби','квидич','сноу','старк','мормонт','варис']
             ka = ['Rusbase','Rusbase','Rusbase','Rusbase','Rusbase','Rusbase','Rusbase','Rusbase','Rusbase', 'Марвел', 'Марвел', 'Марвел', 'Марвел', 'Марвел', 'Марвел', 'Марвел', 'Марвел', 'Марвел', 'Марвел', 'Марвел', 'Гарри Поттер', 'Гарри Поттер', 'Гарри Поттер', 'Гарри Поттер', 'Гарри Поттер', 'Гарри Поттер', 'Гарри Поттер', 'Игра Престолов', 'Игра Престолов', 'Игра Престолов', 'Игра Престолов']
             users[id]['pop'] = 6
             users[id]['is_bk'] = []
             t = random.choice(s)
             users[id]['text'] = t
             ind = s.index(t)
             k = ka[ind]
             q = len(t)
             w = ''
             while q > 0:
                 w += '*'
                 q -= 1
             users[id]['text1'] = w
             write_msg(id,  "загаданное слово: " + str(users[id]['text1'])+". Категория: " +k+'. У тебя 6 попыток', keyboard=opis_visel())
             print(users[id]['text'])
            elif body.lower() == users[id]['text']:
             users[id]['state'] = 89
             write_msg(id, "Молодец ты отгадал слово. Молодец ты отгадал слово. Если ты хочешь играть еще раз нажми 'начать'", keyboard=visel_keyboard())
             users[id]['text'] == ""
             users[id]['is_bk'] = []
            elif body.lower() != users[id]['text'] and users[id]['text'] != '' and len(body) != 1:
             users[id]['state'] = 90
             write_msg(id, "Неправильное слово. Попробуй писать по буквам.", keyboard=opis_visel())
            elif body.lower() in users[id]['is_bk']:
             users[id]['state'] = 91
             write_msg(id,  "Ты уже писал эту букву. Напиши другую", keyboard=opis_visel())
            elif body.lower() in users[id]['text']:
             users[id]['state'] = 92
             e = []
             users[id]['is_bk'].append(body.lower())
             for i in range(len(users[id]['text'])):
                 if body.lower() == users[id]['text'][i]:
                     e.append(str(body.lower()))
                 else:
                     e.append('*')
             for i in range(len(users[id]['text1'])):
                 if users[id]['text1'][i].isalpha():
                     e[i] = users[id]['text1'][i]
             users[id]['text1'] = ''.join(e)
             if users[id]['text1'] != t:
              write_msg(id, "Ты отгадал букву: " + users[id]['text1'], keyboard=opis_visel())
              e = []
             else:
              write_msg(id, "Молодец ты отгадал слово. Если ты хочешь играть еще раз нажми 'начать'", keyboard=visel_keyboard())
            elif body.lower() not in users[id]['text'] and users[id]['text'] != '':
             users[id]['state'] = 93
             users[id]['pop'] -= 1
             users[id]['is_bk'].append(body.lower())
             if users[id]['pop'] == 0:
              write_msg(id, "У тебя закончились попытки.", keyboard=opis_visel())
             else:
              write_msg(id, "нет такой буквы. У тебя еще "+str(users[id]['pop'])+' попыток', keyboard=opis_visel())
            else:
                write_msg(id, "Не понял тебя")
    time.sleep(1)
