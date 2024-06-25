users = {}


def show_stat(user):
    print(user)
    print(users)
    return f"Ваша статистика:\nПобед: {users[user]['wins']}\nПоражений: {users[user]['loses']}\nНичьи: {users[user]['draws']}\nВсего игр: {users[user]['tries']}"
