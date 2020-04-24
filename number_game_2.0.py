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
            id_user = event.obj.message['from_id']
            flag = True

            game_flag = False

            number_game = False

            useful_flag = False
            form_procc = True

            print(event)
            print('Новое сообщение:')
            print('Для меня от:', event.obj.message['from_id'])
            print('Текст:', event.obj.message['text'])
            vk.messages.send(user_id=event.obj.message['from_id'],
                             message="Привет я бот(название бота)\n"
                                     "и вот что я могу:\n"
                                     "Игры\n"
                                     "Кое-что полезное",
                             random_id=random.randint(0, 2 ** 64))

        if event.type == VkBotEventType.MESSAGE_NEW and 'игр' in \
                event.obj.message['text'].lower() and flag:

            game_flag = True

            number_game = False
            numb_gm_ii, numb_gm_polz = False, False

            vk.messages.send(user_id=event.obj.message['from_id'],
                             message="Можем поиграть в:\n"
                                     "Камень ножницы бумага(1)\n"
                                     "Угадай число(2)\n"
                                     "Что бы выбрать напиши цифру в скобках",
                             random_id=random.randint(0, 2 ** 64))

        if event.type == VkBotEventType.MESSAGE_NEW and 'полезн' in \
                event.obj.message['text'].lower() and flag:

            useful_flag = True
            vk.messages.send(user_id=event.obj.message['from_id'],
                             message="Что я могу:\n"
                                     "Помочь принять решение(1)\n",
                             random_id=random.randint(0, 2 ** 64))

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

        if event.type == VkBotEventType.MESSAGE_NEW and event.obj.message[
            'text'] == '2' and flag and game_flag and not numb_gm_ii:

            number_game = True

            vk.messages.send(user_id=event.obj.message['from_id'],
                             message="Название: Угадай число\n"
                                     "Один из нас - Я или ВЫ - загадывает число от 1 до 999.\n"
                                     "Другой начинает начинает угадывать, называя числа, "
                                     "получая в ответ фразы 'больше' или 'меньше'.\n"
                                     "'Меньше' - загаданное число меньше Вашего.\n"
                                     "'Больше' - загаданное число больше Вашего.\n"
                                     "Напишите СТОП - если хотите завершить игру\n"
                                     "Кто загадывает число: Я или ВЫ?",
                             random_id=random.randint(0, 2 ** 64))

        if event.type == VkBotEventType.MESSAGE_NEW and \
                ((event.obj.message['text'].lower() == 'я' and flag and number_game) or \
                 (event.obj.message['text'].lower() in ["перезапустить", "не перезапускать", "стоп"]
                 and flag and number_game and numb_gm_polz)):

            numb_gm_polz = True
            numb_gm_p_cl = NumberGamePolz(number_game, numb_gm_polz)

            if event.obj.message['text'].lower() in ["не перезапускать", "стоп"]:
                number_game, numb_gm_polz = False, False

                vk.messages.send(user_id=event.obj.message['from_id'],
                                 message="Вот что я могу:\n"
                                         "Игры\n"
                                         "Кое-что полезное",
                                 random_id=random.randint(0, 2 ** 64))
            else:
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

                # number_game, numb_gm_polz, \
                text = numb_gm_p_cl.numb_game_plz_func\
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
        if event.type == VkBotEventType.MESSAGE_NEW and \
                ((event.obj.message[
                      'text'].lower() == 'вы' and flag and number_game) or \
                 (event.obj.message['text'].lower() in ["перезапустить",
                                                        "не перезапускать", "стоп"]
                  and flag and number_game and numb_gm_ii)):

            numb_gm_ii = True
            find_highest = False

            numb_gm_ii_cl = NumberGameII(number_game, numb_gm_ii, find_highest)

            if event.obj.message['text'].lower() in ["не перезапускать", "стоп"]:
                number_game, numb_gm_ii, find_highest = False, False, False

                vk.messages.send(user_id=event.obj.message['from_id'],
                                 message="Вот что я могу:\n"
                                         "Игры\n"
                                         "Кое-что полезное",
                                 random_id=random.randint(0, 2 ** 64))
            else:
                text = "Введите максимальное число, которое мне можно загадать\n"\
                       "Минимальное число - 0"

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

                text = numb_gm_ii_cl.numb_game_ii_func(event.obj.message['text'].lower())

                vk.messages.send(user_id=event.obj.message['from_id'],
                                 message=text,
                                 random_id=random.randint(0, 2 ** 64))

        if event.type == VkBotEventType.MESSAGE_NEW and event.obj.message[
            'text'] == '1' and flag and useful_flag and form_procc:
            form_procc = True
            kit = []

            vk.messages.send(user_id=event.obj.message['from_id'],
                             message="Я могу Вам помочь выбрать что-то "
                                     "из определённой последовательнсти "
                                     "предметов, которую Вы назовёте.\n"
                                     "Нужна такая помощь? ДА / НЕТ\n"
                                     "Напишите СТОП - если хотите завершить навык\n",
                             random_id=random.randint(0, 2 ** 64))

        if event.type == VkBotEventType.MESSAGE_NEW and ((event.obj.message[
            'text'].lower() in ['нет', 'да', "перезапустить", "не перезапускать", "стоп"] and flag and useful_flag and form_procc) or (event.obj.message[
            'text'].lower() == "стоп" and flag and useful_flag and not form_procc)):

            if event.obj.message['text'].lower() in ['нет', "не перезапускать", "стоп"]:

                text = "Ладно...А я ведь просто хотел помочь."
                useful_flag = False
                form_procc = True

                vk.messages.send(user_id=event.obj.message['from_id'],
                                 message=text,
                                 random_id=random.randint(0, 2 ** 64))

                vk.messages.send(user_id=event.obj.message['from_id'],
                                 message="Мои навыки:\n"
                                         "Игры\n"
                                         "Кое-что полезное",
                                 random_id=random.randint(0, 2 ** 64))

            else:
                form_procc = False
                kit = []
                text = f"Ура, ура, ура! Я с радостью Вам помогу.\n"\
                    "Введите все элементы последовательности, из которой"\
                    "мне нужно будет выбрать.\n"\
                    "В конце введите слово - ВЫБИРАЙ"
                vk.messages.send(user_id=event.obj.message['from_id'],
                                 message=text,
                                 random_id=random.randint(0, 2 ** 64))

        if event.type == VkBotEventType.MESSAGE_NEW and flag \
                and useful_flag and not form_procc and event.obj.message['text'].lower() == "выбирай":
            form_procc = True

            vk.messages.send(user_id=event.obj.message['from_id'],
                             message=f"Думаю, что {random.choice(kit[1:])} - "
                             "идеальный вариант!\n"
                             "Напишите мне -  ПЕРЕЗАПУСТИТЬ навык / НЕ ПЕРЕЗАПУСКАТЬ",
                             random_id=random.randint(0, 2 ** 64))

        if event.type == VkBotEventType.MESSAGE_NEW and flag and useful_flag and not form_procc:
            print(event.obj.message['text'].lower())

            kit.append(event.obj.message['text'])
            print(kit)


        elif event.type == VkBotEventType.MESSAGE_NEW and not flag:
            vk.messages.send(user_id=id_user,
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
                return f"Число {self.numbers[self.middle]} БОЛЬШЕ, МЕНЬШЕ "\
                           f"или РАВНО вашему числу?"
            else:
                return "Должно быть, Вы ошиблись. Такого числа нет в "\
                       "диапазоне от 1 до 1000\n"\
                       "Напишите мне -  ПЕРЕЗАПУСТИТЬ игру / НЕ ПЕРЕЗАПУСКАТЬ"

        elif answ == "равно":
            return f"Ура! У меня получилось !\n "\
                f"Ваше число : {self.numbers[self.middle]}\n"\
                "Напишите мне -  ПЕРЕЗАПУСТИТЬ игру / НЕ ПЕРЕЗАПУСКАТЬ"
        return "Должно быть, Вы ошиблись. Такого числа нет в " \
               "диапазоне от 1 до 1000\n" \
               "Напишите мне -  ПЕРЕЗАПУСТИТЬ игру / НЕ ПЕРЕЗАПУСКАТЬ"

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
        print(self.numb_ii)
        text = "Всё, я загадал число\n" \
               "Можете угадывать"
        self.find_h = True
        return self.number_game_fl, self.number_game_ii, self.find_h, text

    def numb_game_ii_func(self, answ):
        print(int(answ))
        if int(answ) < self.high and int(answ) >= 0:
            if int(answ) > self.numb_ii:
                text = "Не угадали. Мое число меньше."
            elif int(answ) < self.numb_ii:
                text = "Не угадали. Мое число больше."
            else:
                text = f"Ура ! Вы угадали, мое число {self.numb_ii}.\n" \
                    "Напишите мне -  ПЕРЕЗАПУСТИТЬ игру / НЕ ПЕРЕЗАПУСКАТЬ"

            print(self.numb_ii)
        else:
            text = "Точно нет...Вы сами себе противоречите...\n"\
                   f"Загадано число от 0 до {self.high}"
        return text

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


# подумать над флагом - разрешением выбрать игру
# иначе при игре с числами - путаница

# перезапуск рандомайзера - 1
