class Hotel:
    hotel_name = ''
    hotel_stars_number = 0
    hotel_comment = ''
    hotel_address = {
        'State': '',
        'City': '',
        'Streets': [],
        'Alleys': [],
        'Extra': ''
    }
    hotel_communication_routes = {
        'Numbers': [],
        'Site': '',
        'Post_address': ''
    }
    hotel_facilities = []
    services = []
    rooms = []
    main_users = []
    all_users = []

    def set_address(self, new_address):
        self.hotel_address['State'] = new_address['state']
        self.hotel_address['City'] = new_address['city']
        self.hotel_address['Streets'] = new_address['streets']
        self.hotel_address['Alleys'] = new_address['alleys']
        self.hotel_address['Extra'] = new_address['extra']

    def set_communication_routes(self, new_communication_routes):
        self.hotel_communication_routes['Numbers'] = new_communication_routes['numbers']
        self.hotel_communication_routes['Site'] = new_communication_routes['site']
        self.hotel_communication_routes['Post_address'] = new_communication_routes['post_address']
