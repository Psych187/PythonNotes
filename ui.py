import Note


def create_note(number):
    title = check_len_text_input(
        input('Enter note name: '), number)
    body = check_len_text_input(
        input('Enter note description: '), number)
    return Note.Note(title=title, body=body)


def menu():
    print("\nThis is 'Notes' programm. Following functions available:\n\n1 - show all notes\n2 - add note\n3 - delete note\n4 - refactor note\n5 - choose note by date\n6 - show note by id\n7 - exit\n\nEnter func no: ")


def check_len_text_input(text, n):
    while len(text) <= n:
        print(f'Text should be longer than {n} symbols\n')
        text = input('Enter text: ')
    else:
        return text


def goodbuy():
    print("Come back soon!")