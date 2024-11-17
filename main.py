import urwid


def very_long(password):
    return len(password) >= 12


def has_digit(password):
    return any(digit.isdigit() for digit in password)


def has_letter(password):
    return any(letter.isalpha() for letter in password)


def has_upper_letters(password):
    return any(letter.isupper() for letter in password)


def has_lower_letters(password):
    return any(letter.islower() for letter in password or "Пароль должен содержать букву")


def has_symbols(password):
    symbols = "!@#$%^&*()-_=+[]{}|;:'\",.<>?/"
    return any(symbol.find(symbols) for symbol in password)


def calculate_password_strength(password):
    score = 0
    verification = [
        very_long,
        has_digit,
        has_letter,
        has_upper_letters,
        has_lower_letters,
        has_symbols
    ]
    for verification in verification:
        if verification(password):
            score += 2
    return score


def on_ask_change(edit, new_edit_text):
    score = calculate_password_strength(new_edit_text)
    reply.set_text("Рейтинг пароля: %d" % score)


ask = urwid.Edit('Введите пароль :', mask='*')
reply = urwid.Text("")
menu = urwid.Pile([ask, reply])
menu = urwid.Filler(menu, valign='top')
urwid.connect_signal(ask, 'change', on_ask_change)
urwid.MainLoop(menu).run()
