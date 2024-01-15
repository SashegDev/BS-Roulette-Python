import random


class NoAmmoException(Exception):
    def __init__(self, msg="Shootgun don't have ammo!"):
        super().__init__(msg)


class Shootgun:
    """Класс, реализующий механику дробовика для Buckshoot Roulete"""
    def __init__(self, n):
        self.n = n
        self.lives = 0
        self.blanks = 0
    def random_fill(self):
        """Рандомно заполняет свободное пространство дробовика случайными патронами"""
        self.arr = [bool(random.randint(0, 1)) for i in range(self.n)]
        self.lives = self.arr.count(True)
        self.blanks = self.arr.count(False)
    def get_lives(self):
        """Возвращает кол-во настоящих патронов"""
        return self.lives
    def get_blanks(self):
        """Возвращает кол-во пустых патронов"""
        return self.blanks
    def message_for_dev(self):
        """Сообщение о порядке патронов в дробовике, в основном для разработчика"""
        res = ""
        for i in range(len(self.arr)):
            if self.arr[i]:
                res += "live"
            else:
                res += "blank"
            res += " "
        return res[:len(res)-1]
    def message_for_play(self):
        """Сообщение о кол-ве настоящих и пустых патронов, для игрока"""
        return f"Lives: {self.lives}; Blanks: {self.blanks}"
    def shoot(self):
        """'Выстреливает' патрон и возвращает каким он был, если патронов нет, то выбрасывает NoAmmoException"""
        if len(self.arr) != 0:
            res = self.arr.pop(0)
            if res:
                self.lives -= 1
            else:
                self.blanks -= 1
            return res
        else:
            raise NoAmmoException()