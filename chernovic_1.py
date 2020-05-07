import vk_api
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
import random
import time, datetime
import requests
import sys
from git import addition
import pymorphy2

vk_session = vk_api.VkApi(
    token='dc59d33f532316392242ba355086b5c35e22623e0fdae6f433d6f17b655b10ce8e95db5790ab60344beb1')
longpoll = VkBotLongPoll(vk_session, '193318026')

flag = False
flag_play = False
slovarik_slov = addition.slovarik_slov_add
attachment_ph_d = addition.attachment_ph_d_add

help_1 = False   # пользователь не ввел один из 3 возможных навыков
help_2 = False   # пользователь не ввел название одной из 3 возможных игр
help_3 = False   # пользователь не ввел ДА / НЕТ / СТОП в навыке "решение"
help_4 = False   # пользователь не ввел Я / ВЫ / СТОП в игре "угадай число"
help_5 = False   # пользователь не ввел ДА / НЕТ / в игре "угадай число" (польз)
help_6 = False   # пользователь не ввел БОЛЬШЕ / МЕНЬШЕ / РАВНО в игре "угадай число" (польз)
help_7 = False   # пользователь не ПЕРЕЗАПУСТИТЬ / НЕ ПЕРЕЗАПУСКАТЬ в игре "угадай число" (польз)
help_8 = False   # пользователь не вводит макс. число в игре "угадай число" (комп)
help_9 = False   # пользователь при угадывании вводит не число в игре "угадай число" (польз)
help_10 = False   # пользователь не ввел ДА / НЕТ  в навыке "погода"
help_11 = False   # пользователь на выбрал тип данных в навыке "погода"
help_12 = False   # пользователь на выбрал время прогноза в навыке "погода"
help_13 = False   # пользователь на выбрал время прогноза в навыке "погода"
help_14 = True   # "для начала работы напишите "начать""

id_d = {'id': 'flag'}


