def password_level(passw):
    if len(passw) < 6:
        return 'Недопустимый пароль'
    elif passw.isalpha() and passw.lower():
        return 'Слабый пароль'
    elif passw.isdigit() and passw.lower():
        return 'Слабый пароль'
    elif passw.isalpha() and passw.islower():
        return 'Ненадежный пароль'
    elif passw.isdigit():
        return 'Ненадежный пароль'
    else:
        return 'Надежный пароль'


print(password_level("Qwerty"))
