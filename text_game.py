inventory=[]
import random

def winner():
    print('congrants you won the game!')

def loser():
    print('sorry! you lose!')

def path1():
    print('select your path; left(L) OR right (R)')
    choice1=input().strip().lower()

    if choice1=='l':
        path1_left()

    elif choice1=='r':
        path1_right()

    else:
        print('select appropriate choice!')
        path1()

def path1_left():
    print(''' YOu chose to take the left turn!
        Path 1: The Left Tunnel 
        Stepping cautiously into the left passage, you notice a faint golden glimmer ahead. 
        As you get closer, you see an old wooden chest, covered in dust and cobwebs.

        🛠 Choice 1: Open the Chest or Ignore It?''')

    print('OPen the chest(O) or Ignore it(i)?')
    choice1l=input('')

    if choice1l=='o':
        chest()

    elif choice1l=='i':
        ignore()

    else:
        print('select appropriate choice!')
        path1_left()


def path1_right():
    print(''' YOu chose to take the right turn!
        You step into the right tunnel, feeling the temperature drop as you move forward. A strange growling noise comes from the shadows. You freeze. Two glowing red eyes appear ahead.

        A huge beast—half-wolf, half-reptile—lunges at you!

        🛠 Choice 1: Fight(f) or Run?(r)''')

    print('Fight(f) or Run(r)??')
    choice1r=input()

    if choice1r=='f':
        fight()

    elif choice1r=='r':
        run()

    else:
        print('select appropriate choice!')
        path1_right()


def chest():
    seeder=[1,2]
    seed=random.choice(seeder)
    if seed == 1:
        print('you found a bag of gold and a sword! added to the inventory')
        inventory.append('sword')
        inventory.append('gold')

        crawl_space()

    else:
        print('A dart shoots out, poisoning you. You are dead!')
        loser()


def crawl_space():
    print('''
    Further ahead, the tunnel narrows into a crawl space. You squeeze through and find an underground lake. A rickety old boat floats on the water.

🛠 Choice 2: Swim or Take the Boat?
    ''')

    print('do you wish to swim(s) or take the boat(b)?')

    crawl_choice= input()
    if crawl_choice == 's':
        print('Swim → The water is freezing. Halfway through, you feel something grab your leg..')
        if 'sword' in inventory:
            print('you have the sword, you fight it off.')
            winner()

        else:
            print(' the creature drags you under—game over! since you have no sword!')
            loser()

    elif crawl_choice == 'b':
        print('''The boat creaks but holds steady. 
        You safely reach the other side, where a ladder leads out of the cave—you win!''')
        winner()

    else:
        print('please selec the coreect')
        crawl_space()

def ignore():
    crawl_space()

def fight():
    print(' The beast rips you apart—game over!')
    loser()

def run():
    print(' You sprint down the tunnel. The beast chases you, but you spot a small crevice in the wall.')
    print('Squeeze through → You barely fit, but the monster can’t reach you.')
    print('you reach a hidden passage leading outside—you win! 🎉')
    winner()


print(
    '''
 Introduction: The Awakening
You wake up in complete darkness, lying on a cold, damp surface. A faint, musty smell fills your nostrils, 
and the distant sound of dripping water echoes through what seems to be a vast, underground cavern. 
Your head throbs, and your memory is foggy—you have no recollection of how you got here.

As you sit up and rub your temples, your eyes adjust to the dim light filtering through cracks in the 
cave walls. The rocky floor beneath you is uneven, scattered with loose stones and what feels like... bones?


Panic creeps in. You need to get out.

In front of you, two paths lead deeper into the unknown. One veers left, where the air feels slightly 
warmer, and you hear faint rustling sounds. The other leads right, where the path is cold and eerily silent.

    '''
)

print('select your path; left(L) OR right (R)')

path1()