def main(not_first=False, vk=None, event=None):
    global flag, flag_play, id_d, help_1, help_2, help_3, help_4, help_5, \
        help_6, help_7, help_8, help_9, help_10, help_11, help_12, help_13

    if not_first:
        id_d[event.obj.message['from_id']] = {'flag': True, 'flag_play': False,
                                              'number_game': False,
                                              'numb_gm_ii': False,
                                              'find_highest': False,
                                              'numb_gm_polz': False,
                                              'words_game': False,
                                              'rps_game': False,
                                              'decision': False,
                                              'form_procc': True,
                                              'weather_fl': False,
                                              'city_fl_pr': False,
                                              'w_weather': False,
                                              'w_time': False,
                                              'this_moment': False,
                                              'certain_time': False,
                                              'help': [True, False, False,
                                                       False, False, False,
                                                       False, False, False,
                                                       False, False, False,
                                                       False, False]}
        vk.messages.send(user_id=event.obj.message['from_id'],
                         message="Вот что я могу:\n"
                                 "Игры\n"\
                                 "Погода\n"\
                                 "Помочь принять решение",
                         keyboard=open('keyboard_menu.json', 'r', encoding='UTF-8').read(),
                         random_id=random.randint(0, 2 ** 64))

    for event in longpoll.listen():
        vk = vk_session.get_api()
        if event.type == VkBotEventType.MESSAGE_NEW and\
                event.obj.message['from_id'] not in id_d.keys():
            id_d[event.obj.message['from_id']] = {'flag': False, 'flag_play': False,
                                              'number_game': False,
                                              'numb_gm_ii': False,
                                              'find_highest': False,
                                              'numb_gm_polz': False,
                                              'words_game': False,
                                              'rps_game': False,
                                              'decision': False,
                                              'form_procc': True,
                                              'weather_fl': False,
                                              'city_fl_pr': False,
                                              'w_weather': False,
                                              'w_time': False,
                                              'this_moment': False,
                                              'certain_time': False,
                                              'help': [False, False, False,
                                                       False, False, False,
                                                       False, False, False,
                                                       False, False, False,
                                                       False, True]}
            print(event.obj.message['from_id'])
            print(id_d)
        if event.type == VkBotEventType.MESSAGE_NEW and event.obj.message[
            'text'].lower() == 'начать' and not id_d[event.obj.message['from_id']]['flag']:
            id_d[event.obj.message['from_id']]['flag'] = True

            id_d[event.obj.message['from_id']]['help'][13] = False
            id_d[event.obj.message['from_id']]['help'][0] = True

            print(event)
            print('Новое сообщение:')
            print('Для меня от:', event.obj.message['from_id'])
            print('Текст:', event.obj.message['text'])
            vk.messages.send(user_id=event.obj.message['from_id'],
                             message="Привет я бот ЯЛ\n"
                                     "и вот что я могу:\n"
                                     "Игры\n"
                                     "Погода\n"
                                     "Помочь принять решение",
                             attachment=random.choice(attachment_ph_d['hi']),
                             keyboard=open('keyboard_menu.json', 'r', encoding='UTF-8').read(),
                             random_id=random.randint(0, 2 ** 64))

        elif event.type == VkBotEventType.MESSAGE_NEW and 'игр' in \
                event.obj.message['text'].lower() and id_d[event.obj.message['from_id']]['flag']:
            id_d[event.obj.message['from_id']]['flag_play'] = True
            id_d[event.obj.message['from_id']]['number_game'] = False
            id_d[event.obj.message['from_id']]['numb_gm_ii'] = False
            id_d[event.obj.message['from_id']]['numb_gm_polz'] = False

            id_d[event.obj.message['from_id']]['help'][0] = False
            id_d[event.obj.message['from_id']]['help'][1] = True

            vk.messages.send(user_id=event.obj.message['from_id'],
                             message="Можем поиграть в:\n"
                                     "Камень-ножницы-бумага\n"
                                     "Угадай число\n"
                                     "Слова\n"
                                     "Чтобы выбрать, напиши цифру в скобках",
                             attachment=random.choice(attachment_ph_d['game']),
                             keyboard=open('keyboard_play.json', 'r',
                                           encoding='UTF-8').read(),
                             random_id=random.randint(0, 2 ** 64))

        elif event.type == VkBotEventType.MESSAGE_NEW and "камень-ножницы-бумага" in event.obj.message[
            'text'].lower() and id_d[event.obj.message['from_id']]['flag'] \
                and id_d[event.obj.message['from_id']]['flag_play'] and \
                not(id_d[event.obj.message['from_id']]['number_game'] or
                    id_d[event.obj.message['from_id']]['rps_game'] or
                    id_d[event.obj.message['from_id']]['words_game']):
            id_d[event.obj.message['from_id']]['rps_game'] = True

            id_d[event.obj.message['from_id']]['help'][1] = False
            vk.messages.send(user_id=event.obj.message['from_id'],
                             message="Название: Камень-ножницы-бумага"
                                     "Сейчас пойдет отсчет до 5 и на цифре пять " 
                                     "Вам нужно отправить:"
                                     "КАМЕНЬ, НОЖНИЦЫ или БУМАГА\n"
                                     "Памятка:\n"
                                     "Бумага бьёт камень, но боится ножниц.\n"
                                     "Камень бьёт ножницы, но боится бумагу.\n"
                                     "Ножницы бьют бумагу, но боятся камня.\n"
                                     "Для продолжения напишите ДА\n"
                                     "Если не хотите играть - НЕТ",
                             attachment=random.choice(attachment_ph_d['r-p-s']),
                             keyboard=open('keyboard_y_n.json', 'r', encoding='UTF-8').read(),
                             random_id=random.randint(0, 2 ** 64))

        elif event.type == VkBotEventType.MESSAGE_NEW and \
                id_d[event.obj.message['from_id']]['flag_play']\
                and id_d[event.obj.message['from_id']]['rps_game'] and not\
                (id_d[event.obj.message['from_id']]['number_game'] and
                 id_d[event.obj.message['from_id']]['words_game']):
            if event.obj.message['text'].lower() == 'да':
                rock_paper_scissors(vk, event)
            elif event.obj.message['text'].lower() == 'нет':
                id_d[event.obj.message['from_id']]['help'][0] = True
                main(True, vk, event)
            else:
                text = "Для продолжения напишите ДА\n" \
                       "Если не хотите играть - НЕТ"
                vk.messages.send(user_id=event.obj.message['from_id'],
                                 message=text,
                                 keyboard=open('keyboard_y_n.json', 'r',
                                               encoding='UTF-8').read(),
                                 random_id=random.randint(0, 2 ** 64))

        elif event.type == VkBotEventType.MESSAGE_NEW and event.obj.message[
            'text'].lower() == 'слова' and id_d[event.obj.message['from_id']]['flag'] and \
                id_d[event.obj.message['from_id']]['flag_play'] and not\
                (id_d[event.obj.message['from_id']]['number_game'] or
                 id_d[event.obj.message['from_id']]['rps_game'] or
                 id_d[event.obj.message['from_id']]['words_game']):
            id_d[event.obj.message['from_id']]['words_game'] = True

            id_d[event.obj.message['from_id']]['help'][1] = False
            text = "Название: Игра в слова\n"\
                   "Правила очень просты! Вы называете любое слово,\n"\
                   "а я называю слово, первая буква которого совпадает с"\
                   " последней буквой Вашего слова.\n"\
                   "Если названо слово, заканчивающееся на Й, Ы, Ъ, Ь,\n"\
                   " следующему игроку нужно придумать слово на предпоследню"\
                   " букву.\n"\
                   "Слова в процессе однного кона игры не должны повторяться.\n"\
                   "Нельзя использовать имена прилагательные и имена собственные.\n"   \
                   "Для продолжения напишите ДА\n"\
                   "Если не хотите играть - НЕТ\n"\
                   "Если во время игры Вы не знаете слово"\
                   " или надоело играть - напишите СДАЮСЬ"
            vk.messages.send(user_id=event.obj.message['from_id'],
                             message=text,
                             attachment=random.choice(attachment_ph_d['words']),
                             keyboard=open('keyboard_y_n.json', 'r', encoding='UTF-8').read(),
                             random_id=random.randint(0, 2 ** 64))

        elif event.type == VkBotEventType.MESSAGE_NEW and \
                id_d[event.obj.message['from_id']]['flag_play'] \
                and id_d[event.obj.message['from_id']]['words_game'] and not (
                id_d[event.obj.message['from_id']]['number_game'] and
                 id_d[event.obj.message['from_id']]['rps_game']):
            if event.type == VkBotEventType.MESSAGE_NEW and \
                    event.obj.message['text'].lower() == 'да':
                slova(vk, event)
            elif event.type == VkBotEventType.MESSAGE_NEW and \
                    event.obj.message['text'].lower() == 'нет':
                id_d[event.obj.message['from_id']]['help'][0] = True
                main(True, vk, event)
            else:
                text = "Для продолжения напишите ДА\n" \
                       "Если не хотите играть - НЕТ"
                vk.messages.send(user_id=event.obj.message['from_id'],
                                 message=text,
                                 keyboard=open('keyboard_y_n.json', 'r',
                                               encoding='UTF-8').read(),
                                 random_id=random.randint(0, 2 ** 64))

        elif event.type == VkBotEventType.MESSAGE_NEW and 'число' in event.obj.message[
            'text'] and id_d[event.obj.message['from_id']]['flag'] and \
                id_d[event.obj.message['from_id']]['flag_play'] and not(
                id_d[event.obj.message['from_id']]['number_game'] or
                id_d[event.obj.message['from_id']]['rps_game'] or
                id_d[event.obj.message['from_id']]['words_game']):
            id_d[event.obj.message['from_id']]['number_game'] = True

            id_d[event.obj.message['from_id']]['help'][1] = False
            id_d[event.obj.message['from_id']]['help'][3] = True
            vk.messages.send(user_id=event.obj.message['from_id'],
                             message="Название: Угадай число\n"
                                     "Один из нас - Я или ВЫ - загадывает число от 1 до 999.\n"
                                     "Другой начинает угадывать, называя числа, "
                                     "получая в ответ фразы 'больше' или 'меньше'.\n"
                                     "'Меньше' - загаданное число меньше Вашего.\n"
                                     "'Больше' - загаданное число больше Вашего.\n"
                                     "Напишите СТОП - если хотите завершить игру\n"
                                     "Кто загадывает число: Я или ВЫ?",
                             attachment=random.choice(attachment_ph_d['number']),
                             random_id=random.randint(0, 2 ** 64))

        elif event.type == VkBotEventType.MESSAGE_NEW and \
                ((event.obj.message['text'].lower() == 'я' and
                  id_d[event.obj.message['from_id']]['flag'] and
                  id_d[event.obj.message['from_id']]['number_game'] ) or
                 (event.obj.message['text'].lower() in ["перезапустить", "не перезапускать"]
                  and id_d[event.obj.message['from_id']]['flag'] and
                  id_d[event.obj.message['from_id']]['number_game'] and
                  id_d[event.obj.message['from_id']]['numb_gm_polz']) or
                 (event.obj.message['text'].lower() == "стоп" and
                  id_d[event.obj.message['from_id']]['flag'] and
                  id_d[event.obj.message['from_id']]['number_game'] )):
            id_d[event.obj.message['from_id']]['help'][3] = False
            id_d[event.obj.message['from_id']]['help'][6] = False

            id_d[event.obj.message['from_id']]['numb_gm_polz'] = True
            numb_gm_p_cl = NumberGamePolz(id_d[event.obj.message['from_id']]['number_game'],
                                          id_d[event.obj.message['from_id']]['numb_gm_polz'],
                                          True)

            if event.obj.message['text'].lower() in ["не перезапускать", "стоп"]:
                id_d[event.obj.message['from_id']]['number_game'] = False
                id_d[event.obj.message['from_id']]['numb_gm_polz'] = False
                id_d[event.obj.message['from_id']]['help'][0] = True
                main(True, vk, event)
            else:
                text = "Хорошо. Загадывайте число.\n" \
                       "Загадали? ДА / НЕТ"

                id_d[event.obj.message['from_id']]['help'][4] = True

                vk.messages.send(user_id=event.obj.message['from_id'],
                                 message=text,
                                 keyboard=open('keyboard_y_n.json', 'r', encoding='UTF-8').read(),
                                 random_id=random.randint(0, 2 ** 64))

        elif event.type == VkBotEventType.MESSAGE_NEW and event.obj.message[
            'text'].lower() in ['нет', 'да'] and \
                id_d[event.obj.message['from_id']]['flag'] and \
                id_d[event.obj.message['from_id']]['number_game'] and \
                id_d[event.obj.message['from_id']]['numb_gm_polz']:
            if event.obj.message['text'].lower() == 'нет':

                text = "Ладно, я могу подождать.\n" \
                       "А теперь загадали? ДА / НЕТ"

                vk.messages.send(user_id=event.obj.message['from_id'],
                                 message=text,
                                 attachment=random.choice(attachment_ph_d['wait']),
                                 keyboard=open('keyboard_y_n.json', 'r', encoding='UTF-8').read(),
                                 random_id=random.randint(0, 2 ** 64))

            else:
                id_d[event.obj.message['from_id']]['help'][4] = False
                id_d[event.obj.message['from_id']]['help'][5] = True

                text = "Хорошо. Начинаю угадывать\n"

                vk.messages.send(user_id=event.obj.message['from_id'],
                                 message=text,
                                 random_id=random.randint(0, 2 ** 64))

                vk.messages.send(user_id=event.obj.message['from_id'],
                                 message=numb_gm_p_cl.number_game_st(),
                                 random_id=random.randint(0, 2 ** 64))

        elif event.type == VkBotEventType.MESSAGE_NEW and event.obj.message[
            'text'].lower() in ['больше', 'меньше', 'равно'] and \
                id_d[event.obj.message['from_id']]['flag'] \
                and id_d[event.obj.message['from_id']]['number_game'] and \
                id_d[event.obj.message['from_id']]['numb_gm_polz']:
            if numb_gm_p_cl.minim < numb_gm_p_cl.maxim - 1:

                id_d[event.obj.message['from_id']]['help'][5], \
                id_d[event.obj.message['from_id']]['help'][6], \
                text = numb_gm_p_cl.numb_game_plz_func(event.obj.message['text'].lower())

                vk.messages.send(user_id=event.obj.message['from_id'],
                                 message=text,
                                 random_id=random.randint(0, 2 ** 64))
            else:
                text = "Должно быть, Вы ошиблись.\n" \
                       "Такого числа нет в диапазоне от 1 до 1000"

                vk.messages.send(user_id=event.obj.message['from_id'],
                                 message=text,
                                 attachment=random.choice(attachment_ph_d['fail']),
                                 random_id=random.randint(0, 2 ** 64))
        elif event.type == VkBotEventType.MESSAGE_NEW and \
                ((event.obj.message['text'].lower() == 'вы'
                  and id_d[event.obj.message['from_id']]['flag'] and
                  id_d[event.obj.message['from_id']]['number_game'] ) or
                 (event.obj.message['text'].lower() in ["перезапустить",
                                                        "не перезапускать", "стоп"]
                  and id_d[event.obj.message['from_id']]['flag'] and
                  id_d[event.obj.message['from_id']]['number_game'] and
                  id_d[event.obj.message['from_id']]['numb_gm_ii']) or
                 (event.obj.message['text'].lower() == "стоп" and
                  id_d[event.obj.message['from_id']]['flag'] and
                  id_d[event.obj.message['from_id']]['number_game'] )):
            id_d[event.obj.message['from_id']]['help'][3] = False
            id_d[event.obj.message['from_id']]['help'][6] = False

            id_d[event.obj.message['from_id']]['numb_gm_ii'] = True
            id_d[event.obj.message['from_id']]['find_highest'] = False

            numb_gm_ii_cl = NumberGameII(id_d[event.obj.message['from_id']]['number_game'],
                                         id_d[event.obj.message['from_id']]['numb_gm_ii'],
                                         id_d[event.obj.message['from_id']]['find_highest'],
                                         False)

            if event.obj.message['text'].lower() in ["не перезапускать", "стоп"]:
                id_d[event.obj.message['from_id']]['number_game'], \
                id_d[event.obj.message['from_id']]['numb_gm_ii'], \
                id_d[event.obj.message['from_id']]['find_highest'] = False, False, False
                id_d[event.obj.message['from_id']]['help'][0] = True
                main(True, vk, event)
            else:
                id_d[event.obj.message['from_id']]['help'][7] = True
                text = "Введите максимальное число, которое мне можно загадать\n" \
                       "Минимальное число - 0"

                vk.messages.send(user_id=event.obj.message['from_id'],
                                 message=text,
                                 random_id=random.randint(0, 2 ** 64))

        elif event.type == VkBotEventType.MESSAGE_NEW and event.obj.message[
            'text'].isdigit() and id_d[event.obj.message['from_id']]['flag'] \
                and id_d[event.obj.message['from_id']]['number_game'] and \
                id_d[event.obj.message['from_id']]['numb_gm_ii']:
            id_d[event.obj.message['from_id']]['help'][7] = False

            if not id_d[event.obj.message['from_id']]['find_highest']:
                id_d[event.obj.message['from_id']]['number_game'], \
                id_d[event.obj.message['from_id']]['numb_gm_polz'], \
                id_d[event.obj.message['from_id']]['find_highest'], \
                id_d[event.obj.message['from_id']]['help'][8], text = \
                    numb_gm_ii_cl.highest(event.obj.message['text'].lower())

                vk.messages.send(user_id=event.obj.message['from_id'],
                                 message=text,
                                 random_id=random.randint(0, 2 ** 64))
            else:

                text, id_d[event.obj.message['from_id']]['help'][8], \
                id_d[event.obj.message['from_id']]['help'][6] = \
                    numb_gm_ii_cl.numb_game_ii_func(event.obj.message['text'].lower())

                vk.messages.send(user_id=event.obj.message['from_id'],
                                 message=text,
                                 random_id=random.randint(0, 2 ** 64))

        elif event.type == VkBotEventType.MESSAGE_NEW and 'решение' in event.obj.message[
            'text'].lower() and id_d[event.obj.message['from_id']]['flag'] and \
                id_d[event.obj.message['from_id']]['form_procc'] and not(
                id_d[event.obj.message['from_id']]['number_game'] and
                id_d[event.obj.message['from_id']]['words_game'] and
                 id_d[event.obj.message['from_id']]['rps_game'] ):

            id_d[event.obj.message['from_id']]['help'][0] = False
            id_d[event.obj.message['from_id']]['help'][2] = True

            id_d[event.obj.message['from_id']]['decision'] = True
            id_d[event.obj.message['from_id']]['form_procc'] = True
            kit = []

            vk.messages.send(user_id=event.obj.message['from_id'],
                             message="Я могу Вам помочь выбрать что-то "
                                     "из определённой последовательнсти "
                                     "предметов, которую Вы назовёте.\n"
                                     "Нужна такая помощь? ДА / НЕТ\n"
                                     "Напишите СТОП - если хотите завершить навык\n",
                             keyboard=open('keyboard_y_n.json', 'r', encoding='UTF-8').read(),
                             random_id=random.randint(0, 2 ** 64))

        elif event.type == VkBotEventType.MESSAGE_NEW and \
                ((event.obj.message['text'].lower() in [
                    'нет', 'да', "перезапустить", "не перезапускать", "стоп"]
                  and id_d[event.obj.message['from_id']]['flag'] and
                  id_d[event.obj.message['from_id']]['decision'] and
                  id_d[event.obj.message['from_id']]['form_procc']) or
                 (event.obj.message['text'].lower() == "стоп" and
                  id_d[event.obj.message['from_id']]['flag'] and
                  id_d[event.obj.message['from_id']]['decision'] and
                  not id_d[event.obj.message['from_id']]['form_procc'])):
            id_d[event.obj.message['from_id']]['help'][2] = False
            if event.obj.message['text'].lower() in ['нет', "не перезапускать", "стоп"]:

                text = "Ладно...А я ведь просто хотел помочь."

                id_d[event.obj.message['from_id']]['decision'] = False
                id_d[event.obj.message['from_id']]['form_procc'] = True
                id_d[event.obj.message['from_id']]['help'][0] = True
                vk.messages.send(user_id=event.obj.message['from_id'],
                                 message=text,
                                 attachment=random.choice(attachment_ph_d['sad']),
                                 random_id=random.randint(0, 2 ** 64))

                main(True, vk, event)

            else:
                id_d[event.obj.message['from_id']]['form_procc'] = False
                kit = []
                text = f"Ура, ура, ура! Я с радостью Вам помогу.\n" \
                       "Отдельными сообщениями введите все элементы последовательности, из которой" \
                       "мне нужно будет выбрать.\n" \
                       "В конце введите слово - ВЫБИРАЙ"
                vk.messages.send(user_id=event.obj.message['from_id'],
                                 message=text,
                                 attachment=random.choice(attachment_ph_d['choice']),
                                 random_id=random.randint(0, 2 ** 64))

        elif event.type == VkBotEventType.MESSAGE_NEW and id_d[event.obj.message['from_id']]['flag'] \
                and id_d[event.obj.message['from_id']]['decision'] and \
                not id_d[event.obj.message['from_id']]['form_procc'] and \
                event.obj.message['text'].lower() == "выбирай":
            id_d[event.obj.message['from_id']]['form_procc'] = True

            vk.messages.send(user_id=event.obj.message['from_id'],
                             message=f"Думаю, что {random.choice(kit)} - "
                                     "идеальный вариант!\n"
                                     "Напишите мне -  ПЕРЕЗАПУСТИТЬ навык / НЕ ПЕРЕЗАПУСКАТЬ",
                             keyboard=open('keyboard_strat_notstart.json', 'r',
                                           encoding='UTF-8').read(),
                             random_id=random.randint(0, 2 ** 64))

        elif event.type == VkBotEventType.MESSAGE_NEW and \
                id_d[event.obj.message['from_id']]['flag'] and \
                id_d[event.obj.message['from_id']]['decision'] and not \
                id_d[event.obj.message['from_id']]['form_procc']:
            kit.append(event.obj.message['text'])

        elif event.type == VkBotEventType.MESSAGE_NEW and \
                not id_d[event.obj.message['from_id']]['decision']\
                and not id_d[event.obj.message['from_id']]['flag_play']and \
                (('погод' in event.obj.message['text'].lower() and
                  id_d[event.obj.message['from_id']]['flag'] and
                  not id_d[event.obj.message['from_id']]['weather_fl'])
                 or (event.obj.message['text'].lower() and
                     id_d[event.obj.message['from_id']]['flag'] and
                     id_d[event.obj.message['from_id']]['weather_fl']
                     and id_d[event.obj.message['from_id']]['city_fl_pr'])
                 or (event.obj.message['text'].lower() == 'стоп' and
                     id_d[event.obj.message['from_id']]['flag'] and
                     id_d[event.obj.message['from_id']]['weather_fl'])):

            id_d[event.obj.message['from_id']]['help'][0] = False

            if not id_d[event.obj.message['from_id']]['weather_fl']:
                id_d[event.obj.message['from_id']]['weather_fl'] = True
                id_d[event.obj.message['from_id']]['city_fl_pr'] = True

                text = "С радостью Вам помогу! Назовите название города, данные " \
                       "для которого Вы хотели бы получить.\n" \
                       "Для выхода напишите СТОП"

                vk.messages.send(user_id=event.obj.message['from_id'],
                                 message=text,
                                 attachment=random.choice(attachment_ph_d['planet']),
                                 random_id=random.randint(0, 2 ** 64))

            elif event.obj.message['text'].lower() == "стоп":
                id_d[event.obj.message['from_id']]['weather_fl'] = False
                id_d[event.obj.message['from_id']]['city_fl_pr'] = False
                id_d[event.obj.message['from_id']]['w_weather'] = False
                id_d[event.obj.message['from_id']]['w_time'] = False
                id_d[event.obj.message['from_id']]['help'][0] = True

                text = "Ладно...А я ведь просто хотел помочь."

                vk.messages.send(user_id=event.obj.message['from_id'],
                                 message=text,
                                 attachment=random.choice(attachment_ph_d['sad']),
                                 random_id=random.randint(0, 2 ** 64))
                main(True, vk, event)
            else:
                if id_d[event.obj.message['from_id']]['city_fl_pr']:
                    city = event.obj.message['text'].lower()

                    city_cl = Cities(city)

                    if len(city_cl.search(city)) == 3:

                        long, latt, city = city_cl.search(city)
                        id_d[event.obj.message['from_id']]['city_fl_pr'] = False
                        id_d[event.obj.message['from_id']]['help'][9] = True

                        text = f"Вы хотите получить данные о городе {city}?\n"\
                            "ДА или НЕТ\n"

                        vk.messages.send(user_id=event.obj.message['from_id'],
                                         message=text,
                                         attachment=random.choice(attachment_ph_d['city']),
                                         keyboard=open('keyboard_y_n.json', 'r',
                                                       encoding='UTF-8').read(),
                                         random_id=random.randint(0, 2 ** 64))
                    else:
                        text = city_cl.search(city)

                        vk.messages.send(user_id=event.obj.message['from_id'],
                                         message=text,
                                         keyboard=open('keyboard_y_n.json', 'r',
                                                       encoding='UTF-8').read(),
                                         random_id=random.randint(0, 2 ** 64))

        elif event.type == VkBotEventType.MESSAGE_NEW and event.obj.message[
            'text'].lower()in ['да', 'нет'] and id_d[event.obj.message['from_id']]['flag'] \
                and id_d[event.obj.message['from_id']]['weather_fl'] and \
                not id_d[event.obj.message['from_id']]['city_fl_pr']:
            id_d[event.obj.message['from_id']]['help'][9] = False

            if event.obj.message['text'].lower() == 'да':
                id_d[event.obj.message['from_id']]['city_fl_pr'] = False
                id_d[event.obj.message['from_id']]['help'][10] = True

                text = f"Какие данные Вы бы хотели получить для города {city}?\n" \
                    "Данные о погоде(1)\n" \
                    "Данные о времени(2)\n"
                vk.messages.send(user_id=event.obj.message['from_id'],
                                 message=text,
                                 keyboard=open('keyboard_time_wehar.json', 'r',
                                               encoding='UTF-8').read(),
                                 random_id=random.randint(0, 2 ** 64))
            else:
                id_d[event.obj.message['from_id']]['city_fl_pr'] = True
                text = "Повторите ввод названия города"

                vk.messages.send(user_id=event.obj.message['from_id'],
                                 message=text,
                                 random_id=random.randint(0, 2 ** 64))

        elif event.type == VkBotEventType.MESSAGE_NEW and event.obj.message['text']\
                in ['1', '2'] and id_d[event.obj.message['from_id']]['flag'] and \
                id_d[event.obj.message['from_id']]['weather_fl'] and \
                not id_d[event.obj.message['from_id']]['city_fl_pr'] and \
                not id_d[event.obj.message['from_id']]['w_weather'] and \
                not id_d[event.obj.message['from_id']]['w_time']:
            id_d[event.obj.message['from_id']]['help'][10] = False
            if event.obj.message['text'] == "1":
                id_d[event.obj.message['from_id']]['w_weather'] = True
                id_d[event.obj.message['from_id']]['help'][11] = True

                text = "Прогноз погоды на:\n" \
                       "Данный момент (1)\n" \
                       "Определенное время (2)\n"

                vk.messages.send(user_id=event.obj.message['from_id'],
                                 message=text,
                                 attachment=random.choice(attachment_ph_d['weather']),
                                 random_id=random.randint(0, 2 ** 64))
            else:
                id_d[event.obj.message['from_id']]['help'][0] = True
                id_d[event.obj.message['from_id']]['w_time'] = True

                weather_cl = Weather(city, False, latt, long, id_d[event.obj.message['from_id']]['w_weather'])
                text = weather_cl.response_d('')
                vk.messages.send(user_id=event.obj.message['from_id'],
                                 message=text,
                                 random_id=random.randint(0, 2 ** 64))
                main(True, vk, event)

        elif event.type == VkBotEventType.MESSAGE_NEW and \
                ((event.obj.message['text'] in ['1', '2'] and
                  id_d[event.obj.message['from_id']]['flag'] and
                  id_d[event.obj.message['from_id']]['weather_fl'] and
                  not id_d[event.obj.message['from_id']]['city_fl_pr'] and \
                id_d[event.obj.message['from_id']]['w_weather'] and
                  not id_d[event.obj.message['from_id']]['w_time'] and
                  not id_d[event.obj.message['from_id']]['this_moment'] and
                  not id_d[event.obj.message['from_id']]['certain_time']) or
                 (event.obj.message['text'] in ['1', '2', '3', '4'] and
                  id_d[event.obj.message['from_id']]['flag'] and
                  id_d[event.obj.message['from_id']]['weather_fl'] and
                  not id_d[event.obj.message['from_id']]['city_fl_pr'] and \
                id_d[event.obj.message['from_id']]['w_weather'] and
                  not id_d[event.obj.message['from_id']]['w_time'] and
                  (id_d[event.obj.message['from_id']]['this_moment'] or
                   id_d[event.obj.message['from_id']]['certain_time']))):

            if event.obj.message['text'] == '1' and \
                    not id_d[event.obj.message['from_id']]['certain_time']:
                id_d[event.obj.message['from_id']]['help'][11] = False
                id_d[event.obj.message['from_id']]['help'][0] = True
                if not id_d[event.obj.message['from_id']]['this_moment']:
                    id_d[event.obj.message['from_id']]['this_moment'] = True

                weather_cl = Weather(city, id_d[event.obj.message['from_id']]['this_moment'],
                                     latt, long,
                                     id_d[event.obj.message['from_id']]['w_weather'])

                text = weather_cl.response_d('')

                vk.messages.send(user_id=event.obj.message['from_id'],
                                     message=text,
                                     attachment=random.choice(attachment_ph_d['weather']),
                                     random_id=random.randint(0, 2 ** 64))

                main(True, vk, event)
            if (event.obj.message['text'] == '2') or \
                    (id_d[event.obj.message['from_id']]['certain_time'] and
                     event.obj.message['text'] in ['1', '2', '3', '4']):
                id_d[event.obj.message['from_id']]['help'][11] = False
                id_d[event.obj.message['from_id']]['help'][12] = True
                if not id_d[event.obj.message['from_id']]['certain_time']:
                    id_d[event.obj.message['from_id']]['this_moment'] = False
                    id_d[event.obj.message['from_id']]['certain_time'] = True

                    weather_cl = Weather(city, id_d[event.obj.message['from_id']]['this_moment'],
                                         latt, long,
                                         id_d[event.obj.message['from_id']]['w_weather'])

                    text = weather_cl.response_d('')

                    vk.messages.send(user_id=event.obj.message['from_id'],
                                     message=text,
                                     attachment=random.choice(attachment_ph_d['weather']),
                                     random_id=random.randint(0, 2 ** 64))
                else:
                    id_d[event.obj.message['from_id']]['help'][12] = False
                    id_d[event.obj.message['from_id']]['help'][0] = True
                    weather_cl = Weather(city, id_d[event.obj.message['from_id']]['this_moment'],
                                         latt, long,
                                         id_d[event.obj.message['from_id']]['w_weather'])

                    text_1, text_2 = weather_cl.response_d(event.obj.message['text'])
                    # print(weather_cl.response_d(event.obj.message['text']))

                    vk.messages.send(user_id=event.obj.message['from_id'],
                                     message=text_1,
                                     random_id=random.randint(0, 2 ** 64))
                    vk.messages.send(user_id=event.obj.message['from_id'],
                                     message=text_2,
                                     random_id=random.randint(0, 2 ** 64))
                    main(True, vk, event)
        else:
            if event.type == VkBotEventType.MESSAGE_NEW:
                if id_d[event.obj.message['from_id']]:
                    print('ok')
                    if id_d[event.obj.message['from_id']]['help'][0] \
                            and event.type == VkBotEventType.MESSAGE_NEW:
                        text = "Выберите один из навыков:\n" \
                               "Игры\n" \
                               "Погода\n" \
                               "Помочь принять решение",
                        vk.messages.send(user_id=event.obj.message['from_id'],
                                         message=text,
                                         # attachment=random.choice(
                                         #     attachment_ph_d['game']),
                                         keyboard=open('keyboard_play.json', 'r',
                                                       encoding='UTF-8').read(),
                                         random_id=random.randint(0, 2 ** 64))
                    elif id_d[event.obj.message['from_id']]['help'][1] \
                            and event.type == VkBotEventType.MESSAGE_NEW:
                        text = "Выберите игру:\n" \
                               "Камень-ножницы-бумага\n" \
                               "Угадай число\n" \
                               "Слова\n" \
                               "Чтобы выбрать, напиши цифру в скобках"
                        vk.messages.send(user_id=event.obj.message['from_id'],
                                         message=text,
                                         keyboard=open('keyboard_play.json', 'r',
                                                       encoding='UTF-8').read(),
                                         random_id=random.randint(0, 2 ** 64))
                    elif id_d[event.obj.message['from_id']]['help'][2] \
                            and event.type == VkBotEventType.MESSAGE_NEW:
                        text = "Вам нужна помощь с принятием решения?\n" \
                               "Напишите ДА / НЕТ\n" \
                               "Напишите СТОП - если хотите завершить навык\n"
                        vk.messages.send(user_id=event.obj.message['from_id'],
                                         message=text,
                                         keyboard=open('keyboard_y_n.json', 'r',
                                                       encoding='UTF-8').read(),
                                         random_id=random.randint(0, 2 ** 64))
                    elif id_d[event.obj.message['from_id']]['help'][3] \
                            and event.type == VkBotEventType.MESSAGE_NEW:
                        text = "Выберите, кто загадывает число: Я или ВЫ?\n" \
                               "Напишите СТОП - если хотите завершить игру\n"

                        vk.messages.send(user_id=event.obj.message['from_id'],
                                         message=text,
                                         random_id=random.randint(0, 2 ** 64))
                    elif id_d[event.obj.message['from_id']]['help'][4] \
                            and event.type == VkBotEventType.MESSAGE_NEW:
                        text = "Вы загадали число? ДА / НЕТ"

                        vk.messages.send(user_id=event.obj.message['from_id'],
                                         message=text,
                                         keyboard=open('keyboard_y_n.json', 'r',
                                                       encoding='UTF-8').read(),
                                         random_id=random.randint(0, 2 ** 64))
                    elif id_d[event.obj.message['from_id']]['help'][5] \
                            and event.type == VkBotEventType.MESSAGE_NEW:
                        text = "Введите БОЛЬШЕ, МЕНЬШЕ или РАВНО"

                        vk.messages.send(user_id=event.obj.message['from_id'],
                                         message=text,
                                         random_id=random.randint(0, 2 ** 64))
                    elif id_d[event.obj.message['from_id']]['help'][6] \
                            and event.type == VkBotEventType.MESSAGE_NEW:
                        text = "Напишите мне -  ПЕРЕЗАПУСТИТЬ игру / НЕ ПЕРЕЗАПУСКАТЬ"

                        vk.messages.send(user_id=event.obj.message['from_id'],
                                         message=text,
                                         keyboard=open('keyboard_strat_notstart.json',
                                             'r',
                                             encoding='UTF-8').read(),
                                         random_id=random.randint(0, 2 ** 64))
                    elif id_d[event.obj.message['from_id']]['help'][7] \
                            and event.type == VkBotEventType.MESSAGE_NEW:
                        text = "Введите максимальное число, которое мне можно загадать\n" \
                               "Минимальное число - 0"

                        vk.messages.send(user_id=event.obj.message['from_id'],
                                         message=text,
                                         random_id=random.randint(0, 2 ** 64))
                    elif id_d[event.obj.message['from_id']]['help'][8] \
                            and event.type == VkBotEventType.MESSAGE_NEW:
                        text = "Введите число, которое думаете, я загадал\n"

                        vk.messages.send(user_id=event.obj.message['from_id'],
                                         message=text,
                                         random_id=random.randint(0, 2 ** 64))
                    elif id_d[event.obj.message['from_id']]['help'][9] \
                            and event.type == VkBotEventType.MESSAGE_NEW:
                        text = "Введите ДА или НЕТ\n"

                        vk.messages.send(user_id=event.obj.message['from_id'],
                                         message=text,
                                         keyboard=open('keyboard_y_n.json', 'r',
                                                       encoding='UTF-8').read(),
                                         random_id=random.randint(0, 2 ** 64))
                    elif id_d[event.obj.message['from_id']]['help'][10] \
                            and event.type == VkBotEventType.MESSAGE_NEW:
                        text = "Выберите тип данных: \n" \
                               "Данные о погоде(1)\n" \
                               "Данные о времени(2)\n"

                        vk.messages.send(user_id=event.obj.message['from_id'],
                                         message=text,
                                         keyboard=open(
                                             'keyboard_time_wehar.json', 'r',
                                             encoding='UTF-8').read(),
                                         random_id=random.randint(0, 2 ** 64))
                    elif id_d[event.obj.message['from_id']]['help'][11] \
                            and event.type == VkBotEventType.MESSAGE_NEW:
                        text = "Выберите время желаемого прогноза погоды:\n" \
                               "Данный момент (1)\n" \
                               "Определенное время (2)\n"

                        vk.messages.send(user_id=event.obj.message['from_id'],
                                         message=text,
                                         keyboard=open('keyboard_now_notnow.json', 'r',
                                             encoding='UTF-8').read(),
                                         random_id=random.randint(0, 2 ** 64))
                    elif id_d[event.obj.message['from_id']]['help'][12] \
                            and event.type == VkBotEventType.MESSAGE_NEW:
                        text = "Выберите время желаемого прогноза погоды:\n" \
                               "Утро(1)\n" \
                               "День(2)\n" \
                               "Вечер(3)\n" \
                               "Ночь(4)\n"

                        vk.messages.send(user_id=event.obj.message['from_id'],
                                         message=text,
                                         random_id=random.randint(0, 2 ** 64))
                    elif event.type == VkBotEventType.MESSAGE_NEW and \
                            id_d[event.obj.message['from_id']]['help'][13]:
                        vk.messages.send(user_id=event.obj.message['from_id'],
                                         message="Для начала работы напишите 'Начать'",
                                         random_id=random.randint(0, 2 ** 64))



