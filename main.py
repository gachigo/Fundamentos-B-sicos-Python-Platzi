import random

options = ('piedra', 'papel', 'tijera')

rounds = 1
computer_option_win = 0
user_option_win = 0
winner = "toste"

while True :

    user_option = input("¿Piedra, papel ó tijera? => ")
    user_option = user_option.lower()
    computer_option = random.choice(options)
    print('*' * 20)
    print(f'R - O - U - N - D   [{rounds}]')
    print('*' * 20)
    
    print("Elegiste => ", user_option)
    print("La Maquina Eligio => ", computer_option)

    if not user_option in options:
        print('Esa opción no existe')

    if user_option == computer_option:
        print('Empate')
    elif user_option == 'piedra':
        if computer_option == 'tijera':
            print('Piedra gana a tijera')
            print('¡Ganaste!')
            user_option_win += 1
        else:
            print('papel gana a piedra')
            print('La Computadora ganó')
            computer_option_win += 1
    elif user_option == 'papel':
        if computer_option == 'piedra':
            print('Papel gana a piedra')
            print('¡Ganaste!')
            user_option_win += 1
        else:
            print('Tijera gana a papel')
            print('La Computadora ganó')
            computer_option_win += 1
    elif user_option == 'tijera':
        if computer_option == 'papel':
            print('Tijera gana a papel')
            print('¡Ganaste!')
            user_option_win += 1
        else:
            print('Piedra gana a Tijera')
            print('La Computadora ganó')
            computer_option_win += 1
    rounds += 1
    print('*' * 20)
    print(f'USER WINS => [{user_option_win}] & PC WINS => [{computer_option_win}]')
    print('*' * 20)
    if computer_option_win == 3:
            winner = 'THE FUCKING PC'
    elif user_option_win == 3:
            winner = 'THE FUCKING USER'
    if computer_option_win == 3 or user_option_win == 3:  
        print('*' * 40)
        print('*' * 40)
        print('*' * 40)
        print(f"T-H-E  W-I-N-N-E-R  I-S [{winner}]")
        print('*' * 40)
        print('*' * 40)
        print('*' * 40)
        break

    