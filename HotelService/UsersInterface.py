from HotelService.models.Hotel import Hotel
from HotelService.models.User import User
from HotelService.models.Room import Room
from HotelService.models.Service import Service
import sys


class UserInterface:
    hotel = Hotel
    user = User

    def main_menu(self, hotel):
        self.hotel = hotel
        print('    *Users Menu*    ', end='\n\n')

        while True:
            print('Enter \'1\' to reserve new room.')
            print('Enter \'2\' to reserve new service.')
            print('Enter \'3\' to see bill.')
            print('Enter \'0\' to exit.')

            try:
                input_key = int(input())
            except ValueError:
                print('Wrong Input, Try again.')
                continue

            if input_key == 1:
                self.room_view(UserInterface)
                break
            elif input_key == 2:
                self.service_view(UserInterface)
                break
            elif input_key == 3:
                self.see_bill(UserInterface)
                break
            elif input_key == 0:
                sys.exit()
            else:
                print('Wrong Input.')

    def room_view(self):
        print('    *Room view*    \n')
        for room in self.hotel.rooms:
            print(f'{room.room_num}_ number bed: {room.bed_num}, cost: {room.cost}')
        while True:
            print('Chose room number to see it\'s details[back: \'0\']')
            try:
                input_key = int(input())
                if input_key == 0:
                    self.main_menu(UserInterface, self.hotel)
                else:
                    for room_index in self.hotel.rooms:
                        if room_index.room_num == input_key:
                            print(room_index.to_string(Room))
                            if room_index.is_fill:
                                input('Enter any key to back... ')
                                self.room_view(UserInterface)
                            else:
                                input_key_2 = int(input('Enter \'1\' to reserve room.\nEnter \'0\' to back.'))
                                if input_key_2 == 1:
                                    self.reserve_room(UserInterface,room_index)
                                elif input_key_2 == 0:
                                    self.room_view(UserInterface)
            except ValueError:
                print('Wrong input.')

    def reserve_room(self, room):
        self.user.name = input('Enter your name : ')
        self.user.age = int(input('Enter your age : '))
        self.user.phone_num = input('Enter your phone number : ')
        self.user.email_address = input('Enter your email address : ')
        self.user.comrades_num = int(input('Enter number of your participants : '))
        if self.user.comrades_num > 0:
            for index in range(self.user.comrades_num):
                print(f'For {index+1},')
                name = input('Name : ')
                age = int(input('Age : '))
                phone_num = input('Phone number : ')
                room_num = room.room_num
                new_comrade = {
                    'comrade_name': name,
                    'age': age,
                    'phone_num': phone_num,
                    'room_num': room_num
                }
                self.user.comrades.append(new_comrade)
        self.user.room_num = room.room_num
        self.user.bill = room.cost

    def service_view(self):
        print('    *Services view*    \n')
        if self.user.room_num == 0:
            print('You have no room reserved, you can\'t reserved service.')
            self.main_menu(UserInterface, self.hotel)
        counter = 1
        for service in self.hotel.services:
            print(f'{counter}_ name: {service.service_name}, cost per person: {service.cost_per_person}')
            counter += 1
        while True:
            print('Chose service number to see it\'s details[back: \'0\']')
            try:
                input_key = int(input())
                if input_key == 0:
                    self.main_menu(UserInterface, self.hotel)
                else:
                    new_service = self.hotel.services[input_key - 1]
                    new_service.person_number = self.hotel.rooms[self.user.room_num].bed_num
                    print(new_service.to_string(Service))
                    input_key_2 = int(input('Enter \'1\' to reserve service.\nEnter \'0\' to back.'))
                    if input_key_2 == 1:
                        self.user.bill += new_service.final_cost
                        self.user.user_services.append(new_service)
                    elif input_key_2 == 0:
                        self.service_view(UserInterface)
            except ValueError and IndexError:
                print('Wrong input.')

    def see_bill(self):
        print('Your bill.\n')
        print(f'Cost of room : {self.hotel.rooms[self.user.room_num].cost}')
        for item in self.user.user_services:
            print(f'Service name : {item.service_name}, cost: {item.final_cost}')
        print(f'Final cost for you : {self.user.bill}')
        if self.user.is_payed:
            print('It has payed.')
        else:
            print('It hasn\'t payed.')
        input('enter any key to back...')
        self.main_menu(UserInterface, self.hotel)