class NumberGamePolz:
    def __init__(self, nb_gm_fl, nb_gm_plz, h_6):
        self.maxim = 1000
        self.minim = 0

        self.number_game_fl = nb_gm_fl
        self.number_game_plz = nb_gm_plz
        self.help6 = h_6

        self.middle = (self.minim + self.maxim) // 2
        self.numbers = [i for i in range(1000)]

    def numb_game_plz_func(self, answ):
        if answ == "меньше" or answ == "больше":
            if answ == "меньше":
                self.minim = self.middle

            else:
                self.maxim = self.middle

            self.middle = (self.minim + self.maxim) // 2

            if self.minim < self.maxim - 1:
                self.help6 = True
                return self.help6, False, \
                       f"Число {self.numbers[self.middle]} БОЛЬШЕ, МЕНЬШЕ " \
                       f"или РАВНО вашему числу?"
            else:
                self.help6 = False
                return self.help6, True, \
                       "Должно быть, Вы ошиблись. Такого числа нет в " \
                       "диапазоне от 1 до 1000\n" \
                       "Напишите мне -  ПЕРЕЗАПУСТИТЬ игру / НЕ ПЕРЕЗАПУСКАТЬ"

        elif answ == "равно":
            self.help6 = False
            return self.help6, True, \
                   f"Ура! У меня получилось !\n " \
                   f"Ваше число : {self.numbers[self.middle]}\n" \
                   "Напишите мне -  ПЕРЕЗАПУСТИТЬ игру / НЕ ПЕРЕЗАПУСКАТЬ"
        self.help6 = False
        return self.help6, True, \
               "Должно быть, Вы ошиблись. Такого числа нет в " \
               "диапазоне от 1 до 1000\n" \
               "Напишите мне -  ПЕРЕЗАПУСТИТЬ игру / НЕ ПЕРЕЗАПУСКАТЬ"

    def number_game_st(self):
        return f"Число {self.numbers[self.middle]} БОЛЬШЕ, МЕНЬШЕ " \
               f"или РАВНО вашему числу?"


