# Числовая угадайка333333333
def number_guess():
    print('Добро пожаловать в числовую угадайку')
    try_count = 0
    input_random = 100
    def random_gen(input_random):
        import random
        random_number = random.randint(1, input_random + 1)
        print(random_number)
        return random_number

    def is_valid(num):
        if str(num).isdigit() and int(num) in range(1, 101):
            return True
        else:
            return False

    def the_game(input_number, random_number):

        if input_number < random_number:
            print('***Ваше число меньше загаданного, попробуйте еще разок***')

        elif input_number > random_number:
            print('***Ваше число больше загаданного, попробуйте еще разок***')

        elif input_number == random_number:
            print('***Вы угадали, поздравляем!***')

    while True:
        input_number = input('Введите число от 1 до 100:')
        if not is_valid(input_number):
            print('А может быть все-таки введем целое число от 1 до 100?')
            continue
        else:
            input_number = int(input_number)
            the_game(input_number, random_gen(input_random))
            try_count += 1
            print('Количество попыток', try_count)
            game_continue = input('Сыграем ещё раз? д/н:')
            if game_continue.lower() in ('д', 'да'):
                input_random = int(input('До какого числа загадывать? 100 Max'))
                continue
            else:
                print('Спасибо, что играли в числовую угадайку. Еще увидимся...')
                break



# Магический шар
def magic_ball():
    import random
    answers = ['Бесспорно', 'Предрешено', 'Никаких сомнений', 'Определённо да', 'Можешь быть уверен в этом', 'Мне кажется - да', 'Вероятнее всего', 'Хорошие перспективы', 'Знаки говорят - да', 'Да', 'Пока неясно, попробуй снова', 'Спроси позже', 'Лучше не рассказывать', 'Сейчас нельзя предсказать', 'Сконцентрируйся и спроси опять', 'Даже не думай', 'Мой ответ - нет', 'По моим данным - нет', 'Перспективы не очень хорошие', 'Весьма сомнительно']

    print('Привет Мир, я магический шар, и я знаю ответ на любой твой вопрос.')
    user_name = input('Как вас зовут?')
    print(f'***Привет {user_name}***')

    def choice(answers):
        return answers[random.randint(0, 19)]

    while True:
        question = input('Спросите меня, чтобы принять решение:')
        print(f'***{choice(answers)}***')
        again = input('Спросить ещё? д/н:')
        if again.lower() in ('д', 'да'):
            continue
        else:
            print('Возвращайся если возникнут вопросы!')
            break



# Генератор паролей
def password_generator():
    import random
    digits = '0123456789'
    lowercase_letters = 'abcdefghijklmnopqrstuvwxyz'
    uppercase_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    punctuation = '!#$%&*+-=?@^_'
    some_chars = 'il1Lo0O'
    password_cnt = input('Какое количество паролей сгенерировать?')
    password_len = input('Какой длины должен быть пароль (сколько знаков)?')

    def questions():
        chars = ''

        password_dig = input('Включать ли цифры? д/н:')
        if password_dig.lower() in ('д', 'да'):
            chars += digits

        password_upp = input('Включать ли прописные буквы? д/н:')
        if password_upp.lower() in ('д', 'да'):
            chars += uppercase_letters

        password_low = input('Включать ли строчные буквы? д/н:')
        if password_low.lower() in ('д', 'да'):
            chars += lowercase_letters

        password_pun = input('Включать ли символы? д/н:')
        if password_pun.lower() in ('д', 'да'):
            chars += punctuation

        password_wtf = input('Исключать ли неоднозначные символы (il1Lo0O)? д/н:')
        if password_wtf.lower() in ('д', 'да'):
            for i in some_chars:
                chars = chars.replace(i, '')

        return chars

    def generate_password(password_len, chars):
        for _ in range(int(password_cnt)):
            result = ''
            for j in range(int(password_len)):
                result += random.choice(chars)
            print(result)

    generate_password(password_len, questions())




