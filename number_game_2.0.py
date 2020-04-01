import vk_api
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
import random
import time


maxim = 1000
minim = 1
numbers = [i for i in range(1000)]
middle = (minim + maxim) // 2
number_game = False
user_find_h = True


def main():
    global maxim, middle, minim, numbers, number_game
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

        if event.type == VkBotEventType.MESSAGE_NEW and 'игр' in event.obj.message[
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
            vk.messages.send(user_id=event.obj.message['from_id'],
                             message="Название: Угадай число\n"
                             "Один из нас - Я или ВЫ - загадывает число от 1 до 1000.\n"
                             "Другой начинает начинает угадывать, называя числа, "
                             "получая в ответ фразы 'больше' или 'меньше'.\n"
                             "'Меньше' - загаданное число меньше Вашего.\n"
                             "'Больше' - загаданное число больше Вашего.\n"
                             "Кто загадывает число: Я или ВЫ?",
                             random_id=random.randint(0, 2 ** 64))

        if event.type == VkBotEventType.MESSAGE_NEW and event.obj.message[
            'text'].lower() == 'я' and flag and number_game:

                text = number_game_answer(event.obj.message['text'].lower())

                vk.messages.send(user_id=event.obj.message['from_id'],
                                 message=text,
                                 random_id=random.randint(0, 2 ** 64))

        if event.type == VkBotEventType.MESSAGE_NEW and event.obj.message[
            'text'].lower() in ['больш', 'меньш', 'равн'] and flag and number_game:

            text = number_game_answer(event.obj.message['text'].lower())

            vk.messages.send(user_id=event.obj.message['from_id'],
                             message=text,
                             random_id=random.randint(0, 2 ** 64))

        if event.type == VkBotEventType.MESSAGE_NEW and event.obj.message[
            'text'].lower() == 'вы' and flag and number_game and user_find_h:
                text = number_game_answer(event.obj.message['text'].lower())

                vk.messages.send(user_id=event.obj.message['from_id'],
                                 message=text,
                                 random_id=random.randint(0, 2 ** 64))

        if event.type == VkBotEventType.MESSAGE_NEW and event.obj.message[
            'text'].isdigit() and flag and number_game and not user_find_h:
            text = number_game_answer(event.obj.message['text'].lower())

            vk.messages.send(user_id=event.obj.message['from_id'],
                             message=text,
                             random_id=random.randint(0, 2 ** 64))

        elif event.type == VkBotEventType.MESSAGE_NEW and not flag:
            vk.messages.send(user_id=event.obj.message['from_id'],
                             message="Для начала работы напишите 'Начать'",
                             random_id=random.randint(0, 2 ** 64))


def number_game_answer(answ):
    global maxim, middle, minim, numbers, number_game, user_find_h
    err = "Должно быть, Вы ошиблись. Такого\n " \
                   "числа нет в диапазоне от 1 до 1000"
    if answ == 'я':
        text = "Хорошо. Загадывайте число.\n" \
            f"Число {numbers[middle]} БОЛЬШЕ, \n" \
               "МЕНЬШЕ или РАВНО вашему числу?"
    elif answ == 'вы':
        text = "Хорошо. До какого числа я могу загадать?\n"\
               "Введите максимальное число."
    elif answ in ['больш', 'меньш', 'равн']:
        if answ == 'больш':
            if minim <= maxim - 1:
                maxim, middle = middle, (minim + maxim) // 2
                text = f"Число {numbers[middle]} БОЛЬШЕ, \n"\
                           "МЕНЬШЕ или РАВНО вашему числу?"
            else:
                text = err
        elif answ == 'меньш':
            minim, middle = middle, (minim + maxim) // 2
            if minim < maxim - 1:
                text = f"Число {numbers[middle]} БОЛЬШЕ, \n"\
                           "МЕНЬШЕ или РАВНО вашему числу?"
            else:
                text = err
        elif answ == 'равн':
            text = f"Ура! У меня получилось !\n"\
                           f"Ваше число : {numbers[middle]}"
            number_game = False

            maxim = 1000
            minim = 1
            numbers = [i for i in range(1000)]
            middle = (minim + maxim) // 2
    elif answ.isdigit():
        if user_find_h:
            ii_numb = random.randint(0, int(int(answ)))
            text = "Всё, я загадал число\n"\
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
