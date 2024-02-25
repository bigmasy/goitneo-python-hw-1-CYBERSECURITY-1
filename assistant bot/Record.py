from Name import Name
from Phone import Phone


class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []
    

    def add_phone(self,phone):
        self.phones.append(Phone(phone))

    def remove_phone(self, phone):
        for p in self.phones:
            if p.value == phone:
                self.phones.remove(p)
                break

    def edit_phone(self, old_phone, new_phone):
        for p in self.phones:
            if p.value == old_phone:
                p.value = new_phone
                break

    def find_phone(self, phone):
        for p in self.phones:
            if p.value == phone:
                return p
        return None

    def __str__(self):
        return f'Contact name: {self.name.value}, phones: {"; ".join(p.value for p in self.phones)}'