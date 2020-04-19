import vk_api
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
import random
import time

vk_session = vk_api.VkApi(
    token='dc59d33f532316392242ba355086b5c35e22623e0fdae6f433d6f17b655b10ce8e95db5790ab60344beb1')
longpoll = VkBotLongPoll(vk_session, '193318026')
flag = False
flag_play = False


def main(not_first=False, vk=None, event=None):
    global flag, flag_play
    # if not_first:
    #    vk.messages.send(user_id=event.obj.message['from_id'],
    #                     message="Привет я бот(название бота)\n"
    #                             "и вот что я могу:\n"
    #                             "Игры",
    #                     random_id=random.randint(0, 2 ** 64))
    for event in longpoll.listen():
        vk = vk_session.get_api()
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

        if event.type == VkBotEventType.MESSAGE_NEW and 'игр' in \
                event.obj.message[
                    'text'].lower() and flag:
            vk.messages.send(user_id=event.obj.message['from_id'],
                             message="Можем поиграть в:\n"
                                     "Камень ножницы бумага(1)\n"
                                     "Угадай число(2)\n"
                                     "Чтобы выбрать напиши цифру в скобках",
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
                                     "Для продолжения напишите да",
                             random_id=random.randint(0, 2 ** 64))
            for event in longpoll.listen():
                if event.type == VkBotEventType.MESSAGE_NEW and \
                        event.obj.message['text'].lower() == 'да':
                    rock_paper_scissors(vk, event)


        if event.type == VkBotEventType.MESSAGE_NEW and event.obj.message[
            'text'] == '2' and flag:

            number_game = True
            numb_gm_polz = False
            numb_gm_ii = False
            numb_gm = NumberGame()

            vk.messages.send(user_id=event.obj.message['from_id'],
                             message="Название: Угадай число\n"
                                     "Один из нас - Я или ВЫ - загадывает число от 1 до 999.\n"
                                     "Другой начинает начинает угадывать, называя числа, "
                                     "получая в ответ фразы 'больше' или 'меньше'.\n"
                                     "'Меньше' - загаданное число меньше Вашего.\n"
                                     "'Больше' - загаданное число больше Вашего.\n"
                                     "Кто загадывает число: Я или ВЫ?",
                             random_id=random.randint(0, 2 ** 64))

        if event.type == VkBotEventType.MESSAGE_NEW and event.obj.message[
            'text'].lower() == 'я' and flag and number_game:

            numb_gm_polz = True

            text = "Хорошо. Загадывайте число.\n" \
                   "Загадали? ДА / НЕТ"

            vk.messages.send(user_id=event.obj.message['from_id'],
                             message=text,
                             random_id=random.randint(0, 2 ** 64))

        if event.type == VkBotEventType.MESSAGE_NEW and event.obj.message[
            'text'].lower() in ['нет', 'да'] and flag and number_game and numb_gm_polz:
            if event.obj.message['text'].lower() == 'нет':
                text = "Ладно, я могу подождпть.\n" \
                       "А теперь загадали? ДА / НЕТ"

                vk.messages.send(user_id=event.obj.message['from_id'],
                                 message=text,
                                 random_id=random.randint(0, 2 ** 64))

            else:
                text = "Хорошо. Начинаю угадывать\n"

                vk.messages.send(user_id=event.obj.message['from_id'],
                                     message=text,
                                     random_id=random.randint(0, 2 ** 64))

                vk.messages.send(user_id=event.obj.message['from_id'],
                                 message=numb_gm.number_game_st(),
                                 random_id=random.randint(0, 2 ** 64))

        if event.type == VkBotEventType.MESSAGE_NEW and event.obj.message[
            'text'].lower() in ['больше', 'меньше', 'равно'] and flag \
                and number_game and numb_gm_polz:
            if numb_gm.minim < numb_gm.maxim - 1:

                text = numb_gm.number_game_func\
                    (event.obj.message['text'].lower())
                print(numb_gm_polz)
                print(text)
                vk.messages.send(user_id=event.obj.message['from_id'],
                                 message=text,
                                 random_id=random.randint(0, 2 ** 64))
            else:
                text = "Должно быть, Вы ошиблись.\n" \
          "Такого числа нет в диапазоне от 1 до 1000"

                vk.messages.send(user_id=event.obj.message['from_id'],
                                 message=text,
                                 random_id=random.randint(0, 2 ** 64))
        if event.type == VkBotEventType.MESSAGE_NEW and event.obj.message[
            'text'].lower() == 'вы' and flag and number_game:

            numb_gm_ii = True

            text = numb_gm.number_game_func(event.obj.message['text'].lower())

            vk.messages.send(user_id=event.obj.message['from_id'],
                             message=text,
                             random_id=random.randint(0, 2 ** 64))

        if event.type == VkBotEventType.MESSAGE_NEW and event.obj.message[
            'text'].isdigit() and flag and number_game and numb_gm_ii:
            text = numb_gm.number_game_func(event.obj.message['text'].lower())

            vk.messages.send(user_id=event.obj.message['from_id'],
                             message=text,
                             random_id=random.randint(0, 2 ** 64))

        elif event.type == VkBotEventType.MESSAGE_NEW and not flag:
            vk.messages.send(user_id=event.obj.message['from_id'],
                             message="Для начала работы напишите 'Начать'",
                             random_id=random.randint(0, 2 ** 64))


