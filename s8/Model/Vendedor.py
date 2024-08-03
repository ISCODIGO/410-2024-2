import bcrypt


class Vendedor:
    def __init__(self, codigo, nombre, password):
        self.codigo = codigo
        self.nombre = nombre
        # hash password
        self.password = self.set_password(password)

    def set_password(self, raw_password):
        self.password = bcrypt.hashpw(
            raw_password.encode("utf-8"), bcrypt.gensalt()
        ).decode("utf-8")

    def check_password(self, raw_password):
        return bcrypt.checkpw(
            raw_password.encode("utf-8"), self.password.encode("utf-8")
        )

    def __str__(self):
        return f"{self.nombre}"
