gran_up = 100
gran_down = 0
is_game_over = False
while not is_game_over:
    middle = (gran_down + gran_up) // 2
    print(f'{middle}?')
    answer = input()
    
    if answer == 'больше':
        gran_down = middle
    elif answer == 'меньше':
        gran_up = middle
    elif answer == 'угадал':
        is_game_over = True
        print('ура! я выиграл!')
    else:
        print('непонятный ответ, попробуй еще раз')
    if middle == 99 and answer == 'больше':
        print('значит ты загадал число 100!')
        print('ура! я выиграл!')
        is_game_over = True
    