from HotelService.UsersInterface import UserInterface
from HotelService.models.Hotel import Hotel
from HotelService.models.Room import Room
from HotelService.models.Service import Service
import sys


def set_bed_type(bed_index):
    while True:
        print(f'Type of bed.[Bed number is {bed_index+1}]')
        print('Enter \'1\' for \'SINGLE\'.')
        print('Enter \'2\' for \'DOUBLE\'.')

        try:
            input_key = int(input())
            if input_key == 1:
                return 'SINGLE', 1
            elif input_key == 2:
                return 'DOUBLE', 2
            else:
                print('Wrong input.')
        except ValueError:
            print('Wrong input.')


class BoosInterface:
    hotel = Hotel

    def main_menu(self, hotel):
        self.hotel = hotel
        print('    *Hotel Manager Menu*    ', end='\n\n')

        while True:
            print('Enter \'1\' to add new room.')
            print('Enter \'2\' to add new service.')
            print('Enter \'3\' to see hotel rooms.')
            print('Enter \'4\' to see hotel services.')
            print('Enter \'5\' to add and edit hotel information.')
            print('Enter \'6\' to see hotel guess.')
            print('Enter \'7\' to user.')
            print('Enter \'0\' to exit.')

            try:
                input_key = int(input())
            except ValueError:
                print('Wrong Input, Try again.')
                continue

            if input_key == 1:
                self.add_room(BoosInterface)
                break
            elif input_key == 2:
                self.add_service(BoosInterface)
                break
            elif input_key == 3:
                self.rooms_view(BoosInterface)
                break
            elif input_key == 4:
                self.services_view(BoosInterface)
                break
            elif input_key == 5:
                self.hotel_information(BoosInterface)
            elif input_key == 6:
                self.hotel_users(BoosInterface)
            elif input_key == 7:
                UserInterface.main_menu(UserInterface, self.hotel)
            elif input_key == 0:
                sys.exit()
            else:
                print('Wrong Input.')

    def add_room(self):
        new_room = Room
        print('    *Add New Room*    \n')
        print('[for saving a new room you should finish process]')
        print('[don\'t worry about properly fault, you can edit them latter]')

        # room type
        while True:
            print('Room types : ')
            print('Enter \'1\' for \'SIMPLE\'.')
            print('Enter \'2\' for \'FIRST CLASS\'.')
            print('Enter \'3\' for \'VIP\'.')

            try:
                input_key = int(input())
            except ValueError:
                print('Wrong Input, Try again.')
                continue

            if input_key == 1:
                new_room.room_status = 'SIMPLE'
                break
            elif input_key == 2:
                new_room.room_status = 'FIRST CLASS'
                break
            elif input_key == 3:
                new_room.room_status = 'VIP'
                break
            elif input_key == 0:
                self.main_menu(BoosInterface, self.hotel)
            else:
                print('Wrong Input.')

        # room number
        while True:
            try:
                room_num = int(input('Enter room number : '))
                break
            except ValueError:
                print('Wrong input.')
                continue

        new_room.room_num = room_num

        # room beds
        while True:
            try:
                bed_num = int(input('Enter bed number : '))
                break
            except ValueError:
                print('Wrong input.')

        for bed_index in range(bed_num):
            result = set_bed_type(bed_index)
            new_room.bed_list.append(result[0])
            new_room.bed_num += result[1]

        while True:
            extra_bed = input('Does the room any extra bed? [YES:\'y\', NO:\'n\']').lower()
            if extra_bed == 'y':
                new_room.has_extra_bed = True
                break
            elif extra_bed == 'n':
                new_room.has_extra_bed = False
                break
            else:
                print('Wrong input.')

        # bathroom
        while True:
            bathroom = input('Has the room privacy bathroom? [YES:\'y\', NO:\'n\']').lower()
            if bathroom == 'y':
                new_room.has_bathroom = True
                break
            elif bathroom == 'n':
                new_room.has_bathroom = False
                break
            else:
                print('Wrong input.')

        # wc
        while True:
            wc = input('Has the room privacy wc? [YES:\'y\', NO:\'n\']').lower()
            if wc == 'y':
                new_room.has_wc = True
                break
            elif wc == 'n':
                new_room.has_wc = False
                break
            else:
                print('Wrong input.')

        # space
        while True:
            try:
                space = float(input('Enter space of the room [float format, sample 10.0] : '))
                new_room.space = space
                break
            except ValueError:
                print('Wrong input.')

        # floor
        while True:
            try:
                floor = int(input('What is the floor number of room? '))
                new_room.floor = floor
                break
            except ValueError:
                print('Wrong input.')

        # facilities
        while True:
            input_key = input('New facility [like \'cabinet\' or \'closet\', for break enter \'e\'] : ')
            if input_key.lower() == 'e':
                break
            else:
                new_room.facilities.append(input_key)

        # services
        print('Chose hotel services for room.\nServices list :')
        for item in self.hotel.services:
            print(f'{self.hotel.services.index(item)+1}_ {item.service_name} [Times:{item.service_times}]')

        while True:
            try:
                input_key = input('New service [enter service number for choose that, for break enter \'e\'] : ')
                if input_key.lower() == 'e':
                    break
                else:
                    new_service = self.hotel.services[int(input_key)-1]
                    new_service.person_number = bed_num
                    new_room.services.append(new_service)
            except IndexError and ValueError:
                print('Wrong input.')

        # comment
        print('Enter any comment about this room to attract guess[for break enter \'e\'] : ')
        while True:
            comment = input()
            if comment.lower() == 'e':
                break
            else:
                new_room.comment += comment

        # cost
        while True:
            try:
                cost = float(input('Enter cost of the room [float format, sample 10.0] : '))
                new_room.cost = cost
                break
            except ValueError:
                print('Wrong input.')

        self.hotel.rooms.append(new_room)
        self.main_menu(BoosInterface, self.hotel)

    def add_service(self):
        print('    *Add New Service*    \n')
        new_service = Service

        # service_name
        name = input('Enter service name : ')
        new_service.service_name = name

        # service times
        while True:
            time = input('Enter service times [time format ->14:40, for break enter \'e\'] : ')
            if time.lower() == 'e':
                break
            else:
                new_service.service_times.append(time)

        # comment
        print('Enter any comment about this service to attract guess[for break enter \'e\'] : ')
        while True:
            comment = input()
            if comment.lower() == 'e':
                break
            else:
                new_service.service_comment += comment

        # cost
        while True:
            try:
                cost = float(input('Enter cost of the service [float format, sample 10.0] : '))
                new_service.cost_per_person = cost
                break
            except ValueError:
                print('Wrong input.')

        self.hotel.services.append(new_service)
        self.main_menu(BoosInterface, self.hotel)

    def rooms_view(self):
        print('    *Room view*    \n')
        for room in self.hotel.rooms:
            print(f'{room.room_num}_ number bed: {room.bed_num}, cost: {room.cost}')
        while True:
            print('Chose room number to see it\'s details or delete[back: \'0\']')
            try:
                input_key = int(input())
                if input_key == 0:
                    self.main_menu(BoosInterface, self.hotel)
                else:
                    for room_index in self.hotel.rooms:
                        if room_index.room_num == input_key:
                            print(room_index.to_string(Service))
                            input('enter any key to back... ')
                            self.rooms_view(BoosInterface)
            except ValueError:
                print('Wrong input.')

    def services_view(self):
        print('    *Services view*    \n')
        counter = 1
        for service in self.hotel.services:
            print(f'{counter}_ name: {service.service_name}, cost per person: {service.cost_per_person}')
            counter += 1
        while True:
            print('Chose service number to see it\'s details or delete[back: \'0\']')
            try:
                input_key = int(input())
                if input_key == 0:
                    self.main_menu(BoosInterface, self.hotel)
                else:
                    print(self.hotel.services[input_key-1].to_string(Service))
                    input('enter any key to back... ')
                    self.services_view(BoosInterface)
            except ValueError and IndexError:
                print('Wrong input.')

    def hotel_information(self):
        pass

    def hotel_users(self):
        pass