def rock_paper_scissors(vk, event):
    sp = ['ножницы', 'камень', 'бумага']
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
                                 message="Ничья\n"
                                         "Еще раз?",
                                 random_id=random.randint(0, 2 ** 64))
                for event in longpoll.listen():
                    if event.type == VkBotEventType.MESSAGE_NEW and \
                            event.obj.message['text'].lower() == 'да':
                        rock_paper_scissors(vk, event)
                    main(True, vk, event)
            elif (event.obj.message['text'].lower() == 'ножницы' and slov == 'бумага') or (
                    event.obj.message['text'].lower() == 'камень' and slov == 'ножницы') or (
                    event.obj.message['text'].lower() == 'бумага' and slov == 'камень'):
                vk.messages.send(user_id=event.obj.message['from_id'],
                                 message="Вы выиграли\n"
                                         "Еще раз?",
                                 random_id=random.randint(0, 2 ** 64))
                for event in longpoll.listen():
                    if event.type == VkBotEventType.MESSAGE_NEW and \
                            event.obj.message['text'].lower() == 'да':
                        rock_paper_scissors(vk, event)
                    main(True, vk, event)
            elif (event.obj.message['text'].lower() == 'бумага' and slov == 'ножницы') or (
                    event.obj.message['text'].lower() == 'ножницы' and slov == 'камень') or (
                    event.obj.message['text'].lower() == 'камень' and slov == 'бумага'):
                vk.messages.send(user_id=event.obj.message['from_id'],
                                 message="Вы проиграли\n"
                                         "Еще раз?",
                                 random_id=random.randint(0, 2 ** 64))
                for event in longpoll.listen():
                    if event.type == VkBotEventType.MESSAGE_NEW and \
                            event.obj.message['text'].liwer() == 'да':
                        rock_paper_scissors(vk, event)
                    main(True, vk, event)
            vk.messages.send(user_id=event.obj.message['from_id'],
                             message="Такого знака нет",
                             random_id=random.randint(0, 2 ** 64))
            rock_paper_scissors(vk, event)


class NumberGame:
    def __init__(self):
        self.maxim = 1000
        self.minim = 0
        self.middle = (self.minim + self.maxim) // 2
        self.numbers = [i for i in range(1000)]

    def number_game_func(self, answ):
        if answ == "меньше" or answ == "больше":
            if answ == "меньше":
                self.minim = self.middle

            else:
                self.maxim = self.middle

            self.middle = (self.minim + self.maxim) // 2

            if self.minim < self.maxim - 1:
                return f"Число {self.numbers[self.middle]} БОЛЬШЕ, МЕНЬШЕ " \
                    f"или РАВНО вашему числу?"
            else:
                return "Должно быть, Вы ошиблись. Такого числа нет в " \
               "диапазоне от 1 до 1000"

        elif answ == "равно":
            return f"Ура! У меня получилось !\n " \
                    f"Ваше число : {self.numbers[self.middle]}"
        return "Должно быть, Вы ошиблись. Такого числа нет в " \
               "диапазоне от 1 до 1000"

    def number_game_st(self):
        return f"Число {self.numbers[self.middle]} БОЛЬШЕ, МЕНЬШЕ " \
            f"или РАВНО вашему числу?"


if __name__ == '__main__':
    main()