class NumberGameII:
    def __init__(self, nb_gm_fl, find_h, nb_gm_ii, h_9):
        self.numb_ii = 0

        self.find_h = find_h
        self.high = 0
        self.number_game_fl = nb_gm_fl
        self.number_game_ii = nb_gm_ii
        self.help9 = h_9
        self.help7 = False

    def highest(self, answ):
        # print(f"do {answ}")
        self.high = int(answ)
        self.numb_ii = random.randint(0, int(int(answ)))
        # print(self.numb_ii)
        text = "Всё, я загадал число\n" \
               "Можете угадывать"
        self.find_h = True
        self.help9 = True
        return self.number_game_fl, self.number_game_ii, self.find_h, self.help9, text

    def numb_game_ii_func(self, answ):
        # print(int(answ))
        if int(answ) <= self.high and int(answ) >= 0:
            if int(answ) > self.numb_ii:
                text = "Не угадали. Мое число меньше."
                self.help9 = True
                self.help7 = False
            elif int(answ) < self.numb_ii:
                text = "Не угадали. Мое число больше."
                self.help9 = True
                self.help7 = False
            else:
                text = f"Ура ! Вы угадали, мое число {self.numb_ii}.\n" \
                       "Напишите мне -  ПЕРЕЗАПУСТИТЬ игру / НЕ ПЕРЕЗАПУСКАТЬ"
                self.help9 = False
                self.help7 = True

        else:
            text = "Точно нет...Вы сами себе противоречите...\n" \
                   f"Загадано число от 0 до {self.high}"
            self.help9 = False
            self.help7 = True
        return text, self.help9, self.help7


