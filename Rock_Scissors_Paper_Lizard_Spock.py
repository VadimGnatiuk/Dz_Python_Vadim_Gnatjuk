# Rock Scissors Paper  /// Камень Ножницы Бумага
'''
Проведем игру в 3 раунда!           Let's play 3 rounds!
Вы указали неверный вариант! Выберите [r],[p],[s],[l],[k].
'''
# Объявление переменных
import random

player_score = 0
bot_score = 0
player_choice = ''
bot_choice = ''
game = True  # Game repeat
# i = 0#только для while
# while player_score <= 3 and bot_score <= 3:
while game:
    for i in range(1, 4):  # Игра на 3 раунда.
        # i = i + 1#только для while
        print('Let\'s play 3 rounds!')
        print(f'ROUND {i}')
        # Ход игрока 1
        player_choice = ''
        while player_choice != 'r' and player_choice != 'p' and player_choice != 's' and player_choice != 'l' and player_choice != 'k':
            player_choice = str(input("Enter [r],[p],[s],[l],[k] : "))  # l - Lizard, k -Spock
            if player_choice != 'r' and player_choice != 'p' and player_choice != 's' and player_choice != 'l' and player_choice != 'k':
                print('You have entered the wrong option! Select [r],[p],[s],[l],[k].')
        # Ход игрока 2 / бота
        bot_choice = random.choice('rpslk')
        # Обратная связь
        print(f'Player choice : {player_choice} Bot choice : {bot_choice}')
        while player_choice == bot_choice:
            print('Draw round!')
            # ---Ничью нужно переиграть------------------------------------
            print('Draw needs to be replayed!')
            player_choice = ''
            while player_choice != 'r' and player_choice != 'p' and player_choice != 's' and player_choice != 'l' and player_choice != 'k':
                player_choice = str(input("Enter [r],[p],[s],[l],[k] : "))  # l - Lizard, k -Spock
            # Ход игрока 2 / бота
            bot_choice = random.choice('rps')
            # Обратная связь
            print(f'Player choice : {player_choice} Bot choice : {bot_choice}')
        # -------------------------------------------------------------
        if player_choice == 'r':
            if bot_choice == 's' or bot_choice == 'l':
                print('Player won the round!')
                player_score = player_score + 1
            else:
                print('Bot won the round!')
                bot_score = bot_score + 1
        elif player_choice == 's':
            if bot_choice == 'p' or bot_choice == 'l':
                print('Player won the round!')
                player_score = player_score + 1
            else:
                print('Bot won the round!')
                bot_score = bot_score + 1
        elif player_choice == 'p':
            if bot_choice == 'r' or bot_choice == 'k':
                print('Player won the round!')
                player_score = player_score + 1
            else:
                print('Bot won the round!')
                bot_score = bot_score + 1
        elif player_choice == 'l':
            if bot_choice == 'p' or bot_choice == 'k':
                print('Player won the round!')
                player_score = player_score + 1
            else:
                print('Bot won the round!')
                bot_score = bot_score + 1
        elif player_choice == 'k':
            if bot_choice == 's' or bot_choice == 'r':
                print('Player won the round!')
                player_score = player_score + 1
            else:
                print('Bot won the round!')
                bot_score = bot_score + 1
    if player_score == bot_score:
        print('Draw game')
    elif player_score > bot_score:
        print('Player won game!')
    elif player_score < bot_score:
        print('Bot won game!')
    game = str(input("Press [any key] + [enter] to continue \n or press [enter] to exit : "))
