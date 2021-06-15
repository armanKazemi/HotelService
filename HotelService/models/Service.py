class Service:
    service_name = ''
    service_comment = ''
    person_number = 1
    cost_per_person = 0
    final_cost = 0
    service_times = []

    def get_service_name(self):
        return self.service_name

    def get_service_comment(self):
        return self.service_comment

    def get_person_number(self):
        return self.person_number

    def get_cost_per_person(self):
        return self.cost_per_person

    def get_final_cost(self):
        return self.person_number * self.person_number

    def get_service_times(self):
        return self.service_times

    def to_string(self):
        return f'Service name : {self.service_name}\n' \
            f'Cost per person : {self.cost_per_person}\n' \
            f'Final cost for {self.person_number} person : {self.final_cost}\n'\
            f'Service times : {self.service_times}\n'\
            f'More about this service : \n{self.service_comment}'