def restart_game(vk, game_name, event):
    vk.messages.send(user_id=event.obj.message['from_id'],
                     message="Еще раз?",
                     keyboard=open('keyboard_y_n.json', 'r', encoding='UTF-8').read(),
                     random_id=random.randint(0, 2 ** 64))
    for event in longpoll.listen():
        if event.type == VkBotEventType.MESSAGE_NEW and \
                event.obj.message['text'].lower() == 'да':
            game_name(vk, event)
        elif event.type == VkBotEventType.MESSAGE_NEW and \
                event.obj.message['text'].lower() != 'да':
            main(True, vk, event)


def letters_slova(word, proverka=False):
    if proverka:
        return word[0]
    else:
        if word[-2:] == 'ая' or word[-2:] == 'ый' or word[-2:] == 'ые' or not word.isalpha():
            return '0'
        elif word[-1] == 'й' or word[-1] == 'ы' or word[-1] == 'ъ' or word[-1] == 'ь':
            return word[-2]
        return word[-1]


def rock_paper_scissors(vk, event):
    sp = ['ножницы', 'камень', 'бумага']
    vk.messages.send(user_id=event.obj.message['from_id'],
                     message="Отсчёт пошел",
                     keyboard=open('keyboard_k_n_b.json', 'r', encoding='UTF-8').read(),
                     random_id=random.randint(0, 2 ** 64))
    for i in range(1, 6):
        vk.messages.send(user_id=event.obj.message['from_id'],
                         message=f"{i}",
                         random_id=random.randint(0, 2 ** 64))
        time.sleep(1)
    slov = sp[random.randint(0, 2)]
    vk.messages.send(user_id=event.obj.message['from_id'],
                     message=slov,
                     random_id=random.randint(0, 2 ** 64))
    for event in longpoll.listen():
        if event.type == VkBotEventType.MESSAGE_NEW:
            if event.obj.message['text'].lower() == slov:
                vk.messages.send(user_id=event.obj.message['from_id'],
                                 message="Ничья\n",
                                 attachment=random.choice(attachment_ph_d['draw']),
                                 random_id=random.randint(0, 2 ** 64))
                restart_game(vk, rock_paper_scissors, event)
            elif (event.obj.message['text'].lower() == 'ножницы' and slov == 'бумага') or (
                    event.obj.message['text'].lower() == 'камень' and slov == 'ножницы') or (
                    event.obj.message['text'].lower() == 'бумага' and slov == 'камень'):
                vk.messages.send(user_id=event.obj.message['from_id'],
                                 message="Вы выиграли\n",
                                 attachment=random.choice(attachment_ph_d['win']),
                                 random_id=random.randint(0, 2 ** 64))
                restart_game(vk, rock_paper_scissors, event)
            elif (event.obj.message['text'].lower() == 'бумага' and slov == 'ножницы') or (
                    event.obj.message['text'].lower() == 'ножницы' and slov == 'камень') or (
                    event.obj.message['text'].lower() == 'камень' and slov == 'бумага'):
                vk.messages.send(user_id=event.obj.message['from_id'],
                                 message="Вы проиграли\n",
                                 attachment=attachment_ph_d['fail'],
                                 random_id=random.randint(0, 2 ** 64))
                restart_game(vk, rock_paper_scissors, event)
            vk.messages.send(user_id=event.obj.message['from_id'],
                             message="Такого знака нет",
                             random_id=random.randint(0, 2 ** 64))
            restart_game(vk, rock_paper_scissors, event)


