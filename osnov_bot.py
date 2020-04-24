import vk_api
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
import random
import time

vk_session = vk_api.VkApi(
    token='dc59d33f532316392242ba355086b5c35e22623e0fdae6f433d6f17b655b10ce8e95db5790ab60344beb1')
longpoll = VkBotLongPoll(vk_session, '193318026')
flag = False
flag_play = False
id_user = None


def main(not_first=False, vk=None,):
    global flag, flag_play, id_user
    if not_first:
        vk.messages.send(user_id=id_user,
                         message="Привет я бот(название бота)\n"
                                 "и вот что я могу:\n"
                                 "Игры",
                         random_id=random.randint(0, 2 ** 64))
    for event in longpoll.listen():
        vk = vk_session.get_api()
        if event.type == VkBotEventType.MESSAGE_NEW and event.obj.message[
            'text'].lower() == 'начать' and not flag:
            id_user = event.obj.message['from_id']
            flag = True
            print(event)
            print('Новое сообщение:')
            print('Для меня от:', id_user)
            print('Текст:', event.obj.message['text'])
            vk.messages.send(user_id=id_user,
                             message="Привет я бот(название бота)\n"
                                     "и вот что я могу:\n"
                                     "Игры",
                             random_id=random.randint(0, 2 ** 64))
        if event.type == VkBotEventType.MESSAGE_NEW and 'игр' in event.obj.message[
            'text'].lower() and flag:
            vk.messages.send(user_id=id_user,
                             message="Можем поиграть в:\n"
                                     "Камень ножницы бумага(1)\n"
                                     "Что бы выбрать напиши цифру в скобках",
                             random_id=random.randint(0, 2 ** 64))
            flag_play = True
        if event.type == VkBotEventType.MESSAGE_NEW and event.obj.message[
            'text'] == '1' and flag_play:
            vk.messages.send(user_id=id_user,
                             message="Сейчас пойдет отсчет до 5 и на цифре пять нужно отправить"
                                     "или камень или ножницы или бумага\n"
                                     "Памятка:\n"
                                     "Бумага бьёт камень, но боится ножниц\n"
                                     "Камень бьёт ножницы, но боится бумагу\n"
                                     "Ножницы бьют бумагу, но боятся камня\n"
                                     "Для продолжения напишите да",
                             random_id=random.randint(0, 2 ** 64))
            for event in longpoll.listen():
                if event.type == VkBotEventType.MESSAGE_NEW and \
                        event.obj.message['text'].lower() == 'да':
                    rock_paper_scissors(vk, event)



        elif event.type == VkBotEventType.MESSAGE_NEW and not flag:
            vk.messages.send(user_id=id_user,
                             message="Для начала работы напишите 'Начать'",
                             random_id=random.randint(0, 2 ** 64))


def restart_game(vk, game_name):
    vk.messages.send(user_id=id_user,
                     message="Еще раз?",
                     random_id=random.randint(0, 2 ** 64))
    for event in longpoll.listen():
        if event.type == VkBotEventType.MESSAGE_NEW and \
                event.obj.message['text'].lower() == 'да':
            game_name(vk, event)
        elif  event.type == VkBotEventType.MESSAGE_NEW and \
                event.obj.message['text'].lower() != 'да':
            main(True, vk)


def rock_paper_scissors(vk, event):
    sp = ['ножницы', 'камень', 'бумага']
    for i in range(1, 6):
        vk.messages.send(user_id=id_user,
                         message=f"{i}",
                         random_id=random.randint(0, 2 ** 64))
        time.sleep(1)
    slov = sp[random.randint(0, 2)]
    vk.messages.send(user_id=id_user,
                     message=slov,
                     random_id=random.randint(0, 2 ** 64))
    for event in longpoll.listen():
        if event.type == VkBotEventType.MESSAGE_NEW:
            if event.obj.message['text'].lower() == slov:
                vk.messages.send(user_id=id_user,
                                 message="Ничья\n",
                                 random_id=random.randint(0, 2 ** 64))
                restart_game(vk, rock_paper_scissors)
            elif (event.obj.message['text'].lower() == 'ножницы' and slov == 'бумага') or (
                    event.obj.message['text'].lower() == 'камень' and slov == 'ножницы') or (
                    event.obj.message['text'].lower() == 'бумага' and slov == 'камень'):
                vk.messages.send(user_id=id_user,
                                 message="Вы выиграли\n",
                                 random_id=random.randint(0, 2 ** 64))
                restart_game(vk, rock_paper_scissors)
            elif (event.obj.message['text'].lower() == 'бумага' and slov == 'ножницы') or (
                    event.obj.message['text'].lower() == 'ножницы' and slov == 'камень') or (
                    event.obj.message['text'].lower() == 'камень' and slov == 'бумага'):
                vk.messages.send(user_id=id_user,
                                 message="Вы проиграли\n",
                                 random_id=random.randint(0, 2 ** 64))
                restart_game(vk, rock_paper_scissors)
            vk.messages.send(user_id=id_user,
                             message="Такого знака нет",
                             random_id=random.randint(0, 2 ** 64))
            restart_game(vk, rock_paper_scissors)


if __name__ == '__main__':
    main()
