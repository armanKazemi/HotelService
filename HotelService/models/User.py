class User:
    name = ''
    age = 0
    phone_num = ''
    email_address = ''
    comrades_num = 0
    comrades = []
    room_num = 0
    user_services = []
    bill = 0
    is_payed = False

    def add_comrade(self, new_comrade):
        comrade = {
            'name': new_comrade['comrade_name'],
            'age': new_comrade['comrade_age'],
            'phone_num': new_comrade['comrade_phone_num'],
            'room_num': new_comrade['room_num']
        }
        self.comrades.append(comrade)

    def add_to_bill(self, cost):
        self.bill += cost
