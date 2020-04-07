import vk_api
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
import random
import time

maxim = 1000
minim = 0
numbers = [i for i in range(1000)]
number_game = False
user_find_h = True
numb_game_find = False
numb_game_pr = False
print(number_game, numb_game_find, numb_game_pr)


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
            numb_game_pr = True
            vk.messages.send(user_id=event.obj.message['from_id'],
                             message="Название: Угадай число\n"
                                     "Один из нас - Я или ВЫ - загадывает число от 1 до 1000.\n"
                                     "Другой начинает начинает угадывать, называя числа, "
                                     "получая в ответ фразы 'больше' или 'меньше'.\n"
                                     "'Меньше' - загаданное число меньше Вашего.\n"
                                     "'Больше' - загаданное число больше Вашего.\n"
                                     "Кто загадывает число: Я или ВЫ?",
                             random_id=random.randint(0, 2 ** 64))
            # print(number_game, numb_game_find, numb_game_pr)

        if event.type == VkBotEventType.MESSAGE_NEW and event.obj.message[
            'text'].lower() == 'я' and flag and number_game:
            # numb_game_find = True
            # numb_game_find = False
            print(number_game, numb_game_find, numb_game_pr)

            maxim = 1000
            minim = 0

            numbers = [i for i in range(1000)]

            middle = (minim + maxim) // 2

            text = "Хорошо. Загадывайте число.\n" \
                   "Загадали? ДА / НЕТ"

            vk.messages.send(user_id=event.obj.message['from_id'],
                             message=text,
                             random_id=random.randint(0, 2 ** 64))

        if event.type == VkBotEventType.MESSAGE_NEW and event.obj.message[
            'text'].lower() in ['нет', 'да'] and flag and number_game:
            if event.obj.message['text'].lower() == 'нет':
                text = "Ладно, я могу подождпть.\n" \
                       "А теперь загадали? ДА / НЕТ"

                vk.messages.send(user_id=event.obj.message['from_id'],
                                 message=text,
                                 random_id=random.randint(0, 2 ** 64))

            else:
                text = number_game_i("да")

                vk.messages.send(user_id=event.obj.message['from_id'],
                                 message=text,
                                 random_id=random.randint(0, 2 ** 64))

        if event.type == VkBotEventType.MESSAGE_NEW and event.obj.message[
            'text'].lower() in ['больше', 'меньше',
                                'равно'] and flag and number_game:
            # middle = (minim + maxim) // 2
            text = number_game_i(event.obj.message['text'].lower())

            vk.messages.send(user_id=event.obj.message['from_id'],
                             message=text,
                             random_id=random.randint(0, 2 ** 64))

        if event.type == VkBotEventType.MESSAGE_NEW and event.obj.message[
            'text'].lower() == 'вы' and flag and number_game and user_find_h:
            text = number_game_i(event.obj.message['text'].lower())

            vk.messages.send(user_id=event.obj.message['from_id'],
                             message=text,
                             random_id=random.randint(0, 2 ** 64))

        if event.type == VkBotEventType.MESSAGE_NEW and event.obj.message[
            'text'].isdigit() and flag and number_game and not user_find_h:
            text = number_game_i(event.obj.message['text'].lower())

            vk.messages.send(user_id=event.obj.message['from_id'],
                             message=text,
                             random_id=random.randint(0, 2 ** 64))

        elif event.type == VkBotEventType.MESSAGE_NEW and not flag:
            vk.messages.send(user_id=event.obj.message['from_id'],
                             message="Для начала работы напишите 'Начать'",
                             random_id=random.randint(0, 2 ** 64))


def number_game_i(answ, *ii_numb):
    global maxim, middle, minim, numbers, number_game, user_find_h, numb_game_find, numb_game_pr
    err = "Должно быть, Вы ошиблись.\n" \
          "Такого числа нет в диапазоне от 1 до 1000"

    if answ == 'да':
        if minim < maxim - 1:
            middle = (minim + maxim) // 2

            text = "Хорошо. Начинаю угадывать\n" \
                f"Число {numbers[middle]} БОЛЬШЕ, \n" \
                   "МЕНЬШЕ или РАВНО вашему числу?"

    elif answ in ['больше', 'меньше', 'равно']:

        if minim < maxim - 1:
            if answ == 'больше':
                maxim = middle
                # middle = (minim + maxim) // 2
                text = f"Число {numbers[middle]} БОЛЬШЕ, \n" \
                    "МЕНЬШЕ или РАВНО вашему числу?"
            elif answ == 'меньше':
                minim = middle
                # middle = (minim + maxim) // 2
                text = f"Число {numbers[middle]} БОЛЬШЕ, \n" \
                    "МЕНЬШЕ или РАВНО вашему числу?"
            elif answ == 'равно':

                text = f"Ура! У меня получилось !\n" \
                    f"Ваше число : {numbers[middle]}"
            middle = (minim + maxim) // 2
        else:
            text = err
            '''if minim >= 0 and numb_game_find:

                text = f"Ура! У меня получилось !\n" \
                        f"Ваше число : {numbers[middle]}"
                number_game = False
                numb_game_find = False
                numb_game_pr = False
                print(number_game, numb_game_find, numb_game_pr)

                maxim = 1000
                minim = 1
                numbers = [i for i in range(1000)]
            elif minim >= 0 and numb_game_pr:
                text = err

                number_game = False
                numb_game_find = False
                numb_game_pr = False
                print(number_game, numb_game_find, numb_game_pr)
                maxim = 1000
                minim = 1
                numbers = [i for i in range(1000)]'''

    elif answ.isdigit():
        if user_find_h:
            ii_numb = random.randint(0, int(int(answ)))
            text = "Всё, я загадал число\n" \
                   "Можете угадывать"
            user_find_h = False

        if int(answ) > ii_numb and not user_find_h:
            text = "Не угадали. Мое число меньше."
        elif int(answ) < ii_numb and not user_find_h:
            text = "Не угадали. Мое число больше."
        else:
            text = f"Ура ! Вы угадали, мое число {ii_numb}."
    else:
        text = "Я Вас не понимаю"

    return text


if __name__ == '__main__':
    main()
