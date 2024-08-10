import bcrypt


class Vendedor:
    y = 1234

    def __init__(self, codigo, nombre, password):
        self.codigo = codigo
        self.nombre = nombre
        # hash password
        self.password = self.encriptar_password(password)

    def encriptar_password(self, password_original):
        bytes = password_original.encode('utf-8')
        salt = bcrypt.gensalt()
        hash = bcrypt.hashpw(bytes, salt)
        return hash

    def check_password(self, posible_password):
        password = posible_password.encode("utf-8")
        return bcrypt.checkpw(password, self.password)

    def __str__(self):
        return f"{self.nombre}"