def slova(vk, event):
    slova_flag = False
    slova_flag1 = True
    sp_slov_user = []
    slovarik_slov_copy = slovarik_slov.copy()
    vk.messages.send(user_id=event.obj.message['from_id'],
                     message='Вы начинайте',
                     random_id=random.randint(0, 2 ** 64))
    for event in longpoll.listen():
        if event.type == VkBotEventType.MESSAGE_NEW:
            if event.obj.message['text'].lower() == 'сдаюсь':
                vk.messages.send(user_id=event.obj.message['from_id'],
                                 message="Ура, Ура, Ура, я выиграл",
                                 random_id=random.randint(0, 2 ** 64))
                main(True, vk, event)
            else:
                if slova_flag:
                    if letters_slova(i) != letters_slova(event.obj.message['text'].lower(), True) \
                            or str(pymorphy2.MorphAnalyzer().parse(
                        event.obj.message['text'].lower())[0].methods_stack[0][0]) != '<DictionaryAnalyzer>'\
                            or pymorphy2.MorphAnalyzer().parse(event.obj.message['text'].lower())[0].tag.POS != 'NOUN':
                        vk.messages.send(user_id=event.obj.message['from_id'],
                                         message="Слово не подходит",
                                         random_id=random.randint(0, 2 ** 64))
                        slova_flag1 = False
                    else:
                        slova_flag1 = True
                if slova_flag1:
                    letter = letters_slova(event.obj.message['text'].lower())
                    if letter == '0' or event.obj.message['text'].lower() in \
                            sp_slov_user or str(pymorphy2.MorphAnalyzer().parse(
                        event.obj.message['text'].lower())[0].methods_stack[0][0]) != '<DictionaryAnalyzer>'\
                            or pymorphy2.MorphAnalyzer().parse(event.obj.message['text'].lower())[0].tag.POS != 'NOUN':
                        vk.messages.send(user_id=event.obj.message['from_id'],
                                         message="Слово не подходит",
                                         random_id=random.randint(0, 2 ** 64))
                    else:
                        sp_slov_user.append(event.obj.message['text'].lower())
                        if len(slovarik_slov_copy[letter]) == 0:
                            vk.messages.send(user_id=event.obj.message['from_id'],
                                             message="Я сдаюсь, вы выиграли",
                                             random_id=random.randint(0, 2 ** 64))
                            main(True, vk, event)
                        index = random.randint(0, len(slovarik_slov_copy[letter]) - 1)
                        sl = slovarik_slov_copy[letter][index]
                        i = slovarik_slov_copy[letter].pop(index)
                        vk.messages.send(user_id=event.obj.message['from_id'],
                                         message=f"{sl}\n"
                                                 f"Вам на букву {letters_slova(sl)}",
                                         random_id=random.randint(0, 2 ** 64))
                        slova_flag = True


