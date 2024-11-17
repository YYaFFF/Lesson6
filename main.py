password = input("Введите пароль: ")
SCORE = 0


def very_long(password):
    return len(password) >= 12


def has_digit(password):
    return any(digit.isdigit() for digit in password)


def has_letter(password):
    return any(letter.isalpha() for letter in password)


def has_upper_letters(password):
    return any(letter.isupper() for letter in password)


def has_lower_letters(password):
    return any(letter.islower() for letter in password)


verification = [
    very_long,
    has_digit,
    has_letter,
    has_upper_letters,
    has_lower_letters
]

for verification in verification:
    result = verification(password)
    if result:
        SCORE += 2
print(f"Рейтинг пароля: {SCORE}")
