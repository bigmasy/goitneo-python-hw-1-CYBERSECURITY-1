def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            return 'Give me name and phone please.'
        except KeyError:
            return 'Enter correct name please.'
        except IndexError:
            return 'Enter user name please.'
        
    return inner


def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args


@input_error
def add_contact(args, contacts):
    name, phone = args
    if name in contacts:
        return 'Contact already exists, if you want to change it, try the change command'
    else:
        contacts[name] = phone
        return 'Contact added'


@input_error
def change_contact(args, contacts):
    name, phone = args
    contacts[name] = phone
    return 'Contact is changed'


@input_error
def show_phone(args, contacts):
    name = args[0]
    return contacts[name]


def show_all_contacts(contacts):
    contacts_list = [f'{name}: {phone}' for name, phone in contacts.items()]
    return '\n'.join(contacts_list)