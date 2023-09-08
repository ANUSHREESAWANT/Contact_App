from IPython.display import clear_output

contacts = [{'name': 'anu', 'number': 9876543210, 'email': 'anu@gmail.com'},
            {'name': 'munu', 'number': 9876543210, 'email': 'munu@gmail.com'},
            {'name': 'kutu', 'number': 9876543210, 'email': 'kutu@gmail.com'}]


def show_contacts(contacts):
    for i in contacts:
        print('\n', i)


def add_contact(contacts):
    name = input("Enter your name: ")
    mobile = str(input("Enter your number: "))
    email = input("Enter your Email: ")
    contacts.append({'name': name, 'number': mobile, 'email': email})


def open_contact(contacts):
    name = input("Enter your name to open: ")
    for i in contacts:
        if i['name'] == name:
            print(i)


def update_contact(contacts):
    name = input("Enter your name for update: ")
    if contacts['name'] == name:
        for i, j in enumerate(contacts):
            name = input("Enter Your Name: ")
            mobile = str(input("Enter your number: "))
            email = input("Enter your Email: ")
            contacts[i]['name'] = name
            contacts[i]['number'] = mobile
            contacts[i]['email'] = email

def delete_contact(contacts):
    name = input("Enter your name for delet: ")
    for i, j in enumerate(contacts):
        if j['name'] == name:
            del contacts[i]


while True:
    action = input(
        "Press 'a' - add contact, 'o' - open contact, 'u' - update cotact, 'd' - delet contact, 'q' - quit")

    if action == 'a':
        add_contact(contacts)
        show_contacts(contacts)
        break

    elif action == 'o':
        open_contact(contacts)
        break

    elif action == 'u':
        update_contact(contacts)
        show_contacts(contacts)
        break

    elif action == 'd':
        delete_contact(contacts)
        show_contacts(contacts)
        break

    elif action == 'q':
        break

    else:
        print('incorrect choice')


