def get_random_password() -> str:
    # TODO написать функцию генерации случайных паролей
    import random
    import string
    N = 8  # нужная длина пароля
    passwt = string.ascii_uppercase + string.ascii_lowercase + string.digits + string.punctuation
    passw = random.sample(passwt, N)
    password = "".join(passw)
    return password


print(get_random_password())

