def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

def add_contact(args, contacts):
    if len(args) != 2:
        return 'Wrong arguments to the command. Try again.'
    else:
        name, phone = args
        if name in contacts:
            return 'Contact already exists, if you want to change it, try the change command'
        else:
            contacts[name] = phone
            return 'Contact added'

def change_contact(args, contacts):
    if len(args) != 2:
        return 'Wrong arguments to the command. Try again.'
    else:
        name, phone = args
        if name in contacts:
            contacts[name] = phone
            return 'Contact is changed'
        else:
            contacts[name] = phone
            return f'There was no contact with the name {name}, contact added'

def show_phone(args, contacts):
    if len(args) != 1:
        return 'Wrong arguments to the command. Try again.'
    else:
        name = args[0]
        if name in contacts:
            return contacts[name]
        else:
            return f'There is no contact with the name {name}'

def show_all_contacts(contacts):
    contacts_list = [f'{name}: {phone}' for name, phone in contacts.items()]
    return '\n'.join(contacts_list)

