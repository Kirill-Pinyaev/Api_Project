import vk_api
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
import random
import time

vk_session = vk_api.VkApi(
    token='dc59d33f532316392242ba355086b5c35e22623e0fdae6f433d6f17b655b10ce8e95db5790ab60344beb1')
longpoll = VkBotLongPoll(vk_session, '193318026')
flag = False
flag_play = False


def main():
    global flag, flag_play
    for event in longpoll.listen():
        vk = vk_session.get_api()
        #if flag and flag_play:
          #  vk.messages.send(user_id=event.obj.message['from_id'],
           #                  message="Привет я бот(название бота)\n"
           #                          "и вот что я могу:\n"
           #                          "Игры",
            #                 random_id=random.randint(0, 2 ** 64))
            #flag_play = False

        if event.type == VkBotEventType.MESSAGE_NEW and event.obj.message[
            'text'].lower() == 'начать' and not flag:
            flag = True
            print(event)
            print('Новое сообщение:')
            print('Для меня от:', event.obj.message['from_id'])
            print('Текст:', event.obj.message['text'])
            vk.messages.send(user_id=event.obj.message['from_id'],
                             message="Привет я бот(название бота)\n"
                                     "и вот что я могу:\n"
                                     "Игры",
                             random_id=random.randint(0, 2 ** 64))
        if event.type == VkBotEventType.MESSAGE_NEW and 'игр' in event.obj.message[
            'text'].lower() and flag:
            vk.messages.send(user_id=event.obj.message['from_id'],
                             message="Можем поиграть в:\n"
                                     "Камень ножницы бумага(1)\n"
                                     "Что бы выбрать напиши цифру в скобках",
                             random_id=random.randint(0, 2 ** 64))
            flag_play = True
        if event.type == VkBotEventType.MESSAGE_NEW and event.obj.message[
            'text'] == '1' and flag_play:
            vk.messages.send(user_id=event.obj.message['from_id'],
                             message="Сейчас пойдет отсчет до 5 и на цифре пять нужно отправить"
                                     "или камень или ножницы или бумага\n"
                                     "Памятка:\n"
                                     "Бумага бьёт камень, но боится ножниц\n"
                                     "Камень бьёт ножницы, но боится бумагу\n"
                                     "Ножницы бьют бумагу, но боятся камня\n"
                                     "Для продолжения подождите",
                             random_id=random.randint(0, 2 ** 64))
            time.sleep(10)
            sp = ['ножницы', 'камень', 'бумага']
            if event.type == VkBotEventType.MESSAGE_NEW:
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
                        print(event.obj.message['text'].lower())
                        if event.obj.message['text'].lower() == slov:
                            vk.messages.send(user_id=event.obj.message['from_id'],
                                             message="Ничья",
                                             random_id=random.randint(0, 2 ** 64))
                            # Тут должен быть перезапуск
                            main()
                        elif (event.obj.message['text'].lower() == 'ножницы' and slov == 'бумага') or (
                                event.obj.message['text'].lower() == 'камень' and slov == 'ножницы') or (
                                event.obj.message['text'].lower() == 'бумага' and slov == 'камень'):
                            vk.messages.send(user_id=event.obj.message['from_id'],
                                             message="Вы выиграли\n"
                                                     "Еще раз?",
                                             random_id=random.randint(0, 2 ** 64))
                            if event.type == VkBotEventType.MESSAGE_NEW and event.obj.message[
                                'text'] == 'да':
                                main()
                                # Тут должен быть перезапуск
                            main()
                        elif (event.obj.message['text'].lower() == 'бумага' and slov == 'ножницы') or (
                                event.obj.message['text'].lower() == 'ножницы' and slov == 'камень') or (
                                event.obj.message['text'].lower() == 'камень' and slov == 'бумага'):
                            vk.messages.send(user_id=event.obj.message['from_id'],
                                             message="Вы проиграли\n"
                                                     "Еще раз?",
                                             random_id=random.randint(0, 2 ** 64))
                            if event.type == VkBotEventType.MESSAGE_NEW and event.obj.message[
                                'text'] == 'да':
                                main()
                                # Тут должен быть перезапуск
                            main()
                        vk.messages.send(user_id=event.obj.message['from_id'],
                                         message="Такого знака нет",
                                         random_id=random.randint(0, 2 ** 64))
                        # Тут должен быть перезапуск
                        main()

        elif event.type == VkBotEventType.MESSAGE_NEW and not flag:
            vk.messages.send(user_id=event.obj.message['from_id'],
                             message="Для начала работы напишите 'Начать'",
                             random_id=random.randint(0, 2 ** 64))


"""class Play:
    def __init__( event):
        vk = vk_session.get_api()
        event = event

    def play1(:"""

if __name__ == '__main__':
    main()
