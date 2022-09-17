# Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит 2021 конфета. Играют два игрока, делая ход друг после друга. Первый ход определяется жеребьёвкой. 
# За один ход можно забрать не более чем 28 конфет. 
# Все конфеты оппонента достаются сделавшему последний ход. 
# Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?
# a) Добавьте игру против бота
# b) (доп) Подумайте как наделить бота ""интеллектом""

from random import randint

n = 202
m = 28

def human():
    first_player = input('Первый игрок, введите Ваше имя: ')
    second_player = input('Второй игрок, введите Ваше имя: ')

    def play_game(n, players):
        count = 0
        while n > 0:
            size = int(input(f'\n{players[count % 2]}, Ваш ход: '))
            if size > 28 or size <= 0:
                attempt = 3
                print('Ошибка!')
                while attempt > 0:
                    size = int(input(f'Осталось попыток {attempt}. Введите число от 1 до 28: '))
                    if size > 28 or size <= 0:
                        attempt -= 1
                    else:
                        break
                if attempt == 0:
                    return print('Вы проиграли!')
            n = n - size
            if n > 0:
                print(f'Осталось конфет = {n}')
            else: 
                print('Конфет больше нет.')
            count += 1
        return players[not count % 2]

    players = [first_player, second_player]

    winer = play_game(n, players)
    if not winer:
        print('Нет победителя.')
    else:
        print(f'Поздравляю! Победил {winer}.')
    return

def bot():
    player = input('Введите Ваше имя: ')
    bot_player = 1 
    def play_game_with_bot(n, player):
        count = 0
        while n > 0:
            count = count % 2
            if count == 1:
                num = randint(1, 29)
                print(f'\n{bot_player}Ходит бот: {num}')
                n = n - num
                if n > 0:
                    print(f'Осталось конфет = {n}')
                else: 
                    print('Конфет больше нет.')
            if count == 0:
                size = int(input(f'\n{player}, Ваш ход: '))
                if size > 28 or size <= 0:
                    attempt = 3
                    print('Ошибка!')
                    while attempt > 0:
                        size = int(input(f'Осталось попыток {attempt}. Введите число от 1 до 28: '))
                        if size > 28 or size <= 0:
                            attempt -= 1
                        else:
                            break
                    if attempt == 0:
                        return print('Вы проиграли!')
                n = n - size
                if n > 0:
                    print(f'Осталось конфет = {n}')
                else: 
                    print('Конфет больше нет.')
            count += 1
        return player[not count % 2]
    play_game_with_bot(n, player)

    players = [player, bot_player]
    winer = play_game_with_bot(n, player)
    if not winer:
        print('Нет победителя.')
    else:
        print(f'Поздравляю! Победил {winer}.')
    return
    
result = int(input('С кем вы хотите играть? Если с человеком, введите 1. Если с ботом, введите 2: '))
if result == 1:
    human()
if result == 2:
    bot()
else: 
    print('Введите 1 или 2!')


print(f'Правила игры: \n1) На столе лежит {n} конфета.' 
'Играют два игрока, делая ход друг после друга. \n2) За один ход можно забрать не более {m} конфет.' 
'\n3) Все конфеты оппонента достаются тому, кто сделал последний ход. \nУдачной игры!\n')
