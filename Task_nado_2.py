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
    print('Игра с человеком!')
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
    print('Игра с ботом!')
    player = input('Введите Ваше имя: ')
    bot_player = 1 
    def play_game_with_bot(n, player):
        count = 0
        while n > 0:
            count = count % 2
            if count == 1:
                num = randint(1, 29)
                print(f'\nХодит бот: {num}')
                n = n - num
                counting(n, count, player)
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
                counting(n, count, player)
            count += 1
    play_game_with_bot(n, player)

def players_choice():
    num = str(input('\nВведите слово ЧЕЛОВЕК, если хотите сыграть с человеком или БОТ, если с ботом: ').lower())
    if num == 'человек':
        rules()
        human()
    if num == 'бот':
        rules()
        bot()
    if num != 'человек' and num != 'бот':
        print('Можно ввести только ЧЕЛОВЕК или БОТ! Повторите попытку.')
        players_choice()
    
def rules():
    print(f'Правила игры: \n1) На столе лежит {n} конфета.' 
    'Играют два игрока, делая ход друг после друга. \n2) За один ход можно забрать не более {m} конфет.' 
    '\n3) Все конфеты оппонента достаются тому, кто сделал последний ход. \nУдачной игры!\n')

def counting(n, count, player):
    if n > 0:
        print(f'Осталось конфет = {n}')
    else: 
        print('Конфет больше нет.')
        if count == 0:
            print(f'\n{player}, примите наши поздравления, Вы выиграли!')
        if count == 1:
            print(f'\n{player}, Вы проиграли. Выиграл бот!')

players_choice()