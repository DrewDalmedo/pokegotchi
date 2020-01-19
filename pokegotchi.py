from os import system, name
# from time import *

def clear_term():
    if name == 'nt':
        clear_statement = system('cls')
    else:
        clear_statement = system('clear')

# not yet implemented, reserved for the future
def display_location():
    print('placeholder')

def main():
    running: bool = True

    ''' 
    LOCATION ID'S
    0 = bedroom / main menu (lights, tuck in, stats)
    1 = dining room (feed)
    2 = bathroom (bath / clean)
    3 = outdoors (play)
    4 = doctor (medicine)
    5 = location selector
    '''
    location_id: int = 0;  # defaults to main menu / bedroom

    while running:
        clear_term()
        if (location_id == 0):
            print('1) Feed \n2) Lights \n3) Play \n4) Medicine \n5) Bath \n6) Stats \n7) Scold')
        user_input: int = int(input("$ "))



main()
