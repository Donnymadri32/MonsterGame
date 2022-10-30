# This is the code for our Pokemon project

#This is the function for the tackle attack.
def tackle(pokemonone, pokemontwo):
    pokemontwo.health = pokemontwo.health - pokemonone.attack

#This creates Pokemon objects
class Pokemon():

    def __init__(self, name, attack, health):
        self.name = name
        self.attack = attack
        self.health = health

#This will be the Pokemon we will battle
Pikachu = Pokemon('Pikachu', 100, 100)

#The beginning of the game
while True:
    try:
        print('Welcome to the world of Pokemon!')
        firstresponse = input("Which Pokemon would you like to pick?\n"
                          "Press 1 for Squirtle\n"
                          "Press 2 for Charmander\n"
                          "Press 3 for Bulbasaur\n")

        if int(firstresponse) < 1:
            continue

        elif int(firstresponse) > 3:
            continue

        elif int(firstresponse) == 1:
            squirtle = Pokemon('Squirtle', 100, 100)
            print('You have selected Squirtle!\n')
            print('The battle will now begin!\n')
            try:
                fightone = int(input('A trainer and his Pikachu have appeared!\n'
                             'Get ready for battle!\n'
                                 'What attack?\n'
                                 '1 for tackle\n'
                                 '2 for growl\n'
                                 '3 for bulbbe\n'))

                if fightone < 1:
                    continue
                elif fightone > 3:
                    continue
                elif fightone == 1:
                    tackle(squirtle, Pikachu)
                    break
            except ValueError:
                print('Opps! You did not enter a valid command.  Try again')
                break

        elif int(firstresponse) == 2:
            charmander = Pokemon('Charmander', 100, 100)
            print('You have selected Charmander!')
            break

        elif int(firstresponse) == 3:
            bulbasaur = Pokemon('Bulbasaur', 100, 100)
            print('You have selected Bulbasaur!')
            break

    except ValueError:
        print("Opps! You did not enter a valid selection.  Try again")