class Weather:
    def __init__(self, city, now, lat, lon, w_w_fl):
        self.time = now
        self.city_fl = city
        self.lat = lat
        self.lon = lon
        self.w = w_w_fl

        self.fact_d = addition.fact_d
        self.condition_d = addition.condition_d
        self.wind_d = addition.wind_d
        self.clock_d = addition.clock_d
        self.daytime_d = addition.daytime_d
        self.sun_d = addition.sun_d
        self.time_d = addition.time_d
        self.season_d = addition.season_d
        self.moon_d = addition.moon_d

        self.weather_request = 'https://api.weather.yandex.ru/v1/forecast/'

        headers = {'X-Yandex-API-Key': '6b963e22-5fa2-47e6-8a49-d67a12dd9793'}
        w_params = {'lat': self.lat,
                    'lon': self.lon,
                    'lang': "ru_RU"}

        self.response = requests.get(self.weather_request, headers=headers, params=w_params)

    def response_d(self, time):
        if self.response:
            json_response = self.response.json()
            if self.w:
                if self.time:
                    fact_w = json_response['fact']

                    text = f"Температура воздуха: {self.fact_d['temp'][0]} {fact_w['temp']}{self.fact_d['temp'][1]}\n" \
                        f"Скорость ветра:  {self.fact_d['wind_speed']} {fact_w['wind_speed']}м/с\n"\
                        f"Направление ветра:  {self.wind_d[fact_w['wind_dir']][1]} {self.wind_d[fact_w['wind_dir']][0]}\n"\
                        f"Атмосферное давление:  {self.fact_d['pressure_mm']} {fact_w['pressure_mm']}мм рт.ст.\n"\
                        f"Влажность воздуха:  {self.fact_d['humidity']} {fact_w['humidity']}%\n"\
                        f"Описание погоды:  {self.condition_d[fact_w['condition']][0]} {self.condition_d[fact_w['condition']][1]}\n"
                    return text
                else:
                    if time == '':
                        text = "Вы можете получить прогноз погоды на:\n"\
                               "Утро(1)\n"\
                               "День(2)\n"\
                               "Вечер(3)\n"\
                               "Ночь(4)\n"
                        return text
                    else:
                        if time == '1':
                            fact_w = json_response['forecasts'][0]['parts']['morning']
                            text_1 = f"Прогноз на утро:"
                        elif time == '2':
                            fact_w = json_response['forecasts'][0]['parts']['day']
                            text_1 = f"Прогноз на день:"
                        elif time == '3':
                            fact_w = json_response['forecasts'][0]['parts']['evening']
                            text_1 = f"Прогноз на вечер:"
                        elif time == '4':
                            fact_w = json_response['forecasts'][0]['parts']['night']
                            text_1 = f"Прогноз на ночь:"
                        text_2 = f"Температура воздуха: {self.fact_d['temp'][0]} {fact_w['temp_avg']}{self.fact_d['temp'][1]}\n" \
                            f"Скорость ветра:  {self.fact_d['wind_speed']} {fact_w['wind_speed']}м/с\n" \
                            f"Направление ветра:  {self.wind_d[fact_w['wind_dir']][1]} {self.wind_d[fact_w['wind_dir']][0]}\n" \
                             f"Атмосферное давление:  {self.fact_d['pressure_mm']} {fact_w['pressure_mm']}мм рт.ст.\n" \
                            f"Влажность воздуха:  {self.fact_d['humidity']} {fact_w['humidity']}%\n" \
                            f"Описание погоды:  {self.condition_d[fact_w['condition']][0]} {self.condition_d[fact_w['condition']][1]}\n"
                        return text_1, text_2
            else:
                fact_w = json_response
                text = f"Точное время:  {self.clock_d[datetime.datetime.now().hour]}{datetime.datetime.now()}\n"\
                       f"Часовой пояс:  {self.time_d['tzinfo']} {json_response['info']['tzinfo']['name']}\n"\
                       f"Явление полярной ночи в городе:\n"\
                       f"Временя года: \n"
                # print(json_response['now_dt'])
                if json_response['fact']['polar']:
                    polar_txt = 'да'
                else:
                    polar_txt = 'нет'
                text = [f"Дата: {self.time_d['date']} {datetime.datetime.now().date()}\n",
                        # f"Точное время:  {self.clock_d[datetime.datetime.now().hour]}{datetime.datetime.now().time()}\n",
                        f"Часовой пояс:  {self.time_d['tzinfo']} {json_response['info']['tzinfo']['name']}\n",
                        f"Время рассвета: {self.sun_d['sunrise']} {json_response['forecasts'][0]['sunrise']}\n",
                        f"Время заката: {self.sun_d['sunset']} {json_response['forecasts'][0]['sunset']}\n",
                        f"Время года: {self.sрогноeason_d[json_response['fact']['season']][0]} {self.season_d[json_response['fact']['season']][1]}\n",
                        f"Явление полярной ночи в городе: {self.time_d['polar']} {polar_txt}\n",
                        f"Фаза Луны: {self.moon_d[json_response['forecasts'][0]['moon_text']][0]} {self.moon_d[json_response['forecasts'][0]['moon_text']][1]}"]
                return ('').join(text)

        else:
            print("Ошибка выполнения запроса:")
            print(self.weather_request)
            print("Http статус:", self.response.status_code, "(", self.response.reason, ")")
            sys.exit(1)


