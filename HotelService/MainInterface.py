from HotelService.BoosInterface import BoosInterface
from HotelService.UsersInterface import UserInterface
import sys


class MainInterface:
    boosInterface = BoosInterface
    hotel = boosInterface.hotel
    userInterface = UserInterface

    def main_menu(self):
        print('       \'WELCOME TO HOTEL SERVICE APPLICATION\'     ', end='\n\n')

        while True:
            print('Hotel Manager Menu : \'1\'')
            print('User Menu : \'2\'')
            print('Exit : \'0\'')

            try:
                input_key = int(input())
            except ValueError:
                print('Wrong Input, Try again.')
                continue

            if input_key == 1:
                self.boosInterface.main_menu(BoosInterface, self.hotel)
                break
            elif input_key == 2:
                self.userInterface.main_menu(UserInterface, self.hotel)
                break
            elif input_key == 0:
                sys.exit()
            else:
                print('Wrong Input, Try again.')


MainInterface.main_menu(MainInterface)
