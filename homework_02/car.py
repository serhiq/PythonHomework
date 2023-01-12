"""
создайте класс `Car`, наследник `Vehicle`
"""
from base import Vehicle # в README раздел *Важно* в самом начале указывает так не делать
from homework_02.base import Vehicle


class Car(Vehicle):
    def __init__(self, weight, fuel, fuel_consumption):
        # если аргументы родительского метода совпадают с дочерним, 
        # то чтобы не зависеть от изменения аргументов родительского метода можно использовать `*args` и `**kwargs`
        # полноценной статьи про это не вижу, но что нашел: https://docs.python.org/3/glossary.html#term-parameter и https://www.digitalocean.com/community/tutorials/how-to-use-args-and-kwargs-in-python-3
        super().__init__(weight, fuel, fuel_consumption)
        self.engine = None

    def set_engine(self, engine):
        self.engine = engine
