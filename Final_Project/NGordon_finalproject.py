print('A text adventure game by Natasha Gordon')

name = input('Please type your name.\n')
neighborhood = input('what neighborhood do you live in?\n')

pocket_right = {'a screwdriver', 'a piece of candy'}
pocket_left = {'a small baby frog', 'a deflated balloon', 'a long knife'}

pockets = pocket_left.union(pocket_right)

class Character:
    def _init_(self, name, neighborhood):
        self.name = name
        self.neighborhood = neighborhood
    print('Hello {}. You are in {}. You step out of your front door and notice a green shape moving towards you down the street, in the direction of your subway station.'.format(name, neighborhood))
    print()
    print('The shape materializes into a frog the size of a baby elephant. What do you do?')
    print()

    first_action = int(input('\nType 1 to run from the frog. \nType 2 to continue down the street towards the frog.\n Type 3 to re-enter your home.'))

    if first_action == 1:
        print('You run from the frog. It follows you down to the water and eats you. \n*Game Over*')
    elif first_action == 3:
        print('You turn back inside and lock the door to wait until the coast is clear.')
        print()
        home_action = input('Type sleep to go back to sleep. \nType quit to surrender to your panic.')
        if home_action == 'sleep':
            print('You wake up the next morning thinking it was all a strange dream.\n*Congratulations, you return to your normal life.*')
            print('========================================')
        elif home_action == 'quit':
            print('Panic cannot save you from the frog. \n*Game Over*')
    if first_action == 2:
        print('You continue down the street towards the frog. When you reach the frog, it stops and stares at you. It tells you to look into your pockets.')
        print()
        pocket_action = input('Press P to reach into your pockets.')
        if pocket_action == 'P' or 'p':
                print('You reach into your pockets. Your right pocket contains {}. Your left pocket contains {}'.format(pocket_right, pocket_left))
                print()
                print('The frog asks you what you have found. You respond {}'.format(pockets))
        else:
            print('That is not a viable command. Please try again.')
        pass

        second_action = input('Type 1 to fight the big frog. \nType 2 to kiss the big frog. \nType 3 to release the baby frog. \n')
        if second_action == 1:
            print('You pull out the long knife and rush towards the big frog. \nBAM\nIts tongue lashes out and curls around you. The last thing you see is the baby frog hopping away as you fade to dark. \n*Game Over*\n')
        elif second_action == 2:
            print('This is not that kind of story. The big frog gives you a horrified look and quickly eats you. \n*Game Over*')
        elif second_action == 3:
            print('You reach into your pocket and gently lift out the baby frog. You place it on the ground and it *ribbits* before hopping over to the big frog.')
            print('The baby frog hops onto the big frog and they both let out a final *ribbit* before the big frog walks away down the street. \nCongratulations {}, you have won the game.'.format(name))
        else:
            print('Sorry, you will have to learn to follow directions. \n *Game Over*')
