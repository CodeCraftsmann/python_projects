import random

def breaker():
        while True:
            breaker_prompt=input('do you wish to proceed. Y or N')
            if breaker_prompt == 'Y':
                return True
            elif breaker_prompt == 'N':
                return False
            else:
                print('please select Y or N')

while True:
    

    user_input=input('Enter S for stone P for paper and X for scissors')
    choices=['S', 'P', 'X']
    select=random.choice(choices)


    if user_input in choices:
        print(f'you selected {user_input}, and computer selected {select}')

        if user_input==select:
            print('its a draw!')
            #breaker()

        elif user_input == 'S':
            if select == 'p':
                print('computer wins!')
                #breaker()

            else:
                print('user wins!')
                #breaker()



        elif user_input == 'P':
            if select == 'X':
                print('computer wins!')
                #breaker()

            else:
                print('user wins!')
                #breaker()


        elif user_input == 'X':
            if select == 'S':
                print('computer wins!')
                #breaker()

            else:
                print('user wins!')
        if not breaker():
            break

    else:
        print('PLEASE SELECT APPROPRITATE CHOICE FROM S P AND X!')
        if not breaker():
            break
        

        

    
