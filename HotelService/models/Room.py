class Room:
    room_num = 0
    room_status = ''
    bed_num = 0
    bed_list = []
    has_extra_bed = False
    has_bathroom = False
    has_wc = False
    space = 0.0
    floor = 0
    comment = ''
    services = []
    services_names = []
    facilities = []
    cost = 0.0
    is_fill = False

    def to_string(self):
        self.fill_service_names(Room)
        if self.is_fill:
            fill_situation = 'Sorry this roo is fill.'
        else:
            fill_situation = 'Empty room.'

        if self.has_extra_bed:
            extra_bed = 'one'
        else:
            extra_bed = '-'

        if self.has_bathroom:
            bathroom = 'Yes'
        else:
            bathroom = 'No'

        if self.has_wc:
            wc = 'Yes'
        else:
            wc = 'No'

        return f'{fill_situation}\n'\
            f'{self.room_status} room with {self.bed_num} beds{self.bed_list}, extra bed :{extra_bed}\n'\
            f'Just {self.cost}$\n'\
            f'more information...\n'\
            f'Space :{self.space}, in {self.floor} floor\n'\
            f'Facilities : {self.facilities}\n'\
            f'Services : {self.services_names}\n'\
            f'Privacy bathroom : {bathroom}\n'\
            f'Privacy wc : {wc}\n'\
            f'About this room : \n{self.comment}'

    def fill_service_names(self):
        for item in self.services:
            self.services_names.append(item.service_name)
