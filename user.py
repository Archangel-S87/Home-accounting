import hashlib


class User:
    def __init__(self, db):
        self.db = db
        pass

    def checkLogin(self, login, password):
        self.db.cursor.execute('SELECT * FROM users WHERE login=?', (login,))
        user = self.db.cursor.fetchone()
        if user:
            print(user)
        else:
            print('Not user')
        return False

    def registerUser(self, data):
        count = self.db.getCount('users', f'email="{data["email"]}" OR login="{data["login"]}"')
        print(count)
        pass


h = hashlib.md5(b'password')
p = h.hexdigest()   # Пароль, сохраненный в базе
h2 = hashlib.md5(b'password')   # Пароль, введенный пользователем
if p == h2.hexdigest():
    print("Пароль правильный")
