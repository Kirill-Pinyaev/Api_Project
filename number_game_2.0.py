import vk_api
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
import random
import time


def main():
    global maxim, middle, minim, numbers, number_game, numb_game_find, numb_game_pr, user_find_h
    flag = False

    vk_session = vk_api.VkApi(
        token='dc59d33f532316392242ba355086b5c35e22623e0fdae6f433d6f17b655b10ce8e95db5790ab60344beb1')

    longpoll = VkBotLongPoll(vk_session, '193318026')

    for event in longpoll.listen():
        vk = vk_session.get_api()

        if event.type == VkBotEventType.MESSAGE_NEW and event.obj.message[
            'text'].lower() == 'начать':
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
                                     "Что бы выбрать напиши цифру в скобках",
                             random_id=random.randint(0, 2 ** 64))

        if event.type == VkBotEventType.MESSAGE_NEW and event.obj.message[
            'text'] == '1' and flag:
            vk.messages.send(user_id=event.obj.message['from_id'],
                             message="Сейчас пойдет отсчет до 5 и на цыфре пять нужно отправить"
                                     "или камень или ножницы или бумагу\n"
                                     "Памятка:\n"
                                     "Бумага бьёт камень, но боится ножниц\n"
                                     "Камень бьёт ножницы, но боится бумагу\n"
                                     "Ножницы бьют бумагу, но боятся камня",
                             random_id=random.randint(0, 2 ** 64))

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
