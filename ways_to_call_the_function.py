# Домашняя работа по уроку "Способы вызова функции"
# Задача "Рассылка писем"
# Цель: закрепить знания о параметрах по умолчанию и именованных аргументах.

def send_email(message, recipient, *, sender="university.help@gmail.com"):
    valid_list = [".com", ".ru", ".net"]
    # Проверка корректности email-адреса отправителя: sender
    if '@' not in sender or not any(sender.endswith(i) for i in valid_list):
        print(f'Невозможно отправить письмо с адреса {sender} на адрес {recipient}')
        return
    # Проверка корректности email-адреса получателя: recipient
    elif '@' not in recipient or not any(recipient.endswith(i) for i in valid_list):
        print(f'Невозможно отправить письмо с адреса {sender} на адрес {recipient}')

    # Проверка на отправку самому себе
    elif sender == recipient:
        print("Нельзя отправить письмо самому себе!")
        return

    # Проверка на отправителя по умолчанию
    elif sender == "university.help@gmail.com":
        print(f'Письмо успешно отправлено с адреса {sender} на адрес {recipient}')
        return

    else:
        print(f'НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса {sender} на адрес {recipient}')

# Примеры выполнения функции
send_email('Это сообщение для проверки связи', 'vasyok1337@gmail.com')
send_email('Вы видите это сообщение как лучший студент курса!', 'urban.fan@mail.ru', sender='urban.info@gmail.com')
send_email('Пожалуйста, исправьте задание', 'urban.student@mail.ru', sender='urban.teacher@mail.uk')
send_email('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru', sender='urban.teacher@mail.ru')