class Cities:
    def __init__(self, city):
        print(city)
        self.city = city

        out = self.search(self.city)
        print("Cities.search ", out)

    def search(self, toponym):
        if toponym:

            geocoder_api_server = "http://geocode-maps.yandex.ru/1.x/"

            geocoder_params = {
                "apikey": "40d1649f-0493-4b70-98ba-98533de7710b",
                "geocode": toponym,
                "format": "json"}

            response = requests.get(geocoder_api_server, params=geocoder_params)

            json_response = response.json()
            print(json_response['response']["GeoObjectCollection"]["metaDataProperty"]["GeocoderResponseMetaData"]['found'] == '0')
            if json_response['response']["GeoObjectCollection"]["metaDataProperty"]["GeocoderResponseMetaData"]['found'] != '0':
                kind_area = json_response["response"]["GeoObjectCollection"][
                    "featureMember"][0]["GeoObject"]["metaDataProperty"][
                    "GeocoderMetaData"]['Address']['Components'][-1]["kind"]

                if kind_area == 'province' or kind_area == 'locality':

                    toponym = json_response["response"]["GeoObjectCollection"][
                        "featureMember"][0]["GeoObject"]

                    city = json_response["response"]["GeoObjectCollection"]["featureMember"][0]["GeoObject"]["metaDataProperty"][
                          "GeocoderMetaData"]['Address']['Components'][-1][
                          'name']

                    toponym_coodrinates = toponym["Point"]["pos"]
                    toponym_longitude, toponym_lattitude = toponym_coodrinates.split(" ")

                    return toponym_longitude, toponym_lattitude, city
                else:
                    text = "Извините, я не знаю такого города. Может, Вы допустили ошибку?\n" \
                           "Попробуйте ввести название города еще раз"
                return text
            else:
                text = "Извините, я не знаю такого города. Может, Вы допустили ошибку?\n"\
                       "Попробуйте ввести название города еще раз"
                return text

        else:
            text = "Извините, я не знаю такого города. Может, Вы допустили ошибку?\n"\
                   "Попробуйте ввести название города еще раз"
            return text

if __name__ == '__main__':
    main()