# Шифр Цезаря
def caesar_encoding():
    alpha_en = 'abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz'
    alpha_ru = 'абвгдежзийклмнопрстуфхцчшщъыьэюяабвгдежзийклмнопрстуфхцчшщъыьэюя'

    direction = input('Зашифровать или Расшифровать? Введите Заш/Расш:')
    language = input('Какой алфавит применить? Анг/Рус:')
    if language.lower() in ('а', 'ан', 'анг'):
        language = alpha_en
    elif language.lower() in ('р', 'ру', 'рус'):
        language = alpha_ru
    else:
        print('чо?')
    step = input('Введите шаг сдвига (1-25) или 0, если неизвестно:')
    text = input('Введите текст:')

    def encrypt(text):
        encrypted_text = ''
        for i in text:
            if i.isalpha():
                encrypted_text += language[language.index(i.lower()) + int(step)].upper() if i == i.upper() else language[language.index(i.lower()) + int(step)]
            else:
                encrypted_text += i
        print(f'*** {encrypted_text} ***')

    def decrypt(text):
        decrypted_text = ''
        for i in text:
            if i.isalpha():
                decrypted_text += language[language.index(i.lower()) - int(step)].upper() if i == i.upper() else language[language.index(i.lower()) - int(step)]
            else:
                decrypted_text += i
        print(f'*** {decrypted_text} ***')


    if direction.lower() in ('з', 'за', 'заш'):
        encrypt(text)
    elif direction.lower() in ('р', 'ра', 'рас', 'расш'):
        if int(step) == 0:
            step = 1
            for _ in range(1, 26):
                decrypt(text)
                step += 1
        else:
            decrypt(text)
    else:
        print('Чо?')


# Угадайка слов
def word_guess():
    import random
    import time
    word_list = ['жопа', 'сиська', 'рука', 'глаз', 'волос', 'голова', 'нога', 'живот']
    tries = 0

    def get_word(word_list):
        return random.choice(word_list)

    # функция получения текущего состояния
    def display_hangman(tries):
        stages = [  # финальное состояние: голова, торс, обе руки, обе ноги
                    '''
                       --------
                       |      |
                       |      O
                       |     \\|/
                       |      |
                       |     / \\
                       -
                    ''',
                    # голова, торс, обе руки, одна нога
                    '''
                       --------
                       |      |
                       |      O
                       |     \\|/
                       |      |
                       |     /
                       -
                    ''',
                    # голова, торс, обе руки
                    '''
                       --------
                       |      |
                       |      O
                       |     \\|/
                       |      |
                       |
                       -
                    ''',
                    # голова, торс и одна рука
                    '''
                       --------
                       |      |
                       |      O
                       |     \\|
                       |      |
                       |
                       -
                    ''',
                    # голова и торс
                    '''
                       --------
                       |      |
                       |      O
                       |      |
                       |      |
                       |
                       -
                    ''',
                    # голова
                    '''
                       --------
                       |      |
                       |      O
                       |
                       |
                       |
                       -
                    ''',
                    # начальное состояние
                    '''
                       --------
                       |      |
                       |
                       |
                       |
                       |
                       -
                    '''
        ]
        return stages[tries]

    word = get_word(word_list).lower()

    def play(word):
        word_completion = '_' * len(word)  # строка, содержащая символы _ на каждую букву задуманного слова
        guessed = False                    # сигнальная метка
        guessed_letters = []               # список уже названных букв
        guessed_words = []                 # список уже названных слов
        tries = 6                          # количество попыток

        print('Давайте играть в угадайку слов!')
        print('Загаданное слово:', word_completion)

        while tries > 0:
            print(display_hangman(tries))
            time.sleep(0.5)
            answer = input('Введите букву или слово: ').lower()

            if answer.isalpha() and len(answer) >= 1:
                if answer not in guessed_letters and len(answer) == 1:
                    guessed_letters.append(answer)
                    if answer in word:
                        for i in range(len(word)):
                            if word[i] == answer:
                                word_completion = word_completion[: i] + answer.upper() + word_completion[i + 1 :]

                        if word_completion.lower() == word:
                            guessed = True
                            break
                        else:
                            tries -= 1
                            print(word_completion, ': Осталось попыток:', tries)
                    else:
                        tries -= 1
                        print(word_completion, ': Нет такой буквы. Попробуйте ещё раз. Осталось попыток:', tries)
                elif answer not in guessed_words and len(answer) > 1:
                    guessed_words.append(answer)
                    if answer == word:
                        guessed = True
                        break
                    else:
                        tries -= 1
                        print(word_completion, ': Не угадали. Попробуйте ещё раз. Осталось попыток:', tries)
                else:
                    print('Это уже было. Попытка не засчитана. Попробуйте ещё раз.')
            else:
                print('Это не слово. Попробуйте ещё раз.')

        if guessed:
            print('*** Поздравляем, вы угадали слово! Вы победили! -', word.upper())
        else:
            print(display_hangman(tries))
            print('* Вы проиграли * Слово -', word.upper())

        time.sleep(0.5)
        if input('Сыграем ещё раз? Да/Нет: ').lower() in ('д', 'да'):
            play(word)
    play(word)


choice = input(f'1 - Числовая угадайка,\n2 - Магический шар,\n3 - Генератор паролей,\n4 - Шифр Цезаря,\n5 - Угадайка слов')
if int(choice) == '1':
    number_guess()
elif choice == '2':
    magic_ball()
elif choice == '3':
    password_generator()
elif choice == '4':
    caesar_encoding()
elif choice == '5':
    word_guess()