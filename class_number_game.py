class NumberGame:
    def __init__(self):
        self.maxim = 1000
        self.minim = 0
        self.find = int(input("find number: "))
        self.numbers = [i for i in range(1000)]
        self.middle = (self.minim + self.maxim) // 2
        print(self.number_game_func())

    def number_game_func(self):
        while self.minim < self.maxim - 1:
            # self.middle = (self.minim + self.maxim) // 2

            print(f"Число {self.numbers[self.middle]} БОЛЬШЕ, МЕНЬШЕ или РАВНО вашему числу?")
            answ = input().lower()

            if answ == "меньше":
                self.minim = self.middle
                # print('minim:', self.minim)
            elif answ == "больше":
                self.maxim = self.middle
                # print('maxim: ', self.maxim)
            elif answ == "равно":
                return f"Ура! У меня получилось !\n " \
                    f"Ваше число : {self.numbers[self.middle]}"

            self.middle = (self.minim + self.maxim) // 2

            print(self.minim)
            print(self.maxim)
            print('middle', self.middle)
        print("Должно быть, Вы ошиблись. Такого числа нет в диапазоне от 1 до 999")


print(NumberGame())