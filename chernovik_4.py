import vk_api
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
import random
import time


def main():
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
            # numb_gm_cl = NumberGamePolz(number_game, numb_gm_polz)

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
            numb_gm_p_cl = NumberGamePolz(number_game, numb_gm_polz)


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
                                 message=numb_gm_p_cl.number_game_st(),
                                 random_id=random.randint(0, 2 ** 64))

        if event.type == VkBotEventType.MESSAGE_NEW and event.obj.message[
            'text'].lower() in ['больше', 'меньше', 'равно'] and flag \
                and number_game and numb_gm_polz:
            if numb_gm_p_cl.minim < numb_gm_p_cl.maxim - 1:

                number_game, numb_gm_polz, text = numb_gm_p_cl.numb_game_plz_func\
                    (event.obj.message['text'].lower())

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
            find_highest = False

            numb_gm_ii_cl = NumberGameII(number_game, numb_gm_ii, find_highest)

            text = "Введите максимальное число, которое мне можно загадать"

            vk.messages.send(user_id=event.obj.message['from_id'],
                             message=text,
                             random_id=random.randint(0, 2 ** 64))

        if event.type == VkBotEventType.MESSAGE_NEW and event.obj.message[
            'text'].isdigit() and flag and number_game and numb_gm_ii:
            if not find_highest:
                number_game, numb_gm_polz, find_highest, text = numb_gm_ii_cl.\
                    highest(event.obj.message['text'].lower())
                print(number_game)
                print(numb_gm_polz)
                print(find_highest)
                print(text)

                vk.messages.send(user_id=event.obj.message['from_id'],
                                 message=text,
                                 random_id=random.randint(0, 2 ** 64))
            else:

                number_game, numb_gm_polz, find_highest, text = numb_gm_ii_cl.\
                    numb_game_ii_func(event.obj.message['text'].lower())
                print(number_game)
                print(numb_gm_polz)
                print(find_highest)
                print(text)

                vk.messages.send(user_id=event.obj.message['from_id'],
                                 message=text,
                                 random_id=random.randint(0, 2 ** 64))

        elif event.type == VkBotEventType.MESSAGE_NEW and not flag:
            vk.messages.send(user_id=event.obj.message['from_id'],
                             message="Для начала работы напишите 'Начать'",
                             random_id=random.randint(0, 2 ** 64))


class NumberGamePolz:
    def __init__(self, nb_gm_fl, nb_gm_plz):
        self.maxim = 1000
        self.minim = 0

        self.number_game_fl = nb_gm_fl
        self.number_game_plz = nb_gm_plz

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
                return self.number_game_fl, self.number_game_plz, \
                       f"Число {self.numbers[self.middle]} БОЛЬШЕ, МЕНЬШЕ " \
                    f"или РАВНО вашему числу?"
            else:
                self.number_game_fl, self.number_game_plz = False, False
                return self.number_game_fl, self.number_game_plz, \
                       "Должно быть, Вы ошиблись. Такого числа нет в " \
               "диапазоне от 1 до 1000"

        elif answ == "равно":
            self.number_game_fl, self.number_game_plz = False, False
            return self.number_game_fl, self.number_game_plz, \
                   f"Ура! У меня получилось !\n "\
                       f"Ваше число : {self.numbers[self.middle]}"
        self.number_game_fl, self.number_game_plz = False, False
        return self.number_game_fl, self.number_game_plz, \
               "Должно быть, Вы ошиблись. Такого числа нет в " \
               "диапазоне от 1 до 1000"

    def number_game_st(self):
        return f"Число {self.numbers[self.middle]} БОЛЬШЕ, МЕНЬШЕ " \
            f"или РАВНО вашему числу?"


class NumberGameII:
    def __init__(self, nb_gm_fl, find_h, nb_gm_ii):
        self.numb_ii = 0

        self.find_h = find_h
        self.high = 0
        self.number_game_fl = nb_gm_fl
        self.number_game_ii = nb_gm_ii

    def highest(self, answ):
        print(f"do {answ}")
        self.high = int(answ)
        self.numb_ii = random.randint(0, int(int(answ)))
        text = "Всё, я загадал число\n" \
               "Можете угадывать"
        self.find_h = True
        return self.number_game_fl, self.number_game_ii, self.find_h, text

    def numb_game_ii_func(self, answ):
        print(int(answ))
        if int(answ) < self.high and int(answ) > 0:
            if int(answ) > self.numb_ii:
                text = "Не угадали. Мое число меньше."
            elif int(answ) < self.numb_ii:
                text = "Не угадали. Мое число больше."
            else:
                self.number_game_fl, self.number_game_ii, self.find_h = False, False, False
                text = f"Ура ! Вы угадали, мое число {self.numb_ii}."
            print(self.numb_ii)
        else:
            text = "Точно нет...Вы сами себе противоречите...\n"\
                   f"Загадано число от 1 до {self.high}"
        return self.number_game_fl, self.number_game_ii, self.find_h, text



if __name__ == '__main__':
    main()


# подумать над флагом - разрешением выбрать игру
# иначе при игре с числами - путаница